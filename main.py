import requests

url = 'https://script.google.com/macros/s/AKfycbwKdA7InU58sU5tVygP9-oC6L9_6INJCcp_ID6ZkHalfeRtyiAczgxjsXF-G1vMEz2GIw/exec'
data = {
    "challenge_code": "AUTOMATE123"
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print('Requisição POST bem-sucedida!')
    print('Resposta:', response.json())
else:
    print('Erro na requisição POST:', response.status_code)
    print('Resposta:', response.text)