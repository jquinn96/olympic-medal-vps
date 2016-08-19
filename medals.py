import requests
import json

request = requests.get('http://medalbot.com/api/v1/medals')
countries = request.json()
vpsarray = []
print("Importing values...")
for country in countries:
    name = country['country_name']
    golds = country['gold_count'] * 6
    silvers = country['silver_count'] * 4
    bronzes = country['bronze_count'] * 2
    vps = golds + silvers + bronzes
    countryvps = {'country_name':name,'golds':country['gold_count'],'silvers':country['silver_count'] ,'bronzes':country['bronze_count'] ,'total_vps':vps}
    vpsarray.append(countryvps)
    
print("Imported.")

vpsarray = sorted(vpsarray, key=lambda country: country['total_vps'], reverse=True)
position = 0
lastvps = 0
result = ""
for country in vpsarray:
    if lastvps != country['total_vps']:
        position = position + 1
    result+=country['country_name']
    result+="\n"
    result+="----Position: "
    result+=str(position)
    result+="\n"
    result+="----Golds:    "
    result+=str(country['golds'])
    result+="\n"
    result+="----Silvers:  "
    result+=str(country['silvers'])
    result+="\n"
    result+="----Bronzes:  "
    result+=str(country['bronzes'])
    result+="\n"
    result+="----Total VPS "
    result+=str(country['total_vps'])
    result+="\n"
    lastvps = country['total_vps']
    
print("IOC Ladder according to VPs")
print(result)

    

