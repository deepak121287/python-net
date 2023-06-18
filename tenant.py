import json
import requests
import urllib3
from aci_authentication_1 import login

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def tenant(
    APIC,
    user,
    passwd,
    tenantName,
    tenantAlias):
    
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
                "name": "{tenantName}".format(tenantName=tenantName),
                "nameAlias": "{tenantAlias}".format(tenantAlias=tenantAlias),
                "rn": "tn-{tenantName}".format(tenantName=tenantName),
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
    tenantAlias = 'test_tenant_alias'
    print(tenant(
        apicurl,user,passwd,tenantName,tenantAlias
        ))