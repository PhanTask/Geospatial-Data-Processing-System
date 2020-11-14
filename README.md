# Geospatial-Data-Processing-System

## Introduction
Massive multi-source heterogeneous geospatial data produced and collected by Geomatics Center Of Zhejiang, including Digital Orthophoto Map(DOM), Digital Elevation Model(DEM), Spatio-temporal Thematic Data(STD) and 3D Building Model Data(BMD), need a highly effective method to automate data quality inspection process. In this project, a data quality inspection system, consisting of 4 functional modules and 11 task units, was developed. Currently, the system has been put into use, significantly reducing the workload for the Geomatics Center.

![](http://www.jinmengrao.com/gdp/img/GDP-2.jpg)

Specifically, for DOM and DEM data, we designed and implemented several efficient algorithms to detect or remove outlier area(e.g. black or white collars, inner or outer irregular outlier area) or merging error area(e.g. cracked, misaligned area), and to check their metadata and locations. For STD data, we apply regular expression, fuzzy matching and some other methods to analyze and process their locations and attributes. For BMD data, we check their location accuracy and textures by automatically parsing the model data and mapping their coordinates into geographic coordinate systems(e.g. WGS84, CGCS2000).

![](http://www.jinmengrao.com/gdp/img/GDP-3.jpg)

The system is written in Python with plenty of open source libraries such as Pyside, GDAL/OGR, Numpy, Geopandas, Fiona, Shapely, PyGeodesy, Fuzzywuzzy, etc. Threading and multiprocessing are used to parallelize data processing tasks, and Cython is used to accelerate core algorithms.

## References

Du, T., Rao, J., Peng, R. and Du, Q*✉. (2020). Multi-Source Geographic Data Efficient Quality Inspection System Based on Python. Journal of Geomatics 45 (2), 1-6.

Rao, J.✉, Yu, J., Zhu, X., Du, T. and Ren, F. (2019). An Algorithm For Removing Invalid Pixels In Remote Sensing Images Based On Vector Boundary Extraction. Journal of Geomatics.
