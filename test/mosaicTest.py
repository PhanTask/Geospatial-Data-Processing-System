import gdal
import ogr
import os
import numpy as np

if __name__ == "__main__":
    srcFilename = r"D:\Documents\Tencent Files\344042096\FileRecv\dem_cs\dem_cs.img"
    slopeFilename = r"D:\Documents\Tencent Files\344042096\FileRecv\dem_cs\slope\dem_cs_slope.img"
    aspectFilename = r"D:\Documents\Tencent Files\344042096\FileRecv\dem_cs\aspect\dem_cs_aspect.img"
    resultFilename = r"D:\Documents\Tencent Files\344042096\FileRecv\dem_cs\result\dem_cs_result.img"
    resultShpname = r"D:\Documents\Tencent Files\344042096\FileRecv\dem_cs\result\dem_cs_result.shp"

    driver = gdal.GetDriverByName('HFA')

    demSrcDS = gdal.Open(srcFilename)

    # demSlopeDS = driver.Create(slopeFilename, demSrcDS.RasterXSize, demSrcDS.RasterYSize,
    #                          demSrcDS.RasterCount, gdal.GDT_Byte, options=['COMPRESS=RLE'])
    #
    demResultDS = driver.Create(resultFilename, demSrcDS.RasterXSize, demSrcDS.RasterYSize,
                              demSrcDS.RasterCount, gdal.GDT_Byte, options=['COMPRESS=RLE'])

    GeoTransform = demSrcDS.GetGeoTransform()
    Projection = demSrcDS.GetProjection()

    demResultDS.SetGeoTransform(GeoTransform)
    demResultDS.SetProjection(Projection)
    #
    # demAspectDS.SetGeoTransform(GeoTransform)
    # demAspectDS.SetProjection(Projection)

    demSlopeDS = gdal.DEMProcessing(slopeFilename, srcFilename, "slope", computeEdges=True)
    demAspectDS = gdal.DEMProcessing(aspectFilename, srcFilename, "aspect", computeEdges=True)

    rowNum = demSrcDS.RasterYSize
    columnNum = demSrcDS.RasterXSize

    rowblockNum = int((rowNum - 1) / 1024) + 1
    colblockNum = int((columnNum - 1) / 1024) + 1

    valueRange = (20,8000)
    slopeThreshold = 80

    srcBand = demSrcDS.GetRasterBand(1)
    slopeBand = demSlopeDS.GetRasterBand(1)
    aspectBand = demAspectDS.GetRasterBand(1)
    resultBand = demResultDS.GetRasterBand(1)

    srcNoDataValue = srcBand.GetNoDataValue()

    for rowstep in range(rowblockNum):
        for colstep in range(colblockNum):
            rowpafNum = 1024
            colpafNum = 1024
            if (rowstep == rowblockNum - 1):
                rowpafNum = int((rowNum - 1) % 1024) + 1
            if (colstep == colblockNum - 1):
                colpafNum = int((columnNum - 1) % 1024) + 1

            srcArray = srcBand.ReadAsArray(colstep * 1024, rowstep * 1024, colpafNum, rowpafNum)
            slopeArray = slopeBand.ReadAsArray(colstep * 1024, rowstep * 1024, colpafNum, rowpafNum)
            aspectArray = aspectBand.ReadAsArray(colstep * 1024, rowstep * 1024, colpafNum, rowpafNum)

            aspectTemp = np.where(((aspectArray >= 0) & (aspectArray <= 1))|
                            ((aspectArray >= 89) & (aspectArray <= 91))|
                            ((aspectArray >= 179) & (aspectArray <= 181))|
                            ((aspectArray >= 269) & (aspectArray <= 271))|
                            ((aspectArray >= 359) & (aspectArray <= 360))
                            ,0,255)

            ssTemp = np.where((srcArray == srcNoDataValue) |
                              ((srcArray <= valueRange[0]) & (srcArray >= valueRange[1])) |
                              (slopeArray >= slopeThreshold)
                              ,0,255)

            aspectBand.WriteArray(aspectTemp ,colstep * 1024, rowstep * 1024)
            resultBand.WriteArray(ssTemp ,colstep * 1024, rowstep * 1024)

    gdal.SieveFilter(srcBand=aspectBand, maskBand=None, dstBand=aspectBand, threshold=(512))
    for rowstep in range(rowblockNum):
        for colstep in range(colblockNum):
            rowpafNum = 1024
            colpafNum = 1024
            if (rowstep == rowblockNum - 1):
                rowpafNum = int((rowNum - 1) % 1024) + 1
            if (colstep == colblockNum - 1):
                colpafNum = int((columnNum - 1) % 1024) + 1

            resultArray = resultBand.ReadAsArray(colstep * 1024, rowstep * 1024, colpafNum, rowpafNum)
            aspectArray = aspectBand.ReadAsArray(colstep * 1024, rowstep * 1024, colpafNum, rowpafNum)
            resultTemp = np.where(aspectArray == 0, 0, resultArray)
            resultBand.WriteArray(resultTemp, colstep * 1024, rowstep * 1024)

    dstLayername = "POLYGONIZED"
    drv = ogr.GetDriverByName("ESRI Shapefile")
    dst_ds = drv.CreateDataSource(resultShpname)
    dst_layer = dst_ds.CreateLayer(dstLayername, srs=None)

    fd = ogr.FieldDefn("Status", ogr.OFTInteger)
    dst_layer.CreateField(fd)
    dst_field = dst_layer.FindFieldIndex("Status", 1)

    gdal.Polygonize(resultBand, None, dst_layer, dst_field, [], callback=None)

    dst_ds = None
    demSrcDS = None
    demResultDS = None
    demSlopeDS = None
    demAspectDS = None