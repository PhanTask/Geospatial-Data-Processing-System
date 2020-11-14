import ogr
import gdal
import os
import numpy as np
import math


if __name__ == '__main__':

    # my result
    # firstDSmy = gdal.Open(r'D:\1工作空间\数字正射影像DOM\3025-40493_P\3025-40493_P.img')
    # firstDSmy = gdal.Open(r'D:\1工作空间\数字正射影像DOM\H51G082007_C\H51G082007_C.img')
    # firstDSmy = gdal.Open(r'D:\1工作空间\数字正射影像DOM\rotatethreshold\H51G04501611\H51G04501611.img')
    # firstDSmy = gdal.Open(r'D:\1工作空间\数字正射影像DOM\H51G030014_P\H51G030014_P.img')

    # th result
    # firstDSmy = gdal.Open(r'D:\1工作空间\数字正射影像DOM\threshold0014\3025-40493_P\3025-40493_P.img')
    # firstDSmy = gdal.Open(r'D:\1工作空间\数字正射影像DOM\clipthreshold\H51G082007_C\H51G082007_C.img')
    # same same
    # firstDSmy = gdal.Open(r'D:\1工作空间\数字正射影像DOM\threshold0014\H51G030014_P\H51G030014_P.img')

    # scan result
    # firstDSmy = gdal.Open(r'D:\1工作空间\数字正射影像DOM\nearblack0014\3025-40493_P\3025-40493_P.img')
    # firstDSmy = gdal.Open(r'D:\1工作空间\数字正射影像DOM\clipnearblack\H51G082007_C\H51G082007_C.img')
    # same same
    # firstDSmy = gdal.Open(r'D:\1工作空间\数字正射影像DOM\nearblack0014\H51G030014_P\H51G030014_P.img')

    # original result
    # firstDSmy = gdal.Open(r'D:\1工作空间\数字正射影像DOM\to饶\3025-40493_P\3025-40493_P.img')
    # firstDSmy = gdal.Open(r'D:\1工作空间\数字正射影像DOM\clip\H51G082007_C\H51G082007_C.img')
    # same same
    firstDSmy = gdal.Open(r'D:\1工作空间\数字正射影像DOM\to饶\H51G030014_P\H51G030014_P.img')

    # firstDSmy = gdal.Open(r'D:\1工作空间\数字正射影像DOM\threshold0014\3025-40493_P\3025-40493_P.img')  # 多波段
    # secondDSmy = gdal.Open(r'E:\20180401中文\data\dataLab\H51G030014\H51G030014.img.msk') # 多波段
    # thirdDSmy = gdal.Open(r'E:\20180401中文\data\dataLab\H51G030014\H51G030014.img.msk') # 单波段
    # fourthDSmy = gdal.Open(r'E:\20180401中文\data\dataLab\H51G030014\H51G030014.img.msk') # 多波段
    #
    # firstDSnb = gdal.Open(r'E:\20180401中文\data\dataLab\H51G030014\H51G030014.img.msk') # 多波段
    # secondDSnb = gdal.Open(r'E:\20180401中文\data\dataLab\H51G030014\H51G030014.img.msk') # 多波段
    # thirdDSnb = gdal.Open(r'E:\20180401中文\data\dataLab\H51G030014\H51G030014.img.msk') # 单波段
    # fourthDSnb = gdal.Open(r'E:\20180401中文\data\dataLab\H51G030014\H51G030014.img.msk') # 多波段
    #
    # firstDSth = gdal.Open(r'E:\20180401中文\data\dataLab\H51G030014\H51G030014.img.msk') # 多波段
    # secondDSth = gdal.Open(r'E:\20180401中文\data\dataLab\H51G030014\H51G030014.img.msk') # 多波段
    # thirdDSth = gdal.Open(r'E:\20180401中文\data\dataLab\H51G030014\H51G030014.img.msk') # 单波段
    # fourthDSth = gdal.Open(r'E:\20180401中文\data\dataLab\H51G030014\H51G030014.img.msk') # 多波段

    firstDSmyEntropy = 0.0
    # secondDSmyEntropy = 0.0
    # thirdDSmyEntropy = 0.0
    # fourthDSmyEntropy = 0.0
    # firstDSnbEntropy = 0.0
    # secondDSnbEntropy = 0.0
    # thirdDSnbEntropy = 0.0
    # fourthDSnbEntropy = 0.0
    # firstDSthEntropy = 0.0
    # secondDSthEntropy = 0.0
    # thirdDSthEntropy = 0.0
    # fourthDSthEntropy = 0.0

    rowNum = firstDSmy.RasterYSize
    columnNum = firstDSmy.RasterXSize
    for i in range(firstDSmy.RasterCount):
        iBand = firstDSmy.GetRasterBand(i+1)
        iBandList = iBand.GetHistogram(-0.5, 255.5, buckets=256, include_out_of_range=0, approx_ok=0)
        validNumber = float(sum(iBandList))
        # print(rowNum * columnNum)
        # print(validNumber)
        # print(iBandList[255])
        for j in range(256):
            if iBandList[j] != 0:
                firstDSmyEntropy += (iBandList[j] / validNumber) * math.log2(iBandList[j] / validNumber)
            else:
                continue
    firstDSmyEntropy /= (-1 * firstDSmy.RasterCount)

    print(firstDSmyEntropy)
