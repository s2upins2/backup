import requests
import getpass

import requests

user 	= raw_input("User :  ")
pwd  	= getpass.getpass("Password: ")
url = "https://cloud.digitalocean.com/login"
ck = {'user[email]': 'duclase03549@fpt.edu.vn', 'user[password]': 'anhduc95', 'commit':'Log In'}
with requests.Session() as s:
	s.post(url, data = ck)
a = requests.get("https://cloud.digitalocean.com/droplets")
content = a.text
print content