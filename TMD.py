print("Running : requests")
import requests

url = "http://data.tmd.go.th/api/WeatherToday/V1/"

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "63cad96b-461e-4396-b9b5-d678080c2d03"
    }

response = requests.request("GET", url, data=payload, headers=headers)
print("Running : response.json")
#print(response.text)
data = response.json()
#print(type(data))
print("Running : dict")
dict_1=data
#print(data.keys())
#print(data['Stations'])
#print(type(dict_1['Stations']))
#print(len(dict_1['Stations']))
#print(dict_1['Stations'])
#print(dict_1['Stations'][0])
#print(dict_1['Stations'][0].keys())
#print(dict_1['Stations'][0]['Observe'].keys())
#print(dict_1['Stations'][0]['Observe']['Rainfall'])
#print(dict_1['Stations'][0]['Observe']['Rainfall'].keys())
#print(dict_1['Stations'][0]['Observe']['Rainfall']['Value'])
#print(dict_1['Stations'][0]['Observe']['Temperature']['Value'])
#list_branch_name=[]
#for item in dict_1['Stations']:
#    list_branch_name.append(item['StationNameTh'])
#print(list_branch_name)
print("Running : pandas")
import pandas as pd
df1 = pd.DataFrame()
list_branch_name=[]
for item in dict_1['Stations'] :
            list_branch_name.append(item['StationNameTh'])
df1['name']=list_branch_name

list_lat=[]
for item in dict_1['Stations'] :
            list_lat.append(item['Latitude']['Value'])
df1['lat'] = list_lat

list_long=[]
for item in dict_1['Stations'] :
           list_long.append(item['Longitude']['Value'])
df1['long'] = list_long

list_Rain=[]
for item in dict_1['Stations'] :
           list_Rain.append(item['Observe']['Rainfall']['Value'])
df1['rain'] = list_Rain

list_Temp=[]
for item in dict_1['Stations'] :
           list_Temp.append(item['Observe']['Temperature']['Value'])
df1['temp'] = list_Temp

list_Time=[]
for item in dict_1['Stations'] :
           list_Time.append(item['Observe']['Time'])
df1['time'] = list_Time
print("Running : to_csv")
#print(df1)
df1.to_csv('C:/Users/sattawat.a/Desktop/Python/TMD/bbbbddddd.csv')