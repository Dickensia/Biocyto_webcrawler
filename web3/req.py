# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 17:10:40 2020

@author: David
"""


# head = {':authority': 'wge.stemcell.sanger.ac.uk',
#         ':method': 'GET',
#         ':path': '/api/search_by_seq?seq=GCACTGTCCCTAATACACTG&pam_right=2&get_db_data=1&species=Mouse',
#         ':scheme': 'https',
#         'accept': 'application/json, text/javascript, */*; q=0.01',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6',
#         'cookie': '__utmc=140298677; __utmz=140298677.1595379205.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); wge_session=5cd811dbc7c6f06efc3ae2db45738ab7798d7948; __utma=140298677.1797524009.1595379205.1595379205.1595396432.2; __utmt=1; __utmb=140298677.7.10.1595396432',
#         'referer': 'https://wge.stemcell.sanger.ac.uk/search_by_seq',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
#         'x-requested-with': 'XMLHttpRequest'}
def compute(html):
    #import time
    #import json
    import requests
    import re
    pattern2=re.compile(r"(\d+:\d+-\d+)")
    coord= re.findall(pattern2, html)[0]
    left = int(coord.split(':')[1].split('-')[0])
    right = int(coord.split(':')[1].split('-')[1])
    chr = coord.split(':')[0]
    # params3 = {'chr':chr,
    #        'start':str(right-500),
    #        'end':str(right+500)}
    # url4 = "https://wge.stemcell.sanger.ac.uk/api/crisprs_in_region?chr=%(chr)s&start=%(start)s&end=%(end)s&assembly=GRCm38&species_id=Mouse&design_id=&crispr_filter=&flank_size=" %params3
    # coord_map = requests.get(url4).text
    params2 = {'species': 'Mouse',
           'start_coord': str(left),
           'end_coord': str(right),
           'chromosome_number': chr,
           'assembly_id': 'GRCm38',
           'all_singles': '1'
           }
    url3 = 'https://wge.stemcell.sanger.ac.uk/api/region_off_target_search?species=%(species)s&start_coord=%(start_coord)s&end_coord=%(end_coord)s&chromosome_number=%(chromosome_number)s&assembly_id=%(assembly_id)s&all_singles=%(all_singles)s' %params2
    requests.get(url3)


def req3(seq,name,i,root):
    import time
    import json
    import requests
    import re
    params = {'seq': seq[:-3],
          'pam_right': '2',#'NGG':'2','NAG':'1'
          'get_db_data': '1',
          'species': 'Mouse'}

    url = 'https://wge.stemcell.sanger.ac.uk/api/search_by_seq?'
    response = requests.get(url=url+"seq=%(seq)s&pam_right=%(pam_right)s&get_db_data=%(get_db_data)s&species=%(species)s" %params)
    #https://wge.stemcell.sanger.ac.uk/crispr/468661457
    res_dict = json.loads(response.text)[0]
    url2 =  "https://wge.stemcell.sanger.ac.uk/crispr/%(id)s" %res_dict
    response2 = requests.get(url2)
    html = response2.text
    pattern1 = re.compile(r'<td class="seq">(\w+)</td>') #og seq not included
    seqlist = re.findall(pattern1,html)
    if len(seqlist) == 0:
        compute(html)
        time.sleep(2)
        response2 = requests.get(url2)
        response2 = requests.get(url2)
        time.sleep(2)
        response2 = requests.get(url2)
        html = response2.text
        pattern1 = re.compile(r'<td class="seq">(\w+)</td>') #og seq not included
        seqlist = re.findall(pattern1,html)
    with open(root+'web2files\\'+name+'_mouse_'+str(i)+'.csv','w') as o:
        for s in seqlist:
            #['-']*5+[s[:-3]]+[s[-3:]]+['-']*5
            o.write(('\t').join(['-']*5+[s[:-3]]+[s[-3:]]+['-']*5)+'\n')
        o.close()
    return seqlist
