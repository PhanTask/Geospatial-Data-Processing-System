#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 21:13
# @Author  : Dutian
# @Site    : 
# @File    : xFileReadImp.py
# @Software: PyCharm
# @license : Copyright(C), Dutian
# @Contact : free.du@qq.com
import  os
import pygeodesy
from osgeo import ogr
from pygeodesy.ellipsoidalVincenty import LatLon
from PySide2 import QtCore
from logger.logRcd import logRcd

class xFileTextureCheck(QtCore.QThread):
    '''
    贴图完整性检查
    '''
    doneflag  = QtCore.Signal(bool) # 是否成功完成
    modelTableItemDataSignal = QtCore.Signal(object)  # model表格项signal
    dostop = False  # 是否强制终止
    def __init__(self,inputFilePath,textureFolder):
        """
        输入.x文件，以txt格式进行读取，按照文件规范逐行读取，得到坐标信息、贴图名称等信息。
        :param inputFilePath:  输入文件路径
        """
        super(xFileTextureCheck, self).__init__()

        self.inputFilePath=inputFilePath
        self.textureFolder=textureFolder
        self.FrameList=[]

        self.logRcd = logRcd('贴图完整性检查')
        self.textureNum=0       #已处理贴图数
        self.textureCount =0 #贴图总数
        # 自定义信号发射函数
        # 任务完成信号
    def emitFinish(self, isSuccessful):
        self.doneflag.emit(isSuccessful)

    # 结果传输到列表信号
    def emitModelTableItemData(self, ModelTableItemData):
        self.modelTableItemDataSignal.emit(ModelTableItemData)

    def run(self):
        """
        程序执行函数
        :return:
        """

        lineList = []
        textureFilenameList = []
        isReadMaterial = False
        isReadMeshMaterialList = False
        isReadFrame = False
        isReadMesh = False
        isFirstLoad = True
        isFirstLoadMeshXY = True
        materialReadList = []  # 读写Frame时存储的list'
        materialDicList = []  # 第一次读取存储在字典的list
        frameDicList = []

        domTableItemDataList=[] #存储输出的缺失的贴图名称、3D模型名称以及文件路径
        signalProcess=''    #存储输出过程的中间日志
        materialDic = {'mName': '',
                       'textureFilename': textureFilenameList
                       }

        frameDic = {'frameName': '',
                    'lon': '',
                    'lat': '',
                    'meshName': '',
                    'minX': '',
                    'minY': '',
                    'maxX': '',
                    'maxY': '',
                    'materialList': materialReadList

                    }
        file_object = open(self.inputFilePath, 'rU')
        signalProcess='已打开文件'+self.inputFilePath+'\n'
        print(signalProcess)
        try:

            lineList = file_object.readlines()
            signalProcess = signalProcess+ '正在读取X文件' +'\n'
            for index in range(len(lineList) - 2):  # 少读末尾，用来标记判断文件尾
                tempLine = lineList[index].strip().rstrip("\n")
                tempLineNext = lineList[index + 1].strip().rstrip("\n")
                if tempLine[:8] == "Material":
                    if materialDic['mName'] != '' and isReadMaterial:
                        materialDic['textureFilename'] = textureFilenameList
                        materialDicList.append(materialDic)
                        materialDic = {}
                        textureFilenameList = []
                        isReadMaterial = False
                    materialList = lineList[index].split(" ")
                    materialDic['mName'] = materialList[1]
                    isReadMaterial = True
                if isReadMaterial and tempLine.find("TextureFilename") >= 0:
                    textureFilenameList.append(tempLineNext.split("\"")[1])

                if tempLine[:7] == "Frame _":
                    if isFirstLoad:
                        materialDic['textureFilename'] = textureFilenameList

                        materialDicList.append(materialDic)
                        materialDic = {}
                        textureFilenameList = []
                        isReadMaterial = False

                        isFirstLoad = False

                    frameDic['frameName'] = tempLine.split(' ')[1]
                    isReadFrame = True

                if isReadFrame and tempLine.find("FrameTransformMatrix") >= 0:
                    frameTransformMatrixList = tempLineNext.split(",")
                    frameDic['lon'] = frameTransformMatrixList[12]
                    frameDic['lat'] = frameTransformMatrixList[14]
                if isReadFrame and tempLine.find("Mesh _") >= 0:
                    frameDic['meshName'] = tempLine.split(' ')[1][1:]
                    isReadMesh = True
                if isReadFrame and isReadMesh:

                    if len(tempLine.split(";")) > 2:
                        if len(tempLineNext.split(";")) <= 2: isReadMesh = False
                        tempX = float(tempLine.split(";")[0])
                        tempY = float(tempLine.split(";")[2])
                        if isFirstLoadMeshXY:
                            meshMinX = tempX
                            meshMaxX = tempX
                            meshMinY = tempY
                            meshMaxY = tempY
                            isFirstLoadMeshXY = False
                        else:
                            if tempX > meshMaxX: meshMaxX = tempX
                            if tempX < meshMinX: meshMinX = tempX
                            if tempY > meshMaxY: meshMaxY = tempY
                            if tempY < meshMinY: meshMinY = tempY
                        frameDic['maxY'] = meshMaxY
                        frameDic['maxX'] = meshMaxX
                        frameDic['minX'] = meshMinX
                        frameDic['minY'] = meshMinY

                        if len(tempLineNext.split(";")) < 2: isReadMesh = False
                if isReadFrame and tempLine.find("MeshMaterialList") >= 0:
                    isReadMeshMaterialList = True
                    materialReadList = []
                if isReadFrame and isReadMeshMaterialList:
                    if tempLine[0] == '{' and tempLine[-1] == '}':
                        materialName = tempLine.split(" ")[1]
                        for i in materialDicList:
                            if i['mName'] == materialName:
                                materialReadList.extend(i['textureFilename'])
                                break
                    if tempLineNext == '}':
                        isReadMeshMaterialList = False
                        isFirstLoadMeshXY = True
                        frameDic['materialList'] = materialReadList
                        tempFrame = FrameOfX(kwargs=frameDic)
                        frameDicList.append(tempFrame)
            signalProcess = signalProcess + '.X文件读取完毕，正在检查贴图文件' + '\n'
            print(frameDicList)

            self.logRcd.emitInfo(signalProcess)
            # 检查完整性执行函数
            self.modelTableItemDataSignal.emit(self.textureCheck(materialDicList))

            signalProcess = signalProcess + '贴图检查完毕' + '\n'


            self.logRcd.emitProcessValue(100)
            self.logRcd.emitInfo('[INFO] 检查完成')
            self.logRcd.logFileClose()

            print(materialDicList)
        finally:
            file_object.close()

    def textureCheck(self,materialDicList):
        tempLackTextureNameList=[]
        for tempMaterialDic in materialDicList:
            self.textureCount=len(materialDicList)
            for tempTexture in tempMaterialDic['textureFilename']:
                if not os.path.exists(self.textureFolder +'\\' + tempTexture):
                    tempLackTextureNameList.append((tempTexture,'缺失',
                                                    tempMaterialDic['mName'],
                                                    self.inputFilePath, self.textureFolder))
                    print(tempTexture)
                else:
                    tempLackTextureNameList.append((tempTexture, '完整',
                                                    tempMaterialDic['mName'],
                                                    self.inputFilePath, self.textureFolder))
                # 设置进度栏
                self.textureNum += 1
                # 进度栏显示
                self.logRcd.emitInfo('[INFO] ' + '(' + self.textureNum.__str__() +
                                     '/' + self.textureCount.__str__() + ')\n'
                                     )
                self.logRcd.emitInfo(tempTexture +"  已检查" + '\n')
                self.logRcd.emitProcessValue(int(100.0 * self.textureNum / self.textureCount))

        return tempLackTextureNameList



class FrameOfX():
    def __init__(self, kwargs):
        self.frameName=kwargs['frameName']
        self.lon=kwargs['lon']
        self.lat=kwargs['lat']
        self.meshName=kwargs['meshName']
        self.maxX=kwargs['maxX']
        self.maxY = kwargs['maxY']
        self.minX = kwargs['minX']
        self.minY = kwargs['minY']

        self.materialList=kwargs['materialList']

def pointToPolygon(outLayer,destLBPoint,destRTPoint,fieldDic,*args):
    '''

    :param outLayer: 输出的图层
    :param destLBPoint: 输入的左下角定点坐标
    :param destRTPoint: 输入的右上角坐标
    :param fieldDic:    属性表的字段名称和值
    :param args: 其他补充值
    :return:
    '''
    fieldName = fieldDic['fieldName']
    fieldValue = fieldDic['fieldValue']

    ring1 = ogr.Geometry(ogr.wkbLinearRing)



    ring1.AddPoint(destLBPoint[1], destLBPoint[0])
    ring1.AddPoint(destLBPoint[1], destRTPoint[0])
    ring1.AddPoint(destRTPoint[1], destRTPoint[0])
    ring1.AddPoint(destRTPoint[1], destLBPoint[0])
    ring1.AddPoint(destLBPoint[1], destLBPoint[0])

    poly1 = ogr.Geometry(ogr.wkbPolygon)
    poly1.AddGeometry(ring1)


    outFeature = ogr.Feature(outLayer.GetLayerDefn())
    outFeature.SetGeometry(poly1)

    outFeature.SetField(fieldName, fieldValue)
    outLayer.CreateFeature(outFeature)

    outFeature.Destroy()
def disPrjCalculatePointToEnvelope(pointLat,pointLon,envelopeTuple):
    '''
    计算给定点到四至中心点的距离，用到投影坐标系CGCS2000
    :param pointLat: 输入待测点纬度
    :param pointLon: 输入待测点经度
    :param envelopeTuple: 四至的元祖，前两个为经度，后两个为纬度，从小到大排序
    :return: 投影后计算的距离
    '''
    centerEnvelopePrj = LatLon(pointLat,
                               pointLon,
                               datum=pygeodesy.datum.Datums.CGCS2000)
    geom3DEnvelopCenPrj = LatLon((envelopeTuple[2] + envelopeTuple[3]) / 2, \
                                 (envelopeTuple[0] + envelopeTuple[1]) / 2, \
                                 datum=pygeodesy.datum.Datums.CGCS2000)

    deviationValue = centerEnvelopePrj.distanceTo(geom3DEnvelopCenPrj)
    return deviationValue

if  __name__ == '__main__':
    inputFilePath = r'C:\Users\Administrator\Desktop\数据质检\数据文件\三维\testAll709.X'
    textureFolder=r'C:\Users\Administrator\Desktop\数据质检\数据文件\三维\10\texture - 副本'
    test=xFileTextureCheck(inputFilePath,textureFolder)
    test.run()