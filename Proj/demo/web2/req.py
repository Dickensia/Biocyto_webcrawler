# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:16:31 2020

@author: David
"""

def req2(seq,species,name,i,root):#species:'human' or else 
    import os    
    import selenium.webdriver as webdriver
    import requests
    #import json
    from requests_toolbelt  import MultipartEncoder
    import time
    import urllib3.contrib.pyopenssl
    urllib3.contrib.pyopenssl.inject_into_urllib3()
    #proxies = {'http': 'http://localhost:8888', 'https':'http://localhost:8888'}
    head = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Length':'1345',
        'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryirJun27ycbydqvZ4',
        'Cookie':'_ga=GA1.2.2049463369.1595379208; _gid=GA1.2.540023763.1595379208; _gat=1',
        'Host':'crispr.cos.uni-heidelberg.de',
        'Origin':'https://crispr.cos.uni-heidelberg.de',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Referer': 'https://crispr.cos.uni-heidelberg.de/',
        'Sec-Fetch-Dest':'document',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-Site':'same-origin',
        'Sec-Fetch-User':'?1'
        }
    form_data = {'name': name,
             'radQ': 'single',
             'sequence': seq,#query sequence
             'pamType': 'NGG-NRG',#pam-type
             'targetLength': '20',
             'sgRNA5': 'NN',
             'sgRNA3': 'NN',
             'inVitroTx': 'T7',
             'totalMismatches': '4',
             'useCore': 'on',
             'coreLength': '12',
             'coreMismatches': '2',
             'species': 'hg38' if species == 'human' else 'mm10'#mm10 for mouse
             }

    m = MultipartEncoder(form_data,boundary='----WebKitFormBoundaryirJun27ycbydqvZ4')
    response = requests.post(url='https://crispr.cos.uni-heidelberg.de/cgi-bin/search.py', data = m,headers=head,verify=False)

    r_url = response.url.split('=')[-1]
    time.sleep(3)
    
    # head2 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'Accept-Encoding':'gzip, deflate, br',
    #     'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6',
    #     'Connection':'keep-alive',
    #     'Cookie':'_ga=GA1.2.2049463369.1595379208',
    #     'Host':'crispr.cos.uni-heidelberg.de',
    #     'Upgrade-Insecure-Requests':'1',
    #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',       
    #     'Sec-Fetch-Dest':'document',
    #     'Sec-Fetch-Mode':'navigate',
    #     'Sec-Fetch-Site':'none',
    #     'Sec-Fetch-User': '?1'
    #     # 'If-Modified-Since': 'Wed, 29 Jul 2020 05:37:08 GMT',
    #     # 'If-None-Match': '"74ce-5ab8df25ac14c"'
    #     } 
    # head2 = {'Upgrade-Insecure-Requests': '1',
    #          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
#https://crispr.cos.uni-heidelberg.de/result/fa46264f433515752e2a9272a8ee83848b00de37/unnamed.xls
    #response2 = requests.get(url='https://crispr.cos.uni-heidelberg.de/result/'+r_url+'/'+form_data['name']+'.xls',verify=False)
    # print(response2)
    option =  webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': root+'web1files\\'}
    option.add_experimental_option('prefs', prefs)
    chrome = webdriver.Chrome(chrome_options=option)
    try:
        os.remove(root+'web1files\\'+name+'.xls')
    except FileNotFoundError:
        pass
    chrome.get('https://crispr.cos.uni-heidelberg.de/result/'+r_url+'/'+form_data['name']+'.xls')
    time.sleep(5)
    try:
        os.remove(root+'web1files\\'+name+'.xls')
    except FileNotFoundError:
        pass
    chrome.close()
    
    
    option =  webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': root+'web1files\\'}
    option.add_experimental_option('prefs', prefs)
    chrome = webdriver.Chrome(chrome_options=option)
    try:
        os.remove(root+'web1files\\'+name+'_'+species+'_'+str(i)+'.xls')
    except FileNotFoundError:
        pass
    chrome.get('https://crispr.cos.uni-heidelberg.de/result/'+r_url+'/'+form_data['name']+'.xls')
    #time.sleep(4)
    # try:
    #     os.rename(root+'web1files\\'+name+'.xls',root+'web1files\\'+name+'_'+species+'_'+str(i)+'.xls')
    # except FileNotFoundError:
    #     time.sleep(4)
    #     os.rename(root+'web1files\\'+name+'.xls',root+'web1files\\'+name+'_'+species+'_'+str(i)+'.xls')
    starttime = time.time()
    while os.path.exists(root+'web1files\\'+name+'.xls') != True:
        if (round(time.time() - starttime, 2)<20):
            time.sleep(1)
        else:
            break
    try:
        with open(root+'web1files\\'+name+'.xls','r') as r:
            content = r.readlines()[17:-1]
            with open(root+'web1files\\'+name+'_'+species+'_'+str(i)+'.xls','w') as w:
                for c in content:
                    w.write(c)
                w.close()
            r.close()
        os.remove(root+'web1files\\'+name+'.xls')
        #os.rename(root+'web1files\\'+name+'.xls',root+'web1files\\'+name+'_'+species+'_'+str(i)+'.xls')
    except FileNotFoundError:
        pass
    chrome.close()
    
    # f2=open(root+'web1files//'+name+species+'_'+str(i)+'.xls','r+')
    # f2.close
# if __name__ == '__main__':
#     req2()
       
        