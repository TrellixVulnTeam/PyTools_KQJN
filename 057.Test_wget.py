# -*-coding:utf-8-*-
# @auth ivan
# @time 20200620 12:24:19
# @goal wget the file online
"""
SOMETIME U USE
    os.system("wget ... -o ...")
WILL BE STOP.
"""
import wget
DATA_URL = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
DATA_PATH = '057.Test_wget.png'
wget.download(DATA_URL, out=DATA_PATH)
# 100% [..............................................................................] 15444 / 15444%
