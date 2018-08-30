"""
Description : Export ovhcloud Pcc nsx configuration to xml file.
            : For a formated view of output file use http://www.xmlviewer.org/
Prerequisite: python3.0 or higher
            : Install requests module as it is not a builtin module(From a cmd prompt, use > Path\easy_install.exe requests, where Path is your Python*\Scripts folder, if it was installed. (For example: C:\Python32\Scripts\easy_install.exe))
            : Notepad++
Queries     : abin.francis@corp.ovh.us or abin001@gmail.com

"""

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings( InsecureRequestWarning )
import os
import getpass

s = requests.Session()
s.verify = False

def Get_EdgeConfig(vcip,username,password):
    response = s.get( vcip+'/api/4.0/edges',auth=(username, password))
    return response

vcip = input('Enter the Pcc FQDN. Eg. https:/pcc-x-x-x-x.ovh.us:')
USERNAME = input('Enter username:')
PASSWORD = getpass.getpass('Password:')

EdgeConfig = Get_EdgeConfig(vcip,USERNAME,PASSWORD)

with open('data.xml', 'w') as f:
    f.write(EdgeConfig.text)

currentPath = os.getcwd()
filepath = currentPath + "\data.xml"
print( '-' * (len(list(filepath))+16) )
print( 'File Location: ', filepath )
print( '-' * (len( list( filepath ) ) + 16) )
notepad = (r'"C:\Program Files (x86)\Notepad++\notepad++.exe" data.xml')
os.system( notepad )
exit()
