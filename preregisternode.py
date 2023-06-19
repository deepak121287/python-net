import requests
import json
import urllib3
from aci_authentication_1 import login

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def preRegisterNode(
    APIC,
    user,
    passwd,
    Serial,
    nodeId,
    nodeName):
    
    cookie = login(APIC,user,passwd)
    base_url = 'https://{APIC}/api/'.format(APIC=APIC)
    url_prepend = 'node/mo/uni/controller/nodeidentpol/nodep-{Serial}.json'.format(Serial=Serial)
    url = base_url + url_prepend
    headers = { 
               'content-type':'application/json',
               'connection':'keep-alive'
               }
    
    prepayload = {
        "fabricNodeIdentP": {
            "attributes": {
            "dn": "uni/controller/nodeidentpol/nodep-{Serial}".format(Serial=Serial),
            "serial": "{Serial}".format(Serial=Serial),
            "nodeId": "{nodeId}".format(nodeId=nodeId),
            "name": "{nodeName}".format(nodeName=nodeName),
            "rn": "nodep-{Serial}".format(Serial=Serial),
            "status": "created"
            },
            "children": []
        }
    }

    
    payload = json.dumps(prepayload)
    response = requests.request(
        'POST',
        url,
        cookies=cookie,
        data=payload,
        headers=headers,
        verify=False
        )
    json_reponse = json.loads(response.text)
    print(json_reponse)
    return response.status_code




if __name__ == '__main__':
    apicurl = '10.10.20.14'
    user = 'admin'
    passwd = 'C1sco12345' 
    Serial = 'AAAAAAAAAAAA'
    nodeId = '212'
    nodeName = 'fake-leaf-212'
    print(preRegisterNode(
            apicurl,user,passwd,Serial,nodeId,nodeName
        ))