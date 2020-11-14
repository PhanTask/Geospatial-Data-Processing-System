# -*- coding:utf-8 -*-

from shapely.ops import cascaded_union
from osgeo import gdal
import ogr
import os
import time
import multiprocessing as mp
from PySide2 import QtCore
from logger.logRcd import logRcd
import numpy as np
from shapely.geometry import shape,Polygon
import json
import shutil

if __name__ == "__main__":
    #srcFilename = r"E:\20180401中文\data\多波段异常值\H51G030014\H51G030014.img" # r"E:\20180401中文\data\多波段异常值\H51G082007\H51G082007.img"
    srcFilename = r"E:\arcgisDataLab\clip\clip_mon.img"
    dstFilename = r"E:\arcgisDataLab\clip_mon.img"
    driver = gdal.GetDriverByName('HFA')
    domSrcDS = gdal.Open(srcFilename)
    domDstDS = driver.Create(dstFilename, domSrcDS.RasterXSize, domSrcDS.RasterYSize,
                             domSrcDS.RasterCount, gdal.GDT_Byte, options=['COMPRESS=RLE'])
    GeoTransform = domSrcDS.GetGeoTransform()
    Projection = domSrcDS.GetProjection()
    domDstDS.SetGeoTransform(GeoTransform)
    domDstDS.SetProjection(Projection)

    kwargs = {'format': 'HFA',
            'colors': 255,
            'nearDist': 50,
            'maxNonBlack': 20,
            'delNum': 4,
            'setMask': True
            }

    # gdal.Nearblack(domDstDS,
    #                domSrcDS,
    #                    format=kwargs['format'],
    #                    colors=[tuple(kwargs['colors'] for i in range(domSrcDS.RasterCount))],
    #                    nearDist=kwargs['nearDist'],
    #                    maxNonBlack=kwargs['maxNonBlack'],
    #                    setMask=kwargs['setMask'],
    #                    )

    # 这里不关闭数据集的话，msk数据将不能保存，下一步没法用。不用nearblack及其msk的话就不用考虑了
    # domDstDS = None
    # domDstDS = gdal.Open(dstFilename,gdal.GA_Update)

    rowNum = domDstDS.RasterYSize
    columnNum = domDstDS.RasterXSize

    rowblockNum = int((rowNum - 1) / 2048) + 1
    colblockNum = int((columnNum - 1) / 2048) + 1

    # mskDS = gdal.Open(dstFilename + '.msk',gdal.GA_Update)

    # 分块检查异常值手动生成掩膜的方案
    mskDS = driver.Create(dstFilename.replace('.img', '_M.img'), domSrcDS.RasterXSize,
                          domSrcDS.RasterYSize,
                          1, gdal.GDT_Byte, options=['COMPRESS=RLE'])

    mskDS.SetGeoTransform(GeoTransform)
    mskDS.SetProjection(Projection)

    delNum = kwargs['delNum']

    mskBand = mskDS.GetRasterBand(1)

    for rowstep in range(rowblockNum):
        for colstep in range(colblockNum):
            rowpafNum = 2048
            colpafNum = 2048
            if (rowstep == rowblockNum - 1):
                rowpafNum = int((rowNum - 1) % 2048) + 1
            if (colstep == colblockNum - 1):
                colpafNum = int((columnNum - 1) % 2048) + 1
            mskArray = np.zeros((rowpafNum, colpafNum),
                                dtype=np.int8)  # np.ones(rowpafNum, colpafNum) * 255 # mskBand.ReadAsArray(colstep * 2048, rowstep * 2048, colpafNum, rowpafNum)
            for i in range(domSrcDS.RasterCount):
                band = domSrcDS.GetRasterBand(i + 1)
                domSrcNoData = band.GetNoDataValue()
                tempArray = band.ReadAsArray(colstep * 2048, rowstep * 2048, colpafNum, rowpafNum)
                mskArray = np.where((mskArray == 0) & (((tempArray <= kwargs['colors'] + kwargs['nearDist']) &
                                                        (tempArray >= kwargs['colors'] - kwargs['nearDist'])) |
                                                       (tempArray == domSrcNoData)), 0, 255)
                band = None
            mskBand.WriteArray(mskArray, colstep * 2048, rowstep * 2048)
    gdal.SieveFilter(srcBand=mskBand, maskBand=None, dstBand=mskBand, threshold=(1024))

    # if delNum != 0:
    unit = abs(GeoTransform[5])
    mskLessDS = driver.Create(dstFilename.replace('.img', '_N.img'), domSrcDS.RasterXSize,
                              domSrcDS.RasterYSize, 1, gdal.GDT_Byte, options=['COMPRESS=RLE'])

    mskLessDS.SetGeoTransform(GeoTransform)
    mskLessDS.SetProjection(Projection)

    # mskLessBand = mskLessDS.GetRasterBand(1)

    shpFilename = dstFilename.replace('.img', '_N.shp')
    dstLayername = "POLYGONIZED"
    drv = ogr.GetDriverByName("ESRI Shapefile")
    dst_ds = drv.CreateDataSource(shpFilename)
    dst_layer = dst_ds.CreateLayer(dstLayername, srs=None)

    fd = ogr.FieldDefn("Status", ogr.OFTInteger)
    dst_layer.CreateField(fd)
    dst_field = dst_layer.FindFieldIndex("Status", 1)

    gdal.Polygonize(mskBand, None, dst_layer, dst_field, [], callback=None)

    dst_ds = None
    dst_ds = ogr.Open(shpFilename, 1)
    dst_layer2 = dst_ds.GetLayer(0)

    maxAreaFID = None
    maxTempArea = 0
    delIndexList = []
    mergeIndexList = []
    mergePolyList = []
    f = dst_layer2.GetNextFeature()
    while f is not None:
        # for f in dst_layer2:
        if f.GetField('status') == 0:
            delIndexList.append(f.GetFID())
        else:
            mergeIndexList.append(f.GetFID())
            mergePolyList.append(shape(json.loads(f.geometry().ExportToJson())))
        # else:
        #     if f.geometry().GetArea() > maxTempArea:
        #         if maxAreaFID != None:
        #             delIndexList.append(maxAreaFID)
        #         maxAreaFID = f.GetFID()
        #         maxTempArea = f.geometry().GetArea()
        #     else:
        #         delIndexList.append(f.GetFID())
        f = None
        f = dst_layer2.GetNextFeature()

    # poly = cascaded_union(mergePolyList)
    [dst_layer2.DeleteFeature(i) for i in delIndexList]
    [dst_layer2.DeleteFeature(i) for i in mergeIndexList[1:]]

    feat = dst_layer2.GetFeature(mergeIndexList[0])

    # geo = feat.geometry()
    # # ogr的缓冲区无法指定笔帽和合并效果
    # # geosimple = geo.Buffer(10 * unit, quadsecs = 2).Buffer(-10 * unit, quadsecs = 2)#.Simplify(5 * unit)
    # # geobf = geo.Buffer(distance=0 - (delNum * unit), quadsecs = 2)
    # poly = shape(json.loads(geo.ExportToJson()))

    # simplePoly = poly#None
    # if poly.geom_type == 'Polygon':
    #     simplePoly = Polygon(poly.exterior)
    # else:
    #     maxArea = 0
    #     maxExt = None
    #     for p in poly:
    #         if (p.area > maxArea):
    #             maxArea = p.area
    #             maxExt = p.exterior
    #     simplePoly = Polygon(maxExt)
    reducePolyList = []
    for simplePoly in mergePolyList:
        if simplePoly.geom_type == 'Polygon':
            simplePoly = Polygon(simplePoly.exterior)
        else:
            maxArea = 0
            maxExt = None
            for p in simplePoly:
                if (p.area > maxArea):
                    maxArea = p.area
                    maxExt = p.exterior
            simplePoly = Polygon(maxExt)
        fx = simplePoly.buffer(distance=kwargs['maxNonBlack'] * unit, cap_style=1, join_style=2).buffer(
            distance=-(kwargs['maxNonBlack'] * unit), cap_style=1, join_style=2)
        reducefx = fx
        if delNum != 0:
            reducefx = fx.buffer(distance=-(delNum * unit), cap_style=1, join_style=3)
        if reducefx.geom_type == 'Polygon':
            reducefx = Polygon(reducefx.exterior)
        else:
            maxArea = 0
            maxExt = None
            for p in reducefx:
                if (p.area > maxArea):
                    maxArea = p.area
                    maxExt = p.exterior
            reducefx = Polygon(maxExt)
        reducePolyList.append(reducefx)

    # simplePoly = None
    # if reducefx.geom_type == 'Polygon':
    #     simplePoly = Polygon(reducefx.exterior)
    # else:
    #     maxArea = 0
    #     maxExt = None
    #     for p in reducefx:
    #         if (p.area > maxArea):
    #             maxArea = p.area
    #             maxExt = p.exterior
    #     simplePoly = Polygon(maxExt)

    poly = cascaded_union(reducePolyList)

    geobf = ogr.CreateGeometryFromWkb(poly.wkb)

    feat.SetGeometry(geobf)
    dst_layer2.SetFeature(feat)
    dst_ds = None

    gdal.Rasterize(mskLessDS, shpFilename, attribute='status')

    mskBand = None
    mskBand = mskLessDS.GetRasterBand(1)
    # gdal.SieveFilter(srcBand=mskBand, maskBand=None, dstBand=mskBand, threshold=1024)

    mskList = mskBand.GetHistogram(-0.5, 255.5, buckets=256, include_out_of_range=0, approx_ok=0)

    for rowstep in range(rowblockNum):
        for colstep in range(colblockNum):
            rowpafNum = 2048
            colpafNum = 2048
            if (rowstep == rowblockNum - 1):
                rowpafNum = int((rowNum - 1) % 2048) + 1
            if (colstep == colblockNum - 1):
                colpafNum = int((columnNum - 1) % 2048) + 1
            for i in range(domDstDS.RasterCount):
                srcband = domSrcDS.GetRasterBand(i + 1)
                band = domDstDS.GetRasterBand(i + 1)
                band.SetNoDataValue(255)
                temparray = srcband.ReadAsArray(colstep * 2048, rowstep * 2048, colpafNum, rowpafNum)
                tempmask = mskBand.ReadAsArray(colstep * 2048, rowstep * 2048, colpafNum, rowpafNum)
                temparray = np.where(temparray == 255, 254, temparray)
                temp = np.where(tempmask == 0, 255, temparray)
                band.WriteArray(temp, colstep * 2048, rowstep * 2048)