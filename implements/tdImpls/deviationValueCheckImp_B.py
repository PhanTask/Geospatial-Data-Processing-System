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
from PySide2 import QtCore

import pygeodesy
from osgeo import ogr
from pygeodesy.ellipsoidalVincenty import LatLon
from logger.logRcd import logRcd

class devValueCheck(QtCore.QThread):
    '''
    三维模型偏移值检查模块
    '''
    doneflag  = QtCore.Signal(bool) # 是否成功完成
    modelTableItemDataSignal = QtCore.Signal(object)  # model表格项signal
    dostop = False  # 是否强制终止
    def __init__(self,inputFilePath,referShpFilePath,outputFilePath):
        """
        输入.x文件，以txt格式进行读取，按照文件规范逐行读取，得到坐标信息、贴图名称等信息。
        :param inputFilePath:  输入文件路径
        """

        super(devValueCheck, self).__init__()
        self.inputFilePath=inputFilePath
        self.referShpFilePath=referShpFilePath
        self.outputFilePath=outputFilePath
        self.FrameList=[]


        self.inputFilePath = inputFilePath

        self.FrameList = []

        self.logRcd = logRcd('模型偏移检查')
        self.model3DNum = 0  # 已处理模型数
        self.model3DCount = 0  # 模型总数


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
        centerEnvelopeList=[]
        fieldDic={

        }
        domTableItemDataList = []  # 存储输出的表格数据。包括：3D模型名称、偏差值、匹配要素ID、输出shp路径、参照数据路径、输入路径

        signalProcess = ''  # 存储输出过程的中间日志
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
        signalProcess = '已打开文件  ' + self.inputFilePath
        self.logRcd.emitInfo(signalProcess)
        print(signalProcess)

        try:
            lineList = file_object.readlines()
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
                # if isReadFrame and isReadMeshMaterialList and tempLine=="}" and tempLineNext=='}':

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
                        # tempFrame = FrameOfX(frameName=frameDic['fram         eName'],
                        #                      location=frameDic['location'],
                        #                      meshName=frameDic['meshName'],
                        #                      mbr=frameDic['mbr'],
                        #                      materialList=frameDic['materialList']
                        #                      )
                        tempFrame = FrameOfX(kwargs=frameDic)
                        frameDicList.append(tempFrame)
            # 发送信号
            signalProcess = 'X文件读取完成  ' + self.inputFilePath
            self.logRcd.emitInfo(signalProcess)
            print(frameDicList)
            print(materialDicList)

            # 根据解析结果frameDicList生成最小外接矩形shp文件
            #outputShapePath = r'C:\Users\Administrator\Desktop\数据质检\数据文件\三维\outPutX.shp'
            driver = ogr.GetDriverByName('ESRI Shapefile')

            if os.path.exists(self.outputFilePath):
                driver.DeleteDataSource(self.outputFilePath)
            outPutDataSource = driver.CreateDataSource(self.outputFilePath)
            outLayer = outPutDataSource.CreateLayer(self.outputFilePath, geom_type=ogr.wkbMultiPolygon)
            # 发送信号
            signalProcess = '正在创建模型外接矩形 面数据  ' + self.outputFilePath
            self.logRcd.emitInfo(signalProcess)

            fieldName = 'ID'
            fieldType = ogr.OFTString

            idField = ogr.FieldDefn(fieldName, fieldType)
            outLayer.CreateField(idField)

            for tempFrameDic in frameDicList:
                tempInitPointLanlon = pygeodesy.ellipsoidalNvector.LatLon(float(tempFrameDic.lat),
                                                                          float(tempFrameDic.lon))
                tempInitPointLanlon.datum == pygeodesy.datum.Datums.CGCS2000
                destLBPoint = tempInitPointLanlon.destinationNed(
                    pygeodesy.ellipsoidalNvector.Ned(float(tempFrameDic.minY), float(tempFrameDic.minX), 0))
                destRTPoint = tempInitPointLanlon.destinationNed(
                    pygeodesy.ellipsoidalNvector.Ned(float(tempFrameDic.maxY), float(tempFrameDic.maxX), 0))
                tempFrameDic.destLBPoint = destLBPoint
                tempFrameDic.destRTPoint = destRTPoint

                # lonDe = destRTPoint.latlon[1] - destLBPoint.latlon[1]
                # latDe = destRTPoint.latlon[0] - destLBPoint.latlon[0]

                fieldDic['fieldName'] = 'ID'
                fieldDic['fieldValue'] = tempFrameDic.frameName

                pointToPolygon(outLayer, destLBPoint.latlon, destRTPoint.latlon, fieldDic)
            outPutDataSource.Destroy()

            # 发送信号
            signalProcess = '3D模型外接矩形 面数据 创建完成  ' + self.outputFilePath
            self.logRcd.emitInfo(signalProcess)

            # 计算给定面要素的最小外界矩形MBR,并计算中心dian坐标
            inputPolygonPath = self.referShpFilePath
            inputPolygonSource = driver.Open(inputPolygonPath)
            layer = inputPolygonSource.GetLayer(0)

            # 发送信号
            signalProcess = '正在进行3D模型偏移值计算  ' +'\n'+\
                            '参照数据源：'+ self.referShpFilePath

            self.logRcd.emitInfo(signalProcess)


            tempPolyFeature = layer.GetNextFeature()
            while tempPolyFeature is not None:
                geom = tempPolyFeature.GetGeometryRef()
                envelope = geom.GetEnvelope()
                tempCenterLon = (envelope[0] + envelope[1]) / 2
                tempCenterLat = (envelope[2] + envelope[3]) / 2

                centerEnvelopeList.append({'centerLon': tempCenterLon,
                                           'centerLat': tempCenterLat,
                                           'FCODE': tempPolyFeature.GetField('FCODE'),
                                           'OBJECTID': tempPolyFeature.GetField('OBJECTID'),
                                           'geomWkt': geom.ExportToWkt()
                                           })
                tempPolyFeature = None
                geom = None
                tempPolyFeature = layer.GetNextFeature()

            inputPolygonSource.Release()
            # 遍历三维面要素，对res面要素进行匹配
            outPutDataSource = driver.Open(self.outputFilePath, 1)
            outLayer = outPutDataSource.GetLayer(0)
            outLayer.ResetReading()
            # 添加偏差值字段deviationValue
            deviationField = ogr.FieldDefn('devValue', ogr.OFTString)
            deviationField.SetWidth(20)
            outLayer.CreateField(deviationField)
            # 添加匹配字段match3DFcodeField
            match3DFcodeField = ogr.FieldDefn('ma3DFcode', ogr.OFTString)
            match3DFcodeField.SetWidth(20)
            outLayer.CreateField(match3DFcodeField)
            # 添加匹配字段match3DObjectIDField
            match3DObjectIDField = ogr.FieldDefn('ma3DObjID', ogr.OFTString)
            match3DObjectIDField.SetWidth(10)
            outLayer.CreateField(match3DObjectIDField)

            # 发送信号
            signalProcess = '正在进行 3D模型外接矩形 偏移值写入  ' + self.outputFilePath
            self.logRcd.emitInfo(signalProcess)
            self.model3DCount=outLayer.GetFeatureCount()

            temp3Dfeature = outLayer.GetNextFeature()
            while temp3Dfeature is not None:

                deviationValue = 'emptyDv'
                match3DFcode = ''
                match3DOBJECTID = ''
                isFirstFindInclude = True
                geom3D = temp3Dfeature.GetGeometryRef()
                geom3DEnvelop = geom3D.GetEnvelope()
                isIn3DGeomList = []
                for centerEnvelope in centerEnvelopeList:
                    if geom3DEnvelop[0] <= centerEnvelope['centerLon'] <= geom3DEnvelop[1] and geom3DEnvelop[2] <= \
                            centerEnvelope['centerLat'] <= geom3DEnvelop[3]:
                        isIn3DGeomList.append(centerEnvelope)
                        # print(centerEnvelope['OBJECTID'])
                if len(isIn3DGeomList) == 0:
                    deviationValue = 'emptyDv'
                    match3DFcode = ''
                    match3DObjectID = ''

                if len(isIn3DGeomList) == 1:
                    centerEnvelope1 = isIn3DGeomList[0]
                    # centerEnvelopePrj = LatLon(centerEnvelope['centerLat'],\
                    #                            centerEnvelope['centerLon'], \
                    #                             datum =pygeodesy.datum.Datums.CGCS2000)
                    # geom3DEnvelopCenPrj = LatLon((geom3DEnvelop[2]+geom3DEnvelop[3])/2,\
                    #                              (geom3DEnvelop[0]+geom3DEnvelop[1])/2, \
                    #                              datum=pygeodesy.datum.Datums.CGCS2000)

                    # deviationValue=centerEnvelopePrj.distanceTo(geom3DEnvelopCenPrj)
                    deviationValue = disPrjCalculatePointToEnvelope(centerEnvelope1['centerLat'],
                                                                    centerEnvelope1['centerLon'],
                                                                    geom3DEnvelop)
                    match3DFcode = centerEnvelope1['FCODE']
                    match3DOBJECTID = centerEnvelope1['OBJECTID']

                if len(isIn3DGeomList) > 1:  # 求相交面积，并排序取最大
                    # maxIntersectionDic={'maxIntersectionArea':0,
                    #                     'maxIntersectionGeom':None,
                    # }
                    maxIouValue = 0
                    minDis = 0  # 同一面内包含多个3D面要素，只取距离最近的那个
                    maxIntersectionEnvelope = {}
                    geomSameWktList = []
                    geom3DArea = ogr.Geometry.Area(geom3D)
                    for tempCenterEnvelope in isIn3DGeomList:
                        # 利用交并比确定最大值进行匹配
                        geomFromWkt = ogr.CreateGeometryFromWkt(tempCenterEnvelope['geomWkt'])
                        refPolyGeomArea = ogr.Geometry.Area(geomFromWkt)
                        interSectionGeom = geom3D.Intersection(geomFromWkt)
                        interSectionGeomArea = ogr.Geometry.Area(interSectionGeom)
                        iouValue = interSectionGeomArea / (geom3DArea + refPolyGeomArea - interSectionGeomArea)

                        # print(iouValue)
                        if iouValue > maxIouValue:
                            maxIouValue = iouValue
                            maxIntersectionEnvelope = tempCenterEnvelope
                        # if iouValue == maxIouValue == 1:
                        #     maxIouValue = iouValue
                        #     geomFromWktEn = geomFromWkt.GetEnvelope()
                        #     tempMinDis = disPrjCalculatePointToEnvelope((geomFromWktEn[2] + geomFromWktEn[3]) / 2,
                        #                                                 (geomFromWktEn[0] + geomFromWktEn[1]) / 2,
                        #                                                 geom3DEnvelop)
                        #     if isFirstFindInclude :
                        #         minDis=tempMinDis
                        #         maxIntersectionEnvelope = tempCenterEnvelope
                        #         isFirstFindInclude=False
                        #     if (not isFirstFindInclude) and tempMinDis<minDis:
                        #         minDis=tempMinDis
                        #         maxIntersectionEnvelope = tempCenterEnvelope

                        geomFromWkt = None
                        interSectionGeom = None

                    # centerEnvelopePrj = LatLon(centerEnvelope['centerLat'], \
                    #                            centerEnvelope['centerLon'], \
                    #                            datum=pygeodesy.datum.Datums.CGCS2000)
                    # geom3DEnvelopCenPrj = LatLon((geom3DEnvelop[2] + geom3DEnvelop[3]) / 2, \
                    #                              (geom3DEnvelop[0] + geom3DEnvelop[1]) / 2, \
                    #                              datum=pygeodesy.datum.Datums.CGCS2000)
                    # deviationValue = centerEnvelopePrj.distanceTo(geom3DEnvelopCenPrj)
                    # 设置交并比阈值，去除差距太大的项
                    if maxIouValue >= 0.2:
                        deviationValue = disPrjCalculatePointToEnvelope(maxIntersectionEnvelope['centerLat'],
                                                                        maxIntersectionEnvelope['centerLon'],
                                                                        geom3DEnvelop)
                        match3DFcode = maxIntersectionEnvelope['FCODE']
                        match3DOBJECTID = maxIntersectionEnvelope['OBJECTID']
                    else:
                        deviationValue = 'emptyDv'
                        match3DFcode = ''
                        match3DOBJECTID = ''
                    isIn3DGeomList = []

                # 属性表写入
                temp3Dfeature.SetField('devValue', deviationValue)
                temp3Dfeature.SetField('ma3DFcode', match3DFcode)
                temp3Dfeature.SetField('ma3DObjID', match3DOBJECTID)
                outLayer.SetFeature(temp3Dfeature)

                # 向表格发送数据
                ModelTableItemData=(temp3Dfeature.GetField('ID'),
                                  match3DOBJECTID.__str__(),
                                  deviationValue.__str__(),
                                  self.inputFilePath,
                                  self.referShpFilePath,
                                  self.outputFilePath,
                                  )
                self.modelTableItemDataSignal.emit(ModelTableItemData)

                # 设置进度栏
                self.model3DNum += 1
                # 进度栏显示
                self.logRcd.emitInfo('[INFO] ' + '(' + self.model3DNum.__str__() +
                                     '/' + self.model3DCount.__str__() + ')\n'
                                     )
                self.logRcd.emitInfo(temp3Dfeature.GetField('ID') + "  已检查" + '\n')
                self.logRcd.emitProcessValue(int(100.0 * self.model3DNum / self.model3DCount))

                geom3D = None
                # 读取下一个
                temp3Dfeature = outLayer.GetNextFeature()
            #销毁数据源并更新

            # 发送信号
            signalProcess = '3D模型外接矩形 偏移值写入完成  ' + self.outputFilePath
            self.logRcd.emitInfo(signalProcess)
            outPutDataSource.Destroy()
            print(frameDicList)


        finally:
            file_object.close()


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

        # self.destLBPoint=kwargs['destLBPoint']
        # self.destRTPoint=kwargs['destRTPoint']

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

    # multipolygon1 = ogr.Geometry(ogr.wkbMultiPolygon)
    # multipolygon1.AddGeometry(poly1)
    #
    # poly2 = poly1
    # multipolygon1.AddGeometry(poly2)
    #
    #
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
    # inputFilePath=r'C:\Users\Administrator\Desktop\数据质检\数据文件\三维\testAll709.X'
    # lineList = []
    # textureFilenameList = []
    # isReadMaterial = False
    # isReadMeshMaterialList=False
    # isReadFrame=False
    # isReadMesh=False
    # isFirstLoad = True
    # isFirstLoadMeshXY=True
    # materialReadList=[] #读写Frame时存储的list'
    # materialDicList = [] #第一次读取存储在字典的list
    # frameDicList=[]
    # fieldDic={}
    # centerEnvelopeList=[]
    # materialDic = {'mName': '',
    #                'textureFilename': textureFilenameList
    #                }
    #
    # frameDic={'frameName':'',
    #           'lon': '',
    #           'lat': '',
    #           'meshName':'',
    #           'minX':'',
    #           'minY':'',
    #           'maxX':'',
    #           'maxY':'',
    #           'materialList': materialReadList
    #
    # }
    # # 解析.X文件
    # file_object = open(inputFilePath, 'rU')
    # try:
    #     lineList = file_object.readlines()
    #     for index in range(len(lineList) - 2):  #少读末尾，用来标记判断文件尾
    #         tempLine = lineList[index].strip().rstrip("\n")
    #         tempLineNext=lineList[index+1].strip().rstrip("\n")
    #         if tempLine[:8] == "Material":
    #             if materialDic['mName'] != '' and isReadMaterial:
    #                 materialDic['textureFilename'] = textureFilenameList
    #
    #                 materialDicList.append(materialDic)
    #                 materialDic={}
    #                 textureFilenameList = []
    #                 isReadMaterial = False
    #             materialList = lineList[index].split(" ")
    #             materialDic['mName'] = materialList[1]
    #             isReadMaterial = True
    #         if isReadMaterial and tempLine.find("TextureFilename")>=0:
    #             textureFilenameList.append(tempLineNext.split("\"")[1])
    #         #if isReadFrame and isReadMeshMaterialList and tempLine=="}" and tempLineNext=='}':
    #
    #         if tempLine[:7]=="Frame _":
    #             if isFirstLoad:
    #                 materialDic['textureFilename'] = textureFilenameList
    #
    #                 materialDicList.append(materialDic)
    #                 materialDic = {}
    #                 textureFilenameList = []
    #                 isReadMaterial = False
    #
    #                 isFirstLoad=False
    #
    #             frameDic['frameName']=tempLine.split(' ')[1]
    #             isReadFrame=True
    #
    #         if isReadFrame and tempLine.find("FrameTransformMatrix")>=0:
    #             frameTransformMatrixList=tempLineNext.split(",")
    #             frameDic['lon']=frameTransformMatrixList[12]
    #             frameDic['lat'] = frameTransformMatrixList[14]
    #         if isReadFrame and tempLine.find("Mesh _")>=0:
    #             frameDic['meshName']=tempLine.split(' ')[1][1:]
    #             isReadMesh=True
    #         if isReadFrame and isReadMesh :
    #
    #             if len(tempLine.split(";"))>2:
    #                 if len(tempLineNext.split(";")) <= 2: isReadMesh = False
    #                 tempX =  float(tempLine.split(";")[0])
    #                 tempY = float(tempLine.split(";")[2])
    #                 if isFirstLoadMeshXY:
    #                     meshMinX=tempX
    #                     meshMaxX=tempX
    #                     meshMinY=tempY
    #                     meshMaxY=tempY
    #                     isFirstLoadMeshXY=False
    #                 else:
    #                     if tempX>meshMaxX:meshMaxX=tempX
    #                     if tempX<meshMinX:meshMinX=tempX
    #                     if tempY>meshMaxY:meshMaxY=tempY
    #                     if tempY<meshMinY:meshMinY=tempY
    #                 frameDic['maxY']=meshMaxY
    #                 frameDic['maxX']=meshMaxX
    #                 frameDic['minX']=meshMinX
    #                 frameDic['minY']=meshMinY
    #
    #                 if len(tempLineNext.split(";")) < 2: isReadMesh=False
    #         if isReadFrame and tempLine.find("MeshMaterialList")>=0:
    #             isReadMeshMaterialList=True
    #             materialReadList=[]
    #         if isReadFrame and isReadMeshMaterialList:
    #             if tempLine[0]=='{' and tempLine[-1]=='}':
    #                 materialName = tempLine.split(" ")[1]
    #                 for i in materialDicList:
    #                     if i['mName']==materialName:
    #                         materialReadList.extend (i['textureFilename'])
    #                         break
    #             if tempLineNext=='}':
    #                 isReadMeshMaterialList=False
    #                 isFirstLoadMeshXY=True
    #                 frameDic['materialList']=materialReadList
    #                 # tempFrame = FrameOfX(frameName=frameDic['fram         eName'],
    #                 #                      location=frameDic['location'],
    #                 #                      meshName=frameDic['meshName'],
    #                 #                      mbr=frameDic['mbr'],
    #                 #                      materialList=frameDic['materialList']
    #                 #                      )
    #                 tempFrame = FrameOfX(kwargs=frameDic)
    #                 frameDicList.append(tempFrame)
    #
    #     print(frameDicList)
    #     print(materialDicList)
    #
    #     # 根据解析结果frameDicList生成最小外接矩形shp文件
    #     outputShapePath = r'C:\Users\Administrator\Desktop\数据质检\数据文件\三维\outPutX.shp'
    #     driver = ogr.GetDriverByName('ESRI Shapefile')
    #
    #     if os.path.exists(outputShapePath):
    #         driver.DeleteDataSource(outputShapePath)
    #     outPutDataSource = driver.CreateDataSource(outputShapePath)
    #     outLayer = outPutDataSource.CreateLayer(outputShapePath, geom_type=ogr.wkbMultiPolygon)
    #
    #     fieldName = 'ID'
    #     fieldType = ogr.OFTString
    #
    #     idField = ogr.FieldDefn(fieldName, fieldType)
    #     outLayer.CreateField(idField)
    #
    #     for tempFrameDic in frameDicList:
    #         tempInitPointLanlon= pygeodesy.ellipsoidalNvector.LatLon(float(tempFrameDic.lat), float(tempFrameDic.lon))
    #         tempInitPointLanlon.datum== pygeodesy.datum.Datums.CGCS2000
    #         destLBPoint=tempInitPointLanlon.destinationNed(pygeodesy.ellipsoidalNvector.Ned(float(tempFrameDic.minY),float(tempFrameDic.minX),0))
    #         destRTPoint=tempInitPointLanlon.destinationNed(pygeodesy.ellipsoidalNvector.Ned(float(tempFrameDic.maxY),float(tempFrameDic.maxX),0))
    #         tempFrameDic.destLBPoint = destLBPoint
    #         tempFrameDic.destRTPoint = destRTPoint
    #
    #         # lonDe = destRTPoint.latlon[1] - destLBPoint.latlon[1]
    #         # latDe = destRTPoint.latlon[0] - destLBPoint.latlon[0]
    #
    #         fieldDic['fieldName']='ID'
    #         fieldDic['fieldValue']=tempFrameDic.frameName
    #
    #         pointToPolygon(outLayer,destLBPoint.latlon,destRTPoint.latlon,fieldDic)
    #     outPutDataSource.Destroy()
    #
    #     #计算给定面要素的最小外界矩形MBR,并计算中心dian坐标
    #     inputPolygonPath=r'C:\Users\Administrator\Desktop\数据质检\数据文件\三维\res.shp'
    #     inputPolygonSource=driver.Open(inputPolygonPath)
    #     layer=inputPolygonSource.GetLayer(0)
    #
    #     tempPolyFeature=layer.GetNextFeature()
    #     while tempPolyFeature is not None:
    #         geom =tempPolyFeature.GetGeometryRef()
    #         envelope=geom.GetEnvelope()
    #         tempCenterLon=(envelope[0]+envelope[1])/2
    #         tempCenterLat = (envelope[2] + envelope[3]) / 2
    #
    #         centerEnvelopeList.append({'centerLon':tempCenterLon,
    #                                    'centerLat':tempCenterLat,
    #                                    'FCODE':tempPolyFeature.GetField('FCODE'),
    #                                    'OBJECTID':tempPolyFeature.GetField('OBJECTID'),
    #                                    'geomWkt':geom.ExportToWkt()
    #                                    })
    #         tempPolyFeature = None
    #         geom = None
    #         tempPolyFeature = layer.GetNextFeature()
    #
    #     inputPolygonSource.Release()
    #     #遍历三维面要素，对res面要素进行匹配
    #     outPutDataSource = driver.Open(outputShapePath,1)
    #     outLayer=outPutDataSource.GetLayer(0)
    #     outLayer.ResetReading()
    #     # 添加偏差值字段deviationValue
    #     deviationField=ogr.FieldDefn('devValue',ogr.OFTString)
    #     deviationField.SetWidth(20)
    #     outLayer.CreateField(deviationField)
    #     # 添加匹配字段match3DFcodeField
    #     match3DFcodeField = ogr.FieldDefn('ma3DFcode', ogr.OFTString)
    #     match3DFcodeField.SetWidth(20)
    #     outLayer.CreateField(match3DFcodeField)
    #     # 添加匹配字段match3DObjectIDField
    #     match3DObjectIDField = ogr.FieldDefn('ma3DObjID', ogr.OFTString)
    #     match3DObjectIDField.SetWidth(10)
    #     outLayer.CreateField(match3DObjectIDField)
    #
    #
    #
    #     temp3Dfeature=outLayer.GetNextFeature()
    #     while temp3Dfeature is not None:
    #
    #         deviationValue = 'emptyDv'
    #         match3DFcode = ''
    #         match3DOBJECTID = ''
    #         isFirstFindInclude=True
    #         geom3D =temp3Dfeature.GetGeometryRef()
    #         geom3DEnvelop=geom3D.GetEnvelope()
    #         isIn3DGeomList = []
    #         for centerEnvelope in centerEnvelopeList:
    #               if geom3DEnvelop[0] <= centerEnvelope['centerLon'] <= geom3DEnvelop[1] and geom3DEnvelop[2] <= centerEnvelope['centerLat'] <= geom3DEnvelop[3]:
    #                   isIn3DGeomList.append(centerEnvelope)
    #                   #print(centerEnvelope['OBJECTID'])
    #         if len(isIn3DGeomList) == 0:
    #             deviationValue='emptyDv'
    #             match3DFcode=''
    #             match3DObjectID=''
    #             #temp3Dfeature.SetField('deviationValue','无匹配项')
    #         if len(isIn3DGeomList) == 1:
    #             centerEnvelope1=isIn3DGeomList[0]
    #             # centerEnvelopePrj = LatLon(centerEnvelope['centerLat'],\
    #             #                            centerEnvelope['centerLon'], \
    #             #                             datum =pygeodesy.datum.Datums.CGCS2000)
    #             # geom3DEnvelopCenPrj = LatLon((geom3DEnvelop[2]+geom3DEnvelop[3])/2,\
    #             #                              (geom3DEnvelop[0]+geom3DEnvelop[1])/2, \
    #             #                              datum=pygeodesy.datum.Datums.CGCS2000)
    #
    #             #deviationValue=centerEnvelopePrj.distanceTo(geom3DEnvelopCenPrj)
    #             deviationValue=disPrjCalculatePointToEnvelope(centerEnvelope1['centerLat'],
    #                                                           centerEnvelope1['centerLon'],
    #                                                           geom3DEnvelop)
    #             match3DFcode=centerEnvelope1['FCODE']
    #             match3DOBJECTID=centerEnvelope1['OBJECTID']
    #
    #         if len(isIn3DGeomList) > 1:#求相交面积，并排序取最大
    #             # maxIntersectionDic={'maxIntersectionArea':0,
    #             #                     'maxIntersectionGeom':None,
    #             # }
    #             maxIouValue=0
    #             minDis=0 # 同一面内包含多个3D面要素，只取距离最近的那个
    #             maxIntersectionEnvelope={}
    #             geomSameWktList=[]
    #             geom3DArea = ogr.Geometry.Area(geom3D)
    #             for tempCenterEnvelope in isIn3DGeomList:
    #                 # 利用交并比确定最大值进行匹配
    #                 geomFromWkt=ogr.CreateGeometryFromWkt(tempCenterEnvelope['geomWkt'])
    #                 refPolyGeomArea=ogr.Geometry.Area(geomFromWkt)
    #                 interSectionGeom = geom3D.Intersection(geomFromWkt)
    #                 interSectionGeomArea=ogr.Geometry.Area(interSectionGeom)
    #                 iouValue=interSectionGeomArea/(geom3DArea+refPolyGeomArea-interSectionGeomArea)
    #
    #                 #print(iouValue)
    #                 if iouValue>maxIouValue:
    #                     maxIouValue=iouValue
    #                     maxIntersectionEnvelope=tempCenterEnvelope
    #                     #maxIntersectionGeom=tempCenterEnvelope['geom']
    #                 # if iouValue == maxIouValue == 1:
    #                 #     maxIouValue = iouValue
    #                 #     geomFromWktEn = geomFromWkt.GetEnvelope()
    #                 #     tempMinDis = disPrjCalculatePointToEnvelope((geomFromWktEn[2] + geomFromWktEn[3]) / 2,
    #                 #                                                 (geomFromWktEn[0] + geomFromWktEn[1]) / 2,
    #                 #                                                 geom3DEnvelop)
    #                 #     if isFirstFindInclude :
    #                 #         minDis=tempMinDis
    #                 #         maxIntersectionEnvelope = tempCenterEnvelope
    #                 #         isFirstFindInclude=False
    #                 #     if (not isFirstFindInclude) and tempMinDis<minDis:
    #                 #         minDis=tempMinDis
    #                 #         maxIntersectionEnvelope = tempCenterEnvelope
    #
    #                 geomFromWkt=None
    #                 interSectionGeom=None
    #
    #             # centerEnvelopePrj = LatLon(centerEnvelope['centerLat'], \
    #             #                            centerEnvelope['centerLon'], \
    #             #                            datum=pygeodesy.datum.Datums.CGCS2000)
    #             # geom3DEnvelopCenPrj = LatLon((geom3DEnvelop[2] + geom3DEnvelop[3]) / 2, \
    #             #                              (geom3DEnvelop[0] + geom3DEnvelop[1]) / 2, \
    #             #                              datum=pygeodesy.datum.Datums.CGCS2000)
    #             # deviationValue = centerEnvelopePrj.distanceTo(geom3DEnvelopCenPrj)
    #             # 设置交并比阈值，去除差距太大的项
    #             if maxIouValue >= 0.2:
    #                 deviationValue = disPrjCalculatePointToEnvelope(maxIntersectionEnvelope['centerLat'],
    #                                                             maxIntersectionEnvelope['centerLon'],
    #                                                             geom3DEnvelop)
    #                 match3DFcode = centerEnvelope1['FCODE']
    #                 match3DOBJECTID = centerEnvelope1['OBJECTID']
    #             else:
    #                 deviationValue = 'emptyDv'
    #                 match3DFcode = ''
    #                 match3DOBJECTID = ''
    #             isIn3DGeomList = []
    #
    #         # 属性表写入
    #         temp3Dfeature.SetField('devValue',deviationValue)
    #         temp3Dfeature.SetField('ma3DFcode', match3DFcode)
    #         temp3Dfeature.SetField('ma3DObjID', match3DOBJECTID)
    #         outLayer.SetFeature(temp3Dfeature)
    #
    #         geom3D=None
    #         # 读取下一个
    #         temp3Dfeature=outLayer.GetNextFeature()
    #
    #         # ogr.Geometry.Within(point1, geom3D)
    #
    #     outPutDataSource.Destroy()
    #     print(frameDicList)
    # finally:
    #     file_object.close()
    inputFilePath=r'C:\Users\Administrator\Desktop\数据质检\数据文件\三维\testAll709.X'
    referShpFilePath=r'C:\Users\Administrator\Desktop\数据质检\数据文件\三维\res.shp'
    outputFilePath=r'C:\Users\Administrator\Desktop\数据质检\数据文件\三维\outPut718X.shp'
    test=devValueCheck(inputFilePath,referShpFilePath,outputFilePath)
    test.run()
