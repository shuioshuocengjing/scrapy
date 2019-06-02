import requests
import pandas as pd
import pprint
import json
url='https://www.autocartruck.com/umbraco/api/ServiceCenter/GetServiceCenters/?'
params={'zip': '98101','modelIdList': '1,2,3,6','truckIdList': '2,5','distance': '100'}
headers={'Accept': 'application/json, text/plain, */*',
         'Referer': 'https://www.autocartruck.com/find-service-location-distributor/',
         'Request-Context': 'appId=cid-v1:8eab6fea-89c2-4b93-acd7-84c36d3950eb',
         'Request-Id': '|cWSAa.UCE/n',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
item={'address':[],'dealer':[],'tel':[],'lat':[],'lng':[],'city':[],'DealerCode':[],'DealerTypeId': [],
      'State': [],'Zip':[]}
a=list('1230')
for i in a:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    params['zip']=i+j+k+l+m
                    html=requests.get(url,params=params,headers=headers)
                    html=html.content.decode().replace('null','" "')
                    html=eval(html)
                    for ht in html:
                        item['address'].append(ht['Address1'])
                        item['dealer'].append(ht['Name'])
                        item['tel'].append(ht['PhoneNumber'])
                        item['lat'].append(ht['Latitude'])
                        item['lng'].append(ht['Longitude'])
                        item['city'].append(ht['City'])
                        item['DealerCode'].append(ht['DealerCode'])
                        item['DealerTypeId'].append(ht['DealerTypeId'])
                        item['State'].append(ht['State'])
                        item['Zip'].append(ht['Zip'])
data=pd.DataFrame(item)
data.drop_duplicates(subset=None,keep='first',inplace=True)
data.to_csv('American.csv')