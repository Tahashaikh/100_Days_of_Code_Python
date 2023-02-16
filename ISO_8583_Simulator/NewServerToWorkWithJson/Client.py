import requests

url = "http://localhost:8080/stub/testing"
method = "GET"
headers = {
    "Content-Type": "text/plain"
}

response = requests.request(method, url, headers=headers)

print(response.text)