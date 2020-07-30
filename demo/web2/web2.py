# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:58:37 2020

@author: David
"""

import os
from demo.web2 import req
from demo.web2 import filter_rule
#root = 'C:\\Users\\David\\Desktop\\demo\\'
def get_glist(root):
    #os.chdir(root)
    glist = [i.split('_')[0] for i in os.listdir(root+'//genes//')]
    return glist

def get_all_seq(glist,root):
    all_seq = {}
    for g in glist:
        g_ = []
        with open(root+'//genes//'+g+'_sequence'+'.csv','r') as f:
            while True:
                x = f.readline()
                if x:
                    g_.append(('').join(x.split(',')[2:4]))
                else:
                    break
            f.close()
        all_seq[g]=g_
    return all_seq#dict:{genename:[all sequences,]}

def filter_by_web2(all_seq,root):
    new_seq = dict.fromkeys(all_seq,[])
    for g in all_seq:
        
        for i in range(len(all_seq[g])):
            if req.req2(all_seq[g][i],'human',g,i,root)=='OK':#filter as human
                if filter_rule.test_h(root+'web1files\\'+g+'_'+'human'+'_'+str(i)+'.xls') == 'PASS':
                    if req.req2(all_seq[g][i],'mouse',g,i,root)=='OK':
                        if filter_rule.test(root+'web1files\\'+g+'_'+'mouse'+'_'+str(i)+'.xls',all_seq[g][i]) == 'PASS':
                            new_seq[g].append(all_seq[g][i])
    return new_seq
                
def web2(root):
    glist = get_glist(root)
    all_seq = get_all_seq(glist,root)
    result=filter_by_web2(all_seq,root)
    return result#dict:{genename:[all sequences,]}
    
        

        