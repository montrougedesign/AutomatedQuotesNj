


from operator import index
import re
from sys import api_version

from cv2 import detail_ExposureCompensator


wl = ['k','WL1','WL2','WL3','WL4','WL5','WL6','WL7']


test = 'WL1'

test_list = ['h','WL1','ABR']

tickers = [
        [],
        ['T','VZ','KBWD'],
        ['ADBE','ALGN','ISGR'],
        ['NKE','LULU','ETSY'],
        ['V','AXP','PYPL'],
        ['MMP','EPD','WPC'],
        ['TROW','IVZ','SCHW'],
        ['HRB','WBA','FDX'],
        ['CRM','SQ','JPM']]

ans = []

def switch(wl):
        my_dict ={
            '':0,
            'WL1':1,
            'WL2':2,
            'Wl3':3,
            'Wl4':4,
            'Wl5':5,
            'WL6':6,
            'WL7':7,
            'WL8':8,
            'WL9':9,
            'WL10':10,
            'WL11':11,
            'WL12':12,
            'WL13':13,
            'WL14':14,
            'WL15':15,
            'WL16':16,
            'WL17':17,
            'WL18':18,
        }
        return my_dict.get(wl)



for a in test_list:
    if str(type(switch(a))) == "<class 'int'>":
        dex = test_list.index(a)
        list_name_index = switch(a)
        list_of_tickers = tickers[list_name_index]
        for item in list_of_tickers:
            print(item + "\n")
        print(a)
        print(dex)
        print('hello')
        
    elif str(type(switch(a))) == "<class 'NoneType'>":
        dex = test_list.index(a)
        print(a)
        print(dex)
        print('nohello')


