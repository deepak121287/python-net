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
    appName,
    appAlias):
    
    cookie = login(APIC,user,passwd)
    base_url = 'https://{APIC}/api/'.format(APIC=APIC)
    url_prepend = 'node/mo/uni/tn-{tenantName}/ap-{appName}.json'.format(tenantName=tenantName,appName=appName)
    url = base_url + url_prepend
    headers = { 
               'content-type':'application/json',
               'connection':'keep-alive'
               }
    
    prepayload = {
        "fvAp": {
            "attributes": {
            "dn": "uni/tn-{tenantName}/ap-{appName}".format(tenantName=tenantName,appName=appName),
            "name": "{appName}".format(appName=appName),
            "nameAlias": "{appAlias}".format(appAlias=appAlias),
            "rn": "ap-{appName}".format(appName=appName),
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
    tenantName = 'test_tenant'
    appName = 'testapp'
    appAlias = 'testapp_alias'
    print(bd(
        apicurl,user,passwd,tenantName,appName,appAlias
        ))