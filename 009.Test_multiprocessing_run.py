# -*- coding:utf-8 -*-
# @auth ivan
# @time 20190110
# @goal test the multiprocessing run
import os
import time
import multiprocessing


def worker(sign):
    print(sign, 'pid:', os.getpid())
    time.sleep(1)
    print(1)


print('Main:', os.getpid())
plist = []
for j in range(5):
    p = multiprocessing.Process(target=worker, args=('process', ))
    p.start()
    plist.append(p)
p.join()
"""
Main: 99228
process pid: 99229
process pid: 99230
process pid: 99231
process pid: 99232
process pid: 99233
1
1
1
1
1
"""