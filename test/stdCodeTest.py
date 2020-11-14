#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 10:46
# @Author  : Dutian
# @Site    :
# @File    : codeConsistCheckImp.py
# @Software: PyCharm
# @license : Copyright(C), Dutian
# @Contact : free.du@qq.com
from osgeo import ogr
import multiprocessing as mp

if __name__ == '__main__':
    gdbDir = r'E:\武大质检程序样例数据\专题数据程序需求\1政务报送数据下载_已发布GUID.gdb'
    driver = ogr.GetDriverByName('FileGDB')
    allFeatureList=[] #所有要素特定字段集合
    oFeatureList=[] # 三个值，[0]为要素名称，[1]为要素编码,[2]所在图层名称
    gdbFile = driver.Open(gdbDir, 0)

    nameSet = set()
    nameAndCodeSet = set()
    featDifferCounterDict = {} #各要素的编码种类的数量，若为1则该要素再各个图层中出现的编码都是一致的，大于1则存在不一致的情况
    resultDict = {}

    # 读取所有要素属性信息
    for oLayer in gdbFile:
        layerName = oLayer.GetName()
        for oFeature in oLayer:
            featName = oFeature.GetField('name')
            if featName not in nameSet:
                featCode = oFeature.GetField('uuid')
                nameSet.add(featName)
                nameAndCodeSet.add(featName + '/' + featCode)
                featDifferCounterDict[featName] = 1
                resultDict[featName] = []
                basicItem = {'name': featName,
                                 'code': featCode,
                                 'layerName': layerName,
                                 'gdbDir': gdbDir
                                 }
                resultDict[featName].append(basicItem)
            else:
                featCode = oFeature.GetField('uuid')
                featNameAndCode = featName + '/' + featCode
                if featNameAndCode not in nameAndCodeSet: #相同名称要素编码不一致，通常是第一次检查到不一致的情况
                    nameAndCodeSet.add(featNameAndCode)
                    featDifferCounterDict[featName] += 1
                    unconsistItem = {'name': featName,
                                     'code': featCode,
                                     'layerName': layerName,
                                     'gdbDir':gdbDir
                                     }
                    resultDict[featName].append(unconsistItem)
                else: #存在相同名称要素编码一致的情况，但可能只是与部分要素的编码一致，整体还可能不一致
                    if featDifferCounterDict[featName] > 1: #若要素数量大于1，说明该要素编码本身就存在多个不一致情况，仍判作不一致
                        unconsistItem = {'name': featName,
                                         'code': featCode,
                                         'layerName': layerName,
                                         'gdbDir': gdbDir
                                         }
                        resultDict[featName].append(unconsistItem)
                    else: #遇到了相同名称要素编码完全一致的理想情况，检查合格
                        pass

            # oFeatureList = []
            # oFeatureList.append(oFeature.GetField(oLayerDic['fName']))
            # oFeatureList.append(oFeature.GetField(oLayerDic['featureCode']))
            # oFeatureList.append(oLayer.GetName())
            # allFeatureList.append(oFeatureList)

    # gdbFile.Release()
    # gdbFile1 = driver.Open(gdbDir, 1)
    # #    二次遍历，查找
    # stdPool = mp.Pool(mp.cpu_count())
    # for oLayer in gdbFile1:
    #     oLayerName = oLayer.GetName()
    #     for oFeature in oLayer:
    #         oFeatureName=oFeature.GetField(oLayerDic['fName'])
    #         oFeatureCode=oFeature.GetField(oLayerDic['featureCode'])
    #
    #         for compareFeList in allFeatureList:
    #             if oFeatureName==compareFeList[0] \
    #                 and oFeatureCode!=compareFeList[1]:
    #                 print(oLayerName+'_'+oFeatureName+oFeatureCode \
    #                         +'     '+ compareFeList[1]+'_'+compareFeList[2])
    #     print('已查找  '+oLayer.GetName())
    # stdPool.close()  # 关闭进程池
    # stdPool.join()  # 等待开辟的所有进程执行完后，主进程才继续往下执行
    for item in resultDict:
        if resultDict[item].__len__() == 1:
            continue
        print('--------------------')
        print(item + ' | ' + resultDict[item].__len__().__str__() + '个')
        print(resultDict[item])