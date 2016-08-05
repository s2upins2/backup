import requests

header = {"Content-Type": "application/json","Authorization": "Bearer e2bdb654316334703dfa1bf42509f6b36596f71a1cd927b3635bb9574d853c75" }
page = requests.get("https://api.digitalocean.com/v2/account", headers = header)
print page.content
