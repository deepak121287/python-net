import os
import pandas as pd
import time
from preregisternode import preRegisterNode

def registerNodes_excel(filename,user,passwd):
    file = "/home/deepaknegi/python-net/data/" +filename
    dataframe = pd.read_excel(file,sheet_name="preRegisterNode")
    # APIC	serial	nodeId	nodeName
    tab_url = list(dataframe['APIC'])
    tab_serial = list(dataframe['Serial'])
    tab_nodeId = list(dataframe['nodeId'])
    tab_nodeName = list(dataframe['nodeName'])
    for i in range(0,len(tab_url)):
        # print(str(tab_url[i]),str(tab_serial[i]),str(tab_nodeId[i]),str(tab_nodeName[i]))
        preRegisterNode(
            str(tab_url[i]),
            user,
            passwd,
            str(tab_serial[i]),
            str(tab_nodeId[i]),
            str(tab_nodeName[i]))
        time.sleep(1)
if __name__ == '__main__':
    user = 'admin'
    passwd = 'C1sco12345'
    filename = 'data.xlsx'
    registerNodes_excel(filename,user,passwd)  