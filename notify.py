import json,requests

data = {
    "subject": "dataware house",
    "grade": "A"
        
}

url = 'http://128.199.212.108/jf-shop/api/v1/grade'
headers = {'content-type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)