# -*- coding:utf-8 -*-

from implements import domImpl
import ogr
import gdal
import os
import numpy as np

if __name__ == '__main__':
    # def asd():
    #     driver = ogr.GetDriverByName("FileGDB")
    #     print(driver)
    #     indexGDFrame = driver.Open(r'E:\武大质检程序样例数据\影像\2自动检查覆盖范围\1987年索引表\AR_005_1987_1_TMQ.gdb', 0)
    #     print(indexGDFrame)
    # # domProcesser = domImpl.domImpl(domDirPath = r"G:\武大质检程序样例数据\影像\1自动处理影像异常值",
    # #                                outlierValue=255,
    # #                                fileType = "img")
    # # domProcesser.getDomPathList()
    # # domProcesser.domOutlierRemover()
    # try:
    #     print("ready")
    #     asd()
    #     print("pass")
    # except Exception as e:
    #     print(e.__str__())
    # # indexGDFrame = driver.Open(r'E:\武大质检程序样例数据\影像\2自动检查覆盖范围\1987年索引表\AR_005_1987_1_TMQ.gdb', 1)
    # # print(indexGDFrame)
    # srcFilename  = r'E:/武大质检程序样例数据/DEM样例数据/h50g095096_100m_to_wu.img'
    # dstFilename = r'E:/武大质检程序样例数据/DEM样例数据/result/h50g095096_100m_to_wu.shp'
    # tempFilename = os.path.splitext(dstFilename)[0] + '_temp.img'
    #
    # driver = gdal.GetDriverByName('HFA')
    # demSrcDS = gdal.Open(srcFilename)
    # demDstDS = driver.Create(tempFilename, demSrcDS.RasterXSize, demSrcDS.RasterYSize,
    #                          demSrcDS.RasterCount, gdal.GDT_Byte, options=['COMPRESS=RLE'])
    # GeoTransform = demSrcDS.GetGeoTransform()
    # Projection = demSrcDS.GetProjection()
    # demDstDS.SetGeoTransform(GeoTransform)
    # demDstDS.SetProjection(Projection)
    #
    # rowNum = demDstDS.RasterYSize
    # columnNum = demDstDS.RasterXSize
    #
    # rowblockNum = int((rowNum - 1) / 1024) + 1
    # colblockNum = int((columnNum - 1) / 1024) + 1
    #
    # valueRange = (20,8000)
    #
    # for rowstep in range(rowblockNum):
    #     for colstep in range(colblockNum):
    #         rowpafNum = 1024
    #         colpafNum = 1024
    #         if (rowstep == rowblockNum - 1):
    #             rowpafNum = int((rowNum - 1) % 1024) + 1
    #         if (colstep == colblockNum - 1):
    #             colpafNum = int((columnNum - 1) % 1024) + 1
    #         for i in range(demDstDS.RasterCount):
    #             dstBand = demDstDS.GetRasterBand(i + 1)
    #             srcBand = demSrcDS.GetRasterBand(i + 1)
    #             srcArray = srcBand.ReadAsArray(colstep * 1024, rowstep * 1024, colpafNum, rowpafNum)
    #             temp = np.where((srcArray >= valueRange[0]) & (srcArray <= valueRange[1]), 0, 255)
    #             dstBand.WriteArray(temp, colstep * 1024, rowstep * 1024)
    #
    # demSrcDS = None
    # demDstDS = None
    #
    # dstLayername = "POLYGONIZED"
    # drv = ogr.GetDriverByName("ESRI Shapefile")
    # dst_ds = drv.CreateDataSource(dstFilename)
    # dst_layer = dst_ds.CreateLayer(dstLayername, srs=None)
    #
    # fd = ogr.FieldDefn("Status", ogr.OFTInteger)
    # dst_layer.CreateField(fd)
    # dst_field = 0
    #
    # demDstDS = gdal.Open(tempFilename)
    # dstBand = demDstDS.GetRasterBand(1)
    # gdal.Polygonize(dstBand, None, dst_layer, dst_field, [], callback=None)
    #
    # dst_ds = None
    # demDstDS = None

    mskDS = gdal.Open(r'E:\20180401中文\data\dataLab\H51G030014\H51G030014.img.msk')
    delNum = 2
    geot = mskDS.GetGeoTransform()
    proj = mskDS.GetProjection()

    driver = gdal.GetDriverByName('HFA')
    dstDS = driver.Create(r'E:\20180401中文\data\dataLab\H51G030014\H51G030014_N.img', mskDS.RasterXSize, mskDS.RasterYSize,
                          mskDS.RasterCount, gdal.GDT_Byte, options=['COMPRESS=RLE'])
    dstDS.SetGeoTransform(geot)
    dstDS.SetProjection(proj)

    #unit = abs(geot[5])
    mskBand = mskDS.GetRasterBand(1)

    dstFilename = r'E:\20180401中文\data\dataLab\H51G030014\polygon.shp'
    dstLayername = "POLYGONIZED"
    drv = ogr.GetDriverByName("ESRI Shapefile")
    dst_ds = drv.CreateDataSource(dstFilename)
    dst_layer = dst_ds.CreateLayer(dstLayername, srs=None)

    fd = ogr.FieldDefn("Status", ogr.OFTInteger)
    dst_layer.CreateField(fd)
    dst_field = dst_layer.FindFieldIndex("Status", 1)

    gdal.Polygonize(mskBand, None, dst_layer, dst_field, [], callback=None)

    #polygonDS = ogr.Open(r'E:\20180401中文\data\H51G030014\polygon.shp', 1)
    #layer = polygonDS.GetLayer(0)
    feat = dst_layer.GetFeature(0)
    #dst_layer.DeleteFeature(1)
    geo = feat.geometry()
    geobf = geo.Buffer(distance=0 - (delNum * 0.000005) , quadsecs = 1)
    feat.SetGeometry(geobf)
    dst_layer.SetFeature(feat)
    dst_ds = None

    gdal.Rasterize(dstDS,dstFilename,attribute = 'status')

