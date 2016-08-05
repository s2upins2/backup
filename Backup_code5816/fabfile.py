from fabric.api import *
from fabric.api import hide, run, get
import digitalocean
import json
import sys
token = "1777439007ca7a858130c4afc855ddd4a5b8f50943bb4edd0613eeef1ab708cc"
def create(tag_name,no):
	with hide('running'):
		i = 0
		while i < int(no):
			name = "%s-%s"%(tag_name,i)
			#Create Droplet
			a = local("curl -X POST -H \"Content-Type: application/json\" -H \"Authorization: Bearer %s\" -d '{\"name\":\"%s\",\"region\":\"sgp1\",\"size\":\"512mb\",\"image\":\"ubuntu-14-04-x64\",\"ssh_keys\":[\"2479056\"],\"backups\":false,\"ipv6\":false,\"user_data\":null,\"private_networking\":null,\"volumes\": null}' \"https://api.digitalocean.com/v2/droplets\" "%(token,name),capture = True)
			dict = json.loads(a)
			drop_id = dict["droplet"]["id"]
			#Create and add TAGs
			local("curl -X POST -H 'Content-Type: application/json' -H \"Authorization: Bearer %s\" -d '{\"name\":\"%s\"}' \"https://api.digitalocean.com/v2/tags\""%(token,name))
			local("curl -X POST -H 'Content-Type: application/json' -H \"Authorization: Bearer %s\" -d '{\"resources\":[{\"resource_id\":%d,\"resource_type\":\"droplet\"}]}' \"https://api.digitalocean.com/v2/tags/%s/resources\" "%(token,drop_id,name))
			i+=1

def Del():
	local("curl -X GET -H \"Content-Type: application/json\" -H \"Authorization: Bearer %s\" \"https://api.digitalocean.com/v2/droplets?page=1&per_page=1\" "%(token))
	print "Enter Droplets to Delete:"
	tags = raw_input("> ")
	with hide('running'):
		local("curl -X DELETE -H \"Content-Type: application/json\" -H \"Authorization: Bearer %s\" \"https://api.digitalocean.com/v2/droplets?tag_name=%s\" "%(token,tags))

def Del_all():
	with hide('running'):
		a = local("curl -X GET -H \"Content-Type: application/json\" -H \"Authorization: Bearer %s\" \"https://api.digitalocean.com/v2/droplets?page=1&per_page=1\" "%(token),capture = True)
		dict = json.loads(a)
		info = dict["droplets"][0]['tags']
		i = 0
		while i < len(info):
			print "delete %s"%info[i]
			local("curl -X DELETE -H \"Content-Type: application/json\" -H \"Authorization: Bearer %s\" \"https://api.digitalocean.com/v2/droplets?tag_name=%s\" "%(token,info[i]))
			i+=1

def test():
	with hide('running'):
		local("ls -la")

def del_tag(tag_name):
	with hide('running'):
		local("curl -X DELETE -H 'Content-Type: application/json' -H \"Authorization: Bearer %s\" \"https://api.digitalocean.com/v2/tags/%s\""%(token,tag_name)) 



def del_tag_all():
	with hide('running'):
		a = local("curl -X GET -H \"Authorization: Bearer %s\" \"https://api.digitalocean.com/v2/tags\""%token,capture=True)
	 	tag = json.loads(a)
	 	tag_name = tag['tags']
	 	i = 0
	 	while i < len(tag_name):
	 		local("curl -X DELETE -H 'Content-Type: application/json' -H \"Authorization: Bearer %s\" \"https://api.digitalocean.com/v2/tags/%s\""%(token,tag_name[i]['name']))
	 		i+=1


