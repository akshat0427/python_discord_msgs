import requests
import json


# to get the auth follow this https://youtu.be/xh28F6f-Cds?t=96
# copy channel ID from discord app

def retrieve_msgs(channel, auth):    
    
    l2 =[] # this string stores all the data/json abject  
    
    headers = {'authorization': auth}
    
    
    #maximum limit is 100
    r = requests.get(f'https://discord.com/api/v9/channels/{channel}/messages?limit=100', headers=headers) 
        
    l2.append(json.loads(r.text))
        
        
    
    return l2
    

l = retrieve_msgs('994258093573685328', 'NzY5MTg4Mzk1MDc4Mzg1Njc0.GJ3IhH.hcDxw6xiH8D32zlrPsPMSs0YyR5_7AGP_S0xYc')
