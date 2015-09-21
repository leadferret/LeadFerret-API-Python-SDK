#!/usr/local/bin/python
'''
Created on Sep 18, 2015

@author: solvire 
'''
import sys 
import requests
import json
 
# Get the total number of args passed to the demo.py
if (len(sys.argv) < 2):
    exit ("Please provide a company name")
 

base_url = "http://local.leadferret.com/public/api"
username = "steven"
password = "leadferret" 
atoken = None
company_name = str(sys.argv[1])
 
print "Hello " + username + " we will be charging you for all the employees of: " + company_name


def getheaders(token=None):
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    if(token != None):
        headers['Authorization'] = 'Bearer ' + token
    return headers


if atoken == None:
    r = requests.post(base_url + "/api-token-auth", headers=getheaders(), json={'username':username,'password':password}, verify=False)
    token = r.json()['token']
    print "Using new token: " + token 
else:
    token = atoken
    

r = requests.get(base_url + '/companies?name=' + company_name, headers=getheaders(token), verify=False)
companies = json.loads(r.text)

company_ids = [];
for company in companies['items']:
    company_ids.append(company['id'])


print "Downloading for these company IDs:"
print company_ids

if len(company) > 0:
    r = requests.get(base_url + "/contacts?company_ids=" + 
                     ','.join(str(idx) for idx in company_ids), 
                     headers=getheaders(token), verify=False)
    print "Pulled the records: "
    print r.text 

