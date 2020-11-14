# -*- coding:utf-8 -*-

from implements import domImpl
import ogr
import gdal
from shapely.geometry import shape
import json

if __name__ == '__main__':
    # polygonDS = ogr.Open(r'E:\20180401中文\data\dataLab\H51G030014\H51G030014_N.shp', 1)
    # layer = polygonDS.GetLayer(0)
    # feat = layer.GetFeature(0)
    # # if feat.GetField('status') == 0:
    # #     feat = None
    # #     feat = layer.GetFeature(1)
    # #     layer.DeleteFeature(0)
    # # else:
    # #     layer.DeleteFeature(1)
    # geo = feat.geometry()
    # poly = shape(json.loads(geo.ExportToJson()))
    # fx = poly.buffer(distance=10 * 0.000005, resolution = 2, cap_style=1, join_style=2).buffer(distance=-10 * 0.000005, resolution = 2, cap_style=1,
    #                                                                            join_style=2)
    # geobf = ogr.CreateGeometryFromWkb(fx.wkb)
    # feat.SetGeometry(geobf)
    # layer.SetFeature(feat)
    # polygonDS = None
    #
    # # gdal.Rasterize(dstDS,dstFilename,attribute = 'status')
    driver = ogr.GetDriverByName("ESRI Shapefile")
    shpFilename = r'E:\20180401中文\data\dataLab\H51G030014\H51G030014_N.shp'
    dst_ds = driver.Open(shpFilename, 1)
    dst_layer2 = dst_ds.GetLayer(0)

    maxAreaFID = None
    maxTempArea = 0
    delIndexList = []
    f = dst_layer2.GetNextFeature()
    while f is not None:
        # for f in dst_layer2:
        if f.GetField('status') == 0:
            delIndexList.append(f.GetFID())
        else:
            if f.geometry().GetArea() > maxTempArea:
                if maxAreaFID != None:
                    delIndexList.append(maxAreaFID)
                maxAreaFID = f.GetFID()
                maxTempArea = f.geometry().GetArea()
            else:
                delIndexList.append(f.GetFID())
        f = dst_layer2.GetNextFeature()
    [dst_layer2.DeleteFeature(i) for i in delIndexList]

    feat = dst_layer2.GetFeature(maxAreaFID)

