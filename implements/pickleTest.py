# -*- coding:utf-8 -*-
from osgeo import gdal
import dill


class PickalableSWIG:
    def __setstate__(self, state):
        self.__init__(*state['args'])

    def __getstate__(self):
        return {'args': self.args}

class PickalableGDALDataset(gdal.Dataset,PickalableSWIG):
    def __init__(self,*args):
        self.args = args

if __name__ == '__main__':
    path = r"G:\武大质检程序样例数据\影像\1自动处理影像异常值\H50G022096\H50G022096.img"
    ds = gdal.Open(path)
    pickleDs = PickalableGDALDataset(ds)
    dill.dumps(pickleDs)