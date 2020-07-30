# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 08:51:00 2020

@author: David
"""
# from demo.web3 import req
# from demo.web2 import filter_rule
#root = 'C:\\Users\\David\\Desktop\\demo\\'
def web3(dic_web2,root):
    from demo.web3 import req
    from demo.web2 import filter_rule
    dic = dic_web2
    new_dic= dict.fromkeys(dic,[])
    for g in dic:
        for i in range(len(dic[g])):
            seqlist = req.req3(dic[g][i],g,i,root)
            if filter_rule.test(root+'web2files\\'+g+'_mouse_'+str(i)+'.csv', dic[g][i])=='PASS':
                new_dic[g].append(dic[g][i])
    return new_dic
            
    