import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def login(apicurl,user,passwd):
    base_url = 'https://{apicurl}/api/'.format(apicurl=apicurl)
    p_payload = {'aaaUser': 
                        {'attributes': 
                            {
                                'name': '{user}'.format(user=user),
                                'pwd': '{passwd}'.format(passwd=passwd)
                            }
                        }
                }
    payload = json.dumps(p_payload)
    url = base_url + 'aaaLogin.json'
    headers = { 
        'content-type':'application/json'
        }
    try:
        response = requests.request(
            'POST',
            url,
            headers=headers,
            data=payload,
            timeout=2,
            verify=False)
        data = json.loads(response.text)
        token = {}
        token["APIC-Cookie"]=data["imdata"][0]["aaaLogin"]["attributes"]["token"]
        return token
    except:
        print("Error Occurred")

if __name__ == '__main__':
    apicurl = '10.10.20.14'
    user = 'admin'
    passwd = 'C1sco12345'
    print(login(apicurl,user,passwd))

