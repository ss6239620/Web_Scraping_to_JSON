import requests
from bs4 import BeautifulSoup as bs
import json
result1=[]
result2=[]
li=[]
dict1={}
j=0

for k in range(0,7):
    url=f"https://www.indiatoday.in/latest-headlines?page={k}"
    r=requests.get(url)
    soup=bs(r.text,'html.parser')
    result=soup.find_all('h2')
    for i in result:
        result2.append(i.string)
        # print(result2[j])
        li.append(j)
        x=dict1.setdefault(li[j-1],result2[j-1])
        j+=1

# data_json=json.dumps(dict1,indent=4)

open_file=open('personal.JSON','w')
json.dump(dict1,open_file,indent=6)