""" 
	

	Link source_code: https://github.com/koalalorenzo/python-digitalocean
	Test_user 		: duclase03549@fpt.edu.vn
	api_token		: e2bdb654316334703dfa1bf42509f6b36596f71a1cd927b3635bb9574d853c75


"""


import digitalocean

#INFORMATION OF DIGITALOCEAN
###############################################################
#Access Token 

Token = "e2bdb654316334703dfa1bf42509f6b36596f71a1cd927b3635bb9574d853c75"
manager = digitalocean.Manager(token=Token)


#check information of account
def account(manager):
	print "*"*50
	print "INFORMATION OF ACCOUNT"
	print "*"*50
	Account  = manager.get_account()
	Account_all = manager.get_account_all()
	print Account
	print Account_all



#List all Regions	
def Regions(manager):
	print "*"*50
	print "INFORMATION OF REGIONS"
	print "*"*50
	a = ""	#print "  ID{:10} 	 NAME{:50}	   SLUG{:19}	DISTRIBUTION".format(a,a,a)
	List_Regions = manager.get_all_sshkeys()
	i = 0
	while i < len(List_Regions):
		print List_Regions[i]
		print "\n\n\n\n"
		i+=1
	

#List All Imange
def create():
	number =1
	data = {		
			"token":"e2bdb654316334703dfa1bf42509f6b36596f71a1cd927b3635bb9574d853c75",
           	"name":'nnips-test1',
            "region":'sgp1', # New York 2
			"image":'ubuntu-14-04-x64', # Ubuntu 14.04 x64
			"size_slug":'512mb',  # 512MB
			"backups":True
			}
	i = 0  
	while i < number:
		Create_droplet =  digitalocean.Droplet(		
				token="e2bdb654316334703dfa1bf42509f6b36596f71a1cd927b3635bb9574d853c75",
	           	name='nnips-test1',
	            region='sgp1', # New York 2
				image='ubuntu-14-04-x64', # Ubuntu 14.04 x64
				size_slug='512mb',  # 512MB
				backups=True)
		Create_droplet.create()



	return Regions(manager)

my_droplets = manager.get_all_droplets()
a = 19266620
i= 1
for a in my_droplets:
	print "%d. "%(i),a
	i+=1
id = input("> ")	
my_droplets[id].power_off()
