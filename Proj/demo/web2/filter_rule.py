# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:02:20 2020

@author: David
"""

# import pandas as pd
# df = pd.read_csv('C://Users//David//Desktop//test.xls',sep='\t')
#import difflib
#sgrna = 'GCACTGTCCCTAATACACTGTGG'[:-3]

def differ(str1,str2):
    diff = {'0':0,'1':0,'2':0}#0:0~2,1:3~7,2:8~19
    for i in range(0,3):
        if str1[i] != str2[i]:
            diff['0']+=1
    for i in range(3,8):
        if str1[i] != str2[i]:
            diff['1']+=1
    for i in range(8,20):
        if str1[i] != str2[i]:
            diff['2']+=1
    return diff

def test(file_name,sgrna):
    with open(file_name,'r') as seqf:
        while True:
            x=seqf.readline()
            if x:
                seq = x.split('\t')[5] 
                pam = x.split('\t')[6]
                print(pam)
                diff = differ(seq,sgrna[:-3])
                print(diff)
                if pam[1]=='G':
                    
                    if diff['0']+diff['1']+diff['2']==0:
                        seqf.close()
                        return 0
                    elif diff['0']+diff['1']+diff['2']==1:
                        seqf.close()
                        return 1
                    elif diff['0']==2 and (diff['1']+diff['2']==0):
                        seqf.close()
                        return 2
                    elif diff['0']==1 and (diff['1']+diff['2']==1):
                        seqf.close()
                        return 2
                    elif diff['0']==3 and (diff['1']+diff['2']==0):
                        seqf.close()
                        return 3
                    elif diff['0']==2 and (diff['1']+diff['2']==1):
                        seqf.close()
                        return 3
                    elif (diff['0']==1) and (diff['1']==2) and (diff['2']==0):
                        seqf.close()
                        return 3
                    elif diff['0']==3 and (diff['1']+diff['2']==1):
                        seqf.close()
                        return 4
                    elif (diff['0']==2) and (diff['1']==2) and (diff['2']==0):
                        seqf.close()
                        return 4
                    else:
                        continue
                elif pam[1]=='A':
                    if diff['0']+diff['1']+diff['2']==0:
                        seqf.close()
                        return 0
                    elif diff['0']+diff['1']+diff['2']==1:
                        seqf.close()
                        return 1
                    elif diff['0']==2 and (diff['1']+diff['2']==0):
                        seqf.close()
                        return 2
                    elif diff['0']==1 and (diff['1']+diff['2']==1):
                        seqf.close()
                        return 2
                    elif diff['0']==3 and (diff['1']+diff['2']==0):
                        seqf.close()
                        return 3
                    elif diff['0']==2 and (diff['1']+diff['2']==1):
                        seqf.close()
                        return 3
                    elif (diff['0']==1) and (diff['1']==2) and (diff['2']==0):
                        pass
                    elif diff['0']==3 and (diff['1']+diff['2']==1):
                        seqf.close()
                        return 4
                    elif (diff['0']==2) and (diff['1']==2) and (diff['2']==0):
                        pass
                    else:
                        continue
            else:
                break
                
    return 'PASS'
    seqf.close()

def test_h(file_name):
    with open(file_name,'r') as seqf:
        i=0
        while True:
            i+=1
            x=seqf.readline()
            if x!='' and x:
                if x.split('\t')[10] in ['IGH','IGK']:
                    seqf.close()
                    return 0
                # try:
                #     x.split('\t')[10]
                # except:
                #     print(type(x))
                #     print(i)
            else:
                break
    seqf.close()            
    #return x[-1]
    return 'PASS'
    



