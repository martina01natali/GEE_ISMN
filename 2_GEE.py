import os
from ismn import readers as ismn
from GEE_ISMN import setup_pkg as pkg
from GEE_ISMN import earthengine as earth
from GEE_ISMN import postprocess as pp
from GEE_ISMN import visualization as vis

import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
from matplotlib.legend_handler import HandlerLine2D
# import pandas as pd
# import geopandas as gpd
# import ee

user_input = pkg.setup_pkg()

#############

test_dict = {}
test_file1 = "./data/ISMN_Filt/" \
             "PBO-H2O_PBO-H2O_BILLINGSAP_sm_0.000000_0" \
             ".050000_GPS_20140401_20191015.stm "
test_file2 = "./data/ISMN_Filt/RSMN_RSMN_Dumbraveni_sm_0.000000_0" \
             ".050000_5TM_20140401_20191015.stm"
data1 = ismn.read_data(test_file1)
data2 = ismn.read_data(test_file2)

test_dict[data1.network + "-" + data1.sensor + "-" + data1.station] = [
    data1.latitude, data1.longitude, data1.data]
test_dict[data2.network + "-" + data2.sensor + "-" + data2.station] = [
    data2.latitude, data2.longitude, data2.data]

test_dict_2 = earth.lc_filter(test_dict, user_input)

test_dict_3 = earth.get_s1_backscatter(test_dict_2)

pp.filter_s1(test_dict_3)

station = 'RSMN-5TM-Dumbraveni'
orbit = 'desc'
pol = 'VH'

vis.plot_data(test_dict_3, station, orbit, pol)

