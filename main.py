import json
f=open('a.json','r',encoding='utf-8')
data=json.load(f)

for i in data:
    print(data[i])
