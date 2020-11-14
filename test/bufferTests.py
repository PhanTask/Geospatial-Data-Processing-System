from osgeo import gdal
import ogr
import numpy as np
from shapely.geometry import shape,Polygon
from shapely.ops import cascaded_union, unary_union
import json
import os

srcFilename = r'D:\1工作空间\数字正射影像DOM\to饶\H51G030014_P\H51G030014_P.img'
# srcFilename = r'D:\1工作空间\数字正射影像DOM\3\3011-40540_PWrap.img'
dstFilename = r'D:\1工作空间\result730\3008-40540_PWrap.img'

kwargs = {}
kwargs['delNum'] = 0
kwargs['colors'] = 255
kwargs['nearDist'] = 10
kwargs['ext'] = 'img'
kwargs['maxNonBlack'] = 20

blockSize = 2048
gdal.AllRegister()
gdal.SetConfigOption('TIFF_USE_OVR', 'YES')
gdal.SetConfigOption('HFA_USE_RRD', 'YES')
# gdal.SetConfigOption('JPEG_QUALITY_OVERVIEW', '50')
# gdal.SetConfigOption('HFA_COMPRESS_OVR', 'YES')
imgdriver = gdal.GetDriverByName('HFA')
driver = gdal.GetDriverByName('HFA')
domSrcDS = gdal.Open(srcFilename)

COMPRESSoptions = ['COMPRESS=RLE']

domDstDS = driver.Create(dstFilename, domSrcDS.RasterXSize, domSrcDS.RasterYSize,
                         domSrcDS.RasterCount, gdal.GDT_Byte, options=COMPRESSoptions)

GeoTransform = domSrcDS.GetGeoTransform()
Projection = domSrcDS.GetProjection()
domDstDS.SetGeoTransform(GeoTransform)
domDstDS.SetProjection(Projection)

rowNum = domDstDS.RasterYSize
columnNum = domDstDS.RasterXSize

rowblockNum=int((rowNum-1)/blockSize)+1
colblockNum=int((columnNum-1)/blockSize)+1

# mskDS = gdal.Open(dstFilename + '.msk',gdal.GA_Update)

# 分块检查异常值手动生成掩膜的方案
mskDS = imgdriver.Create(dstFilename.replace('.' + kwargs['ext'], '_M.img'), domSrcDS.RasterXSize,
                      domSrcDS.RasterYSize,
                          1, gdal.GDT_Byte, options=['COMPRESS=RLE'])

mskDS.SetGeoTransform(GeoTransform)
mskDS.SetProjection(Projection)

delNum = kwargs['delNum']

mskBand = mskDS.GetRasterBand(1)

for rowstep in range(rowblockNum):
    for colstep in range(colblockNum):
        rowpafNum = blockSize
        colpafNum = blockSize
        if (rowstep == rowblockNum - 1):
            rowpafNum = int((rowNum - 1) % blockSize) + 1
        if (colstep == colblockNum - 1):
            colpafNum = int((columnNum - 1) % blockSize) + 1
        mskArray = np.zeros((rowpafNum, colpafNum), dtype=np.int8) # np.ones(rowpafNum, colpafNum) * 255 # mskBand.ReadAsArray(colstep * blockSize, rowstep * blockSize, colpafNum, rowpafNum)
        for i in range(domSrcDS.RasterCount):
            band = domSrcDS.GetRasterBand(i + 1)
            domSrcNoData = band.GetNoDataValue()
            tempArray = band.ReadAsArray(colstep * blockSize, rowstep * blockSize, colpafNum, rowpafNum)
            mskArray = np.where((mskArray == 0) & (((tempArray <= kwargs['colors'] + kwargs['nearDist']) &
                                                     (tempArray >= kwargs['colors'] - kwargs['nearDist'])) |
                                                   (tempArray == domSrcNoData)), 0, 255)
            band = None
        mskBand.WriteArray(mskArray, colstep * blockSize, rowstep * blockSize)
gdal.SieveFilter(srcBand=mskBand, maskBand=None, dstBand=mskBand, threshold=(1024))

#if delNum != 0:
unit = abs(GeoTransform[5])
mskLessDS = imgdriver.Create(dstFilename.replace('.' + kwargs['ext'], '_N.img'), domSrcDS.RasterXSize,
                          domSrcDS.RasterYSize,1, gdal.GDT_Byte, options=['COMPRESS=RLE'])

mskLessDS.SetGeoTransform(GeoTransform)
mskLessDS.SetProjection(Projection)

#mskLessBand = mskLessDS.GetRasterBand(1)

shpFilename = r'D:\1工作空间\result730\shptest4.shp'
shpFilePart = r'D:\1工作空间\result730\shptest4'

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
    f = None
    f = dst_layer2.GetNextFeature()

[dst_layer2.DeleteFeature(i) for i in delIndexList]
[dst_layer2.DeleteFeature(i) for i in mergeIndexList[1:]]
feat = dst_layer2.GetFeature(mergeIndexList[0])

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
    reducePolyList.append(simplePoly)

poly = unary_union(reducePolyList)

unit = abs(GeoTransform[5])

print(unit)


# 对整体poly进行边缘修正与内扩
poly = poly.buffer(0)
# poly = poly.buffer(distance=kwargs['maxNonBlack'] * unit, cap_style=3, join_style=2).buffer(distance=-(kwargs['maxNonBlack'] * unit), cap_style=3, join_style=2)
poly = poly.buffer(distance=kwargs['maxNonBlack'] * unit, cap_style=2, join_style=1).buffer(distance=-(kwargs['maxNonBlack'] * unit), cap_style=2, join_style=2)
# poly = poly.buffer(0, cap_style=3, join_style=2)
if delNum != 0:
    poly = poly.buffer(distance=-(delNum * unit), cap_style=2, join_style=2)


# 消除内部冗余几何形态
finalPolyList = []
if poly.geom_type == 'Polygon':
    poly = Polygon(poly.exterior)
else:
    for p in poly:
        maxExt = p.exterior
        subPoly = Polygon(maxExt)
        finalPolyList.append(subPoly)
    poly = unary_union(finalPolyList)


geobf = ogr.CreateGeometryFromWkb(poly.wkb)

feat.SetGeometry(geobf)
dst_layer2.SetFeature(feat)
dst_ds = None

gdal.Rasterize(mskLessDS, shpFilename, attribute='status')

# 如果注释这里，则最终使用阈值法
mskBand = None