import requests

url  = "http://localhost:5678/webhook-test/chat"
data = {"message": "What is the difference between supervised and unsupervised learning?"}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())