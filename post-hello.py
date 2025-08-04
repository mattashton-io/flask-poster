import requests

response = requests.post("http://127.0.0.1:5001/post-hello?password=123xyz", data={})
print(response)
#print(response.text)