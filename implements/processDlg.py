# -*- coding: utf-8 -*-
"""
processDlg.py
~~~~~~~~~~~~~

执行检查操作后后台运行质检算法，记录日志与提示进度的对话框。

:copyright: (c) 2018 by Jinmeng Rao.
"""

from PySide2 import QtWidgets
from ui import ui_processdlg
from implements import domImpl,domCoverImpl,domFormatImpl,domMatchImpl
from implements.demImpls import demOutlierImpl,demMosaicImpl
from implements.stImpls import stdAttImpl,stdCodeImpl,stdRepeatImpl,CY_stdAttImpl,CY_stdCodeImpl
from implements.tdImpls import xFileTextureCheckImp, deviationValueCheckImp

class processdlg(QtWidgets.QDialog):
    def __init__(self, taskType, kwd): #伪重载，实现processdlg可复用
        super(processdlg, self).__init__(None)
        #self.processValue = 0
        self.ui = ui_processdlg.Ui_ProcessDialog()
        self.ui.setupUi(self)
        self.ui.terminateButton.clicked.connect(self.stopfunc)
        self.ui.finishButton.clicked.connect(self.finished)
        self.t = '线程'
        #根据taskType来执行相应任务线程
        if taskType == 1:#DOM WB
            self.t = domImpl.domImpl(domDirPath = kwd['domDirPath'],
                                     domDirOutputPath = kwd['domDirOutputPath'],
                                     outlierValue = kwd['outlierValue'],
                                     nearDist = kwd['nearDist'],
                                     maxNonBlack = kwd['maxNonBlack'],
                                     delNum = kwd['delNum'],
                                     fileType = kwd['fileType'],
                                     ovrBuild = kwd['ovrBuild'],
                                     nodataFill=kwd['nodataFill'],
                                     c254=kwd['c254'],
                                     easyKill=kwd['easyKill'],
                                     easyColors=kwd['easyColors'],
                                     easyNearDist=kwd['easyNearDist']
                                     )
            self.t.logRcd.infomsgSignal.connect(self.onNewLog)
            self.t.logRcd.processSignal.connect(self.onSetProcessBarValue)
            self.t.doneflag.connect(self.onSetFinishButtonEnabled)
            self.t.start()
        elif taskType == 2:#DOM COVER
            self.t=domCoverImpl.coverCheck(domIndexDirPath=kwd['domIndexDirPath'],
                                            domCoverDirPath=kwd['domCoverDirPath'],
                                            domCoverOutputDirPath=kwd['domCoverOutputDirPath'],
                                            fileType=kwd['fileType'])
            self.t.logRcd.infomsgSignal.connect(self.onNewLog)
            self.t.logRcd.processSignal.connect(self.onSetProcessBarValue)
            self.t.doneflag.connect(self.onSetFinishButtonEnabled)
            self.t.start()
        elif taskType == 3:#DOM FORMAT
            self.t = domFormatImpl.domFormatImpl(domDirPath = kwd['domDirPath'],
                                                 paramsDict = kwd['paramsDict']
            )
            self.t.logRcd.infomsgSignal.connect(self.onNewLog)
            self.t.logRcd.processSignal.connect(self.onSetProcessBarValue)
            self.t.doneflag.connect(self.onSetFinishButtonEnabled)
            self.t.start()
        elif taskType == 4:#DOM MATCH
            self.t = domMatchImpl.domMatchImpl(indexDirPath = kwd['indexDirPath'],
                                               panCap = kwd['panCap'])
            self.t.logRcd.infomsgSignal.connect(self.onNewLog)
            self.t.logRcd.processSignal.connect(self.onSetProcessBarValue)
            self.t.doneflag.connect(self.onSetFinishButtonEnabled)
            self.t.start()
        elif taskType == 5:#DEM OUTLIER
            self.t = demOutlierImpl.demOutlierImpl(demDirPath = kwd['demDirPath'],
                                                   demDirOutputPath = kwd['demDirOutputPath'],
                                                   valueRange = kwd['valueRange'],
                                                   fileType = kwd['fileType']
                                                   )
            self.t.logRcd.infomsgSignal.connect(self.onNewLog)
            self.t.logRcd.processSignal.connect(self.onSetProcessBarValue)
            self.t.doneflag.connect(self.onSetFinishButtonEnabled)
            self.t.start()
        elif taskType == 6:#DEM MOSAIC
            self.t = demMosaicImpl.demMosaicImpl(demDirPath = kwd['demDirPath'],
                                                 demDirOutputPath = kwd['demDirOutputPath'],
                                                 valueRange = kwd['valueRange'],
                                                 slopeThreshold=kwd['slopeThreshold'],
                                                 fileType = kwd['fileType']
                                                 )
            self.t.logRcd.infomsgSignal.connect(self.onNewLog)
            self.t.logRcd.processSignal.connect(self.onSetProcessBarValue)
            self.t.doneflag.connect(self.onSetFinishButtonEnabled)
            self.t.start()
        elif taskType == 7:#STD ATT
            self.t = CY_stdAttImpl.propertyStdCheckImp(gdbInputDirPath = kwd['gdbInputDirPath'],
                                                    gdbDirOutputPath = kwd['gdbDirOutputPath'],
                                                    reMatchDic = kwd['reMatchDic'],
                                                    jsonDict=kwd['jsonDict'],
                                                 )
            # self.t = stdAttImpl.propertyStdCheckImp(gdbInputDirPath = kwd['gdbInputDirPath'],
            #                                         gdbDirOutputPath = kwd['gdbDirOutputPath'],
            #                                         reMatchDic = kwd['reMatchDic'],
            #                                         jsonDict=kwd['jsonDict'],
            #                                      )
            self.t.logRcd.infomsgSignal.connect(self.onNewLog)
            self.t.logRcd.processSignal.connect(self.onSetProcessBarValue)
            self.t.doneflag.connect(self.onSetFinishButtonEnabled)
            self.t.start()
            pass
        elif taskType == 8:#STD CODE
            # self.t = CY_stdCodeImpl.stdCodeImpl(indexDirPath = kwd['indexDirPath'],
            #                                     outputDirPath = kwd['outputDirPath'],
            #                                     )
            # self.t.logRcd.infomsgSignal.connect(self.onNewLog)
            # self.t.logRcd.processSignal.connect(self.onSetProcessBarValue)
            # self.t.doneflag.connect(self.onSetFinishButtonEnabled)
            # self.t.start()
            self.t = stdCodeImpl.stdCodeImpl(indexDirPath = kwd['indexDirPath'],
                                            outputDirPath = kwd['outputDirPath'],
                                            )
            self.t.logRcd.infomsgSignal.connect(self.onNewLog)
            self.t.logRcd.processSignal.connect(self.onSetProcessBarValue)
            self.t.doneflag.connect(self.onSetFinishButtonEnabled)
            self.t.start()
        elif taskType == 9:#STD REPEAT
            self.t = stdRepeatImpl.repeatCheckImp(gdbDirInputPath = kwd['gdbDirInputPath'],
                                                  gdbDirOutputPath = kwd['gdbDirOutputPath'],
                                                  matchDegree = kwd['matchDegree']
                                                 )
            self.t.logRcd.infomsgSignal.connect(self.onNewLog)
            self.t.logRcd.processSignal.connect(self.onSetProcessBarValue)
            self.t.doneflag.connect(self.onSetFinishButtonEnabled)
            self.t.start()
        elif taskType == 10:# THRD TEX
            self.t = xFileTextureCheckImp.xFileTextureCheck(inputFileFolderPath = kwd['thrDTexInputPath'],
                                                            textureFolder = kwd['thrDTexTexturePath']
                                                 )
            self.t.logRcd.infomsgSignal.connect(self.onNewLog)
            self.t.logRcd.processSignal.connect(self.onSetProcessBarValue)
            self.t.doneflag.connect(self.onSetFinishButtonEnabled)
            self.t.start()
        elif taskType == 11:# THRD DEV
            self.t = deviationValueCheckImp.devValueCheck(inputFileFolderPath = kwd['thrDDevInputPath'],
                                                          referShpFilePath = kwd['thrDDevReferencePath'],
                                                          outputFilePath = kwd['thrDDevOutputPath']
                                                 )
            self.t.logRcd.infomsgSignal.connect(self.onNewLog)
            self.t.logRcd.processSignal.connect(self.onSetProcessBarValue)
            self.t.doneflag.connect(self.onSetFinishButtonEnabled)
            self.t.start()
        else:
            # TODO 剩下的任务
            pass

    def onNewLog( self, msg ):
        try:
            self.ui.logText.append( msg )
        except Exception as e:
            print(e.__str__())

    def onSetProcessBarValue(self,pValue):
        self.ui.progressBar.setValue(pValue)

    def onSetFinishButtonEnabled(self,issuccessful):
        self.ui.finishButton.setEnabled(issuccessful)

    def stopfunc(self):
        self.t.dostop=True
        self.t.quit()
        self.ui.progressBar.setValue(0)

    def finished(self):
        self.t.dostop=True
        self.t.quit()
        self.accept()

    def closeEvent(self, event):
        self.t.dostop=True
        self.t.quit()
        self.ui.progressBar.setValue(0)
        return super( processdlg, self ).closeEvent( event )