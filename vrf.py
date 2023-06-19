import json
import requests
import urllib3
from aci_authentication_1 import login

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def vrf(
    APIC,
    user,
    passwd,
    tenantName,
    vrfName,
    vrfAlias):
    
    cookie = login(APIC,user,passwd)
    base_url = 'https://{APIC}/api/'.format(APIC=APIC)
    url_prepend = 'node/mo/uni/tn-{tenantName}.json'.format(tenantName=tenantName)
    url = base_url + url_prepend
    headers = { 
               'content-type':'application/json',
               'connection':'keep-alive'
               }
    
    prepayload = {
        "fvTenant": {
            "attributes": {
            "dn": "uni/tn-{tenantName}".format(tenantName=tenantName),
            "status": "modified"
            },
            "children": [
            {
                "fvCtx": {
                "attributes": {
                    "dn": "uni/tn-{tenantName}/ctx-{vrfName}".format(tenantName=tenantName,vrfName=vrfName),
                    "name": "{vrfName}".format(vrfName=vrfName),
                    "nameAlias": "{vrfAlias}".format(vrfAlias=vrfAlias),
                    "pcEnfPref": "unenforced",
                    "rn": "ctx-{vrfName}".format(vrfName=vrfName),
                    "status": "created"
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
    vrfAlias = 'testvrf_alias'
    print(vrf(
        apicurl,user,passwd,tenantName,vrfName,vrfAlias
        ))