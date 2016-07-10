import requests
import json
from collections import OrderedDict
from datetime import datetime
#from pymongo import MongoClient

#client = MongoClient()

stopexit = [0,0,0,0,0,0]
stopentry = [0,0,0,0,0,0]
#db = client.vahana

#client = MongoClient("mongodb://mongodb0.example.net:27019")

url = 'https://api.datonis.io/api/v3/datonis_query/thing_data'

payload1 = '{"thing_key":"t1b48ta16b", "from":"2016/07/09 17:05:00", "to":"2016/07/10 17:00:00", "time_zone":"Mumbai","time_format":"str","per":"1"}'

#payload = json.loads(payload1, object_pairs_hook=OrderedDict)

headers = {'content-type': 'application/json', 'X-Access-Key' : '7tf589ff6tb86992bcdf8d9325ab39tf4be94348' }
r = requests.post(url, data=payload1, headers=headers)
print r.content
jdata = json.loads(r.content)
#print jdata
jdata1 = json.dumps(jdata)
#print "dumps"
Source = jdata["t1b48ta16b"]["event_data"][0]["data"]["Source"]
Destination = jdata["t1b48ta16b"]["event_data"][0]["data"]["Destination"]
Passenger_No = jdata["t1b48ta16b"]["event_data"][0]["data"]["Passenger_No"]
BUS_ID = jdata["t1b48ta16b"]["event_data"][0]["data"]["BUS ID"]
Ticket_Id = jdata["t1b48ta16b"]["event_data"][0]["data"]["Ticket ID"]
print "Passenger_No"
print Passenger_No
print "Destination"
print Destination
print "Source"
print Source
print "BUS_ID"
print BUS_ID
print "Ticket_Id"
print Ticket_Id

stopentry[int(Source)] = stopentry[int(Source)] + Passenger_No
print stopentry[int(Source)]


#result = db.vahana.insert_one(
    #{
    #    "route":{
    #        "bus":{
    #            "id":"",
    #            "passenger_no":"",
    #            "lat":"",
    #            "long":""
    #        }
    #    }
#
#    }
#)
#print jdata["Passenger_No"]









#curl -v -X POST -H "Content-Type:application/json" --header 'X-Access-Key:8t99cbb439bb98e719b5b14befa3d59tte9374tb' -d "{'thing_key':'t1b48ta16b', 'from':'2016/07/09 17:05:00', 'to':'2016/07/10 17:00:00', 'time_zone':'Mumbai' , 'time_format':'str', 'per':'10'}" 'https://api.datonis.io/api/v3/datonis_query/thing_data'
