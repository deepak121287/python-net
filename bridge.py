import json
import requests
import urllib3
from aci_authentication_1 import login

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def bd(
    APIC,
    user,
    passwd,
    tenantName,
    vrfName,
    bdName,
    bdAlias):
    
    cookie = login(APIC,user,passwd)
    base_url = 'https://{APIC}/api/'.format(APIC=APIC)
    url_prepend = 'node/mo/uni/tn-{tenantName}/BD-{bdName}.json'.format(tenantName=tenantName,bdName=bdName)
    url = base_url + url_prepend
    headers = { 
               'content-type':'application/json',
               'connection':'keep-alive'
               }
    
    prepayload = {
        "fvBD": {
            "attributes": {
            "dn": "uni/tn-{tenantName}/BD-{bdName}".format(tenantName=tenantName,bdName=bdName),
            "mac": "00:22:BD:F8:19:FF",
            "arpFlood": "true",
            "name": "{bdName}".format(bdName=bdName),
            "nameAlias": "{bdAlias}".format(bdAlias=bdAlias),
            "rn": "BD-{bdName}".format(bdName=bdName),
            "status": "created"
            },
            "children": [
            {
                "fvRsCtx": {
                "attributes": {
                    "tnFvCtxName": "{vrfName}".format(vrfName=vrfName),
                    "status": "created,modified"
                },
                "children": []
                }
            }
            ]
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
    tenantName = 'test_tenant'
    vrfName = 'testvrf'
    bdName = 'testbd'
    bdAlias = 'testbd_alias'
    print(bd(
        apicurl,user,passwd,tenantName,vrfName,bdName,bdAlias
        ))