import requests
import json

#reading data
URL='http://127.0.0.1:8000/student/'
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)
    r=requests.get(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)    
    
    
get_data(1)

#Creating data

def post_data():
    data={
        'student_name':'sonam',
        'roll': 20,
        'city':'chennai'
    }
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
    
#post_data()

def update_data():
    data={
        'id':4,
        'student_name':'raj',
        'city':'goa'
    }
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)
    r=requests.put(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
#update_data()

def delete_data():
    data={
        'id':5,
    }
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
    
#delete_data()