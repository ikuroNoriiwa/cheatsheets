import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import re
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from openpyxl import load_workbook

disable_warnings(InsecureRequestWarning)

headers = {} # TODO SITE header
url= "" # TODO Site to scrap

def get_scope_info(scope, mask):
    data = {'address': scope, 'mask': mask, 'view': 'default', 'perimeter': 'Group', 'filter': 'ALL'}
    response = requests.post(url, data=data, headers=headers, verify=False)
    soup = BeautifulSoup(response.content.decode("utf-8"), features="html.parser")

    comment = re.findall("comment...\"(.*)\",", str(soup.findAll("script")[0]))
    ip = re.findall("cidr...\"(.*)\",", str(soup.findAll("script")[0]))
    return comment, ip

def get_vip_list(vip):
    response = requests.get(url_f5 + "/resultvirtuals/{}".format(vip), headers=headers, verify=False)
    print(response)
    #print(response.content)
    soup = BeautifulSoup(response.content.decode("utf-8"), features="html.parser")
    #print(re.findall("tabswintname(.*)", str(soup.findAll("td"))))
    virtual_f5 = re.findall("showf5virtual\(\".*\"\)", str(soup.findAll("td")))
    data = []
    for i in virtual_f5:
        data.append(str(i).replace("showf5virtual(\"", "").replace('")', ''))

    print(data)
    return data

def get_vip_informations(f5virtual):
    response = requests.get(url_f5 + "/showvirtual/{}".format(f5virtual), headers=headers, verify=False)
    print(response)
    #print(response.content)
    soup = BeautifulSoup(response.content.decode("utf-8"), features="html.parser")
    list_tr = soup.findAll("tr")
    for i in list_tr:
        if "Other fallback IPs" in str(i):
            print(i)
            print(re.findall("<td class=\"text-left pl-1\">(.*)</td", str(i)))

