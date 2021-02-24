import requests

headers = {"Content-Type": "application/vnd.com.asdf.nucleotide"}

with open("app.py", "rb") as f:
    requests.post("http://localhost:8001/", data=f, headers=headers)
