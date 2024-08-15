import json
import requests # type: ignore

URL='http://127.0.0.1:8000/empinfo/'

data={
    'emp_name':'sonam',
    'emp_id':1,
    'department':'sales'
    
}
json_data=json.dumps(data)
r=requests.post(url=URL,data=json_data)
data=r.json()
print(data)

