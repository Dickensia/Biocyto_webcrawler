# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:24:32 2020

@author: David
"""

root='C:\\Users\\David\\Desktop\\demo\\'
from demo.web2 import web2
from demo.web3 import web3


def main(root):
    result2 = web2.web2(root)
    result = web3.web3(result2,root)
    return result

if __name__ == '__main__':
    main(root)