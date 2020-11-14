# -*- coding:utf-8 -*-

from osgeo import gdal
import os
import multiprocessing as mp
from PySide2 import QtCore
from logger.logRcd import logRcd
import numpy as np
import shutil

valueRange = 255
valueDist = 10

if __name__ == '__main__':
    driver = gdal.GetDriverByName('HFA')
    domSrcDS = gdal.Open(r'E:\20180401中文\data\多波段异常值\H51G082007_P\H51G082007_P.img')

    maskDS = driver.Create(r'E:\20180401中文\data\dataLab\mask.img', domSrcDS.RasterXSize, domSrcDS.RasterYSize,
                             1, gdal.GDT_Byte, options=['COMPRESS=RLE'])

    domDstDS = driver.Create(r'E:\20180401中文\data\dataLab\H51G082007_P.img', domSrcDS.RasterXSize, domSrcDS.RasterYSize,
                           domSrcDS.RasterCount, gdal.GDT_Byte, options=['COMPRESS=RLE'])

    GeoTransform = domSrcDS.GetGeoTransform()
    Projection = domSrcDS.GetProjection()

    maskDS.SetGeoTransform(GeoTransform)
    maskDS.SetProjection(Projection)
    domDstDS.SetGeoTransform(GeoTransform)
    domDstDS.SetProjection(Projection)

    rowNum = domSrcDS.RasterYSize
    columnNum = domSrcDS.RasterXSize

    rowblockNum = int((rowNum - 1) / 4096) + 1
    colblockNum = int((columnNum - 1) / 4096) + 1

    maskBand = maskDS.GetRasterBand(1)

    for rowstep in range(rowblockNum):
        for colstep in range(colblockNum):
            rowpafNum = 4096
            colpafNum = 4096
            if (rowstep == rowblockNum - 1):
                rowpafNum = int((rowNum - 1) % 4096) + 1
            if (colstep == colblockNum - 1):
                colpafNum = int((columnNum - 1) % 4096) + 1
            maskArray = np.ones((rowpafNum,colpafNum)) * 255
            for i in range(domSrcDS.RasterCount):
                band = domSrcDS.GetRasterBand(i + 1)
                tempArray = band.ReadAsArray(colstep * 4096, rowstep * 4096, colpafNum, rowpafNum)
                maskArray = np.where((maskArray == 0) | ((tempArray <= valueRange + valueDist) &
                        (tempArray >= valueRange - valueDist)), 0, 255)
                band = None
            maskBand.WriteArray(maskArray,colstep*4096,rowstep*4096)

    gdal.SieveFilter(srcBand = maskBand, maskBand = None, dstBand = maskBand, threshold = 1000)
    maskDS = None
    maskDS = gdal.Open(r'E:\20180401中文\data\dataLab\mask.img', gdal.GA_Update)
    maskBand = maskDS.GetRasterBand(1)

    for rowstep in range(rowblockNum):
        for colstep in range(colblockNum):
            rowpafNum = 4096
            colpafNum = 4096
            if (rowstep == rowblockNum - 1):
                rowpafNum = int((rowNum - 1) % 4096) + 1
            if (colstep == colblockNum - 1):
                colpafNum = int((columnNum - 1) % 4096) + 1
            maskarray = maskBand.ReadAsArray(colstep * 4096, rowstep * 4096, colpafNum, rowpafNum)
            for i in range(domSrcDS.RasterCount):
                srcband = domSrcDS.GetRasterBand(i + 1)
                dstband = domDstDS.GetRasterBand(i + 1)
                dstband.SetNoDataValue(255)
                temparray = srcband.ReadAsArray(colstep * 4096, rowstep * 4096, colpafNum, rowpafNum)
                temparray = np.where(temparray == 255, 254, temparray)
                temp = np.where(maskarray == 0, 255, temparray)
                dstband.WriteArray(temp, colstep * 4096, rowstep * 4096)
                srcband = None
                dstband = None

    domSrcDS = None
    domDstDS = None


