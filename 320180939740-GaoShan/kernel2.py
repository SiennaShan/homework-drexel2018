# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 09:37:15 2020

@author: 高珊
"""
__copyright__ = 'T1,Lanzhou University,2020'
__license__ = 'GPLV2 or later'
__version__ = 0.1
__author__ = ['Shan Gao']
__email__ = ['shgao18@lzu.edu.cn']
__status__ = 'done'

from subprocess import Popen, PIPE, DEVNULL
from matplotlib import pyplot as plt

class Get_reproduce:
    def __init__(self,kVer):
        self.get_time("D:\linux-stable","v4.5")
        self.kVer=kVer
        
    def get_time(self, repo,ver):
        cmd_tag = 'git tag -l ' + '"' + ver + '.*"'
        v = Popen(cmd_tag, cwd=repo, stdout=PIPE)
        ttime = v.communicate()[0].decode('utf-8').split('\n')
        date = []
        for i in ttime:
            cmd_str = 'git log -1 --pretty=format:\"%ct\" '+str(i)
            p = Popen(cmd_str, cwd=repo, stdout=PIPE, stderr=DEVNULL)
            doc = p.communicate()[0].decode('utf-8').split('\n')
            date.append(doc)
        return date,ttime 
        
    def plot(self,data,ttime):
        plt.title('release in order')
        plt.xlabel('time')
        plt.ylabel('patchlevel')
        plt.scatter(data, time)


re = get_list()