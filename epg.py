import json
import requests
import urllib3
from aci_authentication_1 import login

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def epg(
    APIC,
    user,
    passwd,
    tenantName,
    bdName,
    appName,
    epgName,
    epgAlias):
    
    cookie = login(APIC,user,passwd)
    base_url = 'https://{APIC}/api/'.format(APIC=APIC)
    url_prepend = 'node/mo/uni/tn-{tenantName}/ap-{appName}/epg-{epgName}.json'.format(tenantName=tenantName,appName=appName,epgName=epgName)
    url = base_url + url_prepend
    headers = { 
               'content-type':'application/json',
               'connection':'keep-alive'
               }
    
    prepayload = {
        "fvAEPg": {
            "attributes": {
            "dn": "uni/tn-{tenantName}/ap-{appName}/epg-{epgName}".format(tenantName=tenantName,appName=appName,epgName=epgName),
            "prio": "level3",
            "name": "{epgName}".format(epgName=epgName),
            "nameAlias": "{epgAlias}".format(epgAlias=epgAlias),
            "rn": "epg-{epgName}".format(epgName=epgName),
            "status": "created"
            },
            "children": [
            {
                "fvRsBd": {
                "attributes": {
                    "tnFvBDName": "{bdName}".format(bdName=bdName),
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
    bdName = 'testbd'
    appName = 'testapp'
    epgName = 'testepg'
    epgAlias = 'testepg_alias'
    print(epg(
        apicurl,user,passwd,tenantName,bdName,appName,epgName,epgAlias
        ))