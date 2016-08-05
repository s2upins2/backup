from sys import exit
from random import randint
import digitalocean
import os
import time
import getch

global clear
global Token
global manager
Token = "e2bdb654316334703dfa1bf42509f6b36596f71a1cd927b3635bb9574d853c75"
manager = digitalocean.Manager(token = Token)
clear = lambda: os.system('clear')

# fix name => engine
class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()
#FIX

class Screen(Scene):

    def enter(self):
        clear() # clear screen in terminal
        print "Logging......"
        Account = manager.get_account()
        clear()
        print "You're logging on:" ,Account
    	print "DigitalOcean Management:"
    	print "\t1. Information."
    	print "\t2. Config Droplet."
        print "\t0. Exit"
        action = raw_input("> ")

        if action == "1":
            return 'info'
        elif action == "2":
            return 'config'
        elif action == "0":
            clear()
            print "Bye !"
            time.sleep(1)
            exit()
        else :
            print "Wrong Please try again !"
            time.sleep(1)
            return 'screen'
            
class Information(Scene):

    def enter(self):
        clear()
        print "INFORMATION"
        print "\t1. Information of Account."
        print "\t2. Information of All Droplets."
        print "\t3. Information of All Images. "
        print "\t4. Information of All Regions."
        print "\t0. Back"
        choose = raw_input("> ")       
        
        if choose == "1":
            return 'account'
        elif choose == "2":
            return "droplets" 
        elif choose == '3':
            return 'image' 
        elif choose == '4':
            return 'region'
        elif choose == '0':
            return 'screen'
        else :
            print "Wrong Please try again !"
            time.sleep(1)
            return 'info'
    
class Config(Scene):

    def enter(self):
        clear()
        print "CONFIG"
        print "\t1. Create Droplets"
        print "\t2. Droplets Action (ON/OFF/RESTART/DEL)"
        print "\t3. Show List SSH key "
        print "\t0. Back"
        choose = raw_input("> ")


        if choose =="1":
            return "create"
        elif choose == "2":
            return "action"
        elif choose == "3":
            return "show"
        elif choose == "0":
            return "screen"
        else :
            print "Wrong Please try again !"
            time.sleep(1)
            return 'config'

 
class Account(Scene):

    def enter(self):
        clear()
        print "*"*50
        print "Information of Account"
        print  "*"*50
        all_account=manager.get_account_all()
        
       
        print all_account
        time.sleep(1)
        getch.pause()  #Press any key
        return  'info'


class Droplets(Scene):

    def enter(self):
        clear()
        print "*"*50
        print "Information of Droplets"
        print "*"*50
        a = ""
        print "No  ID    {:15}NAME       {:20}IP          {:20}Status".format(a,a,a)
        droplets = manager.get_all_droplets()
        i = 0
        while i < len(droplets):
            print "%d. "%(i+1),droplets[i]
            i+=1
        time.sleep(1)
        getch.pause()  #Press any key
        return 'info'

class Image(Scene):

    def enter(self):
        clear()
        print "*"*50
        print "List Images"
        print "*"*50
        print "\n\n"
        a = ""
        print "  ID{:10}   NAME{:50}    SLUG{:10}              OS      ".format(a,a,a)
        print "="*120
        images = manager.get_all_images()
        i = 0
        while i < len(images):
            print images[i]
            i+=1 
        time.sleep(1)
        getch.pause()  #Press any key
        return 'info'
class Region(Scene):

    def enter(self):
        clear()
        print "*"*50
        print "List Regions"
        print "*"*50
        a=""
        print "Name{:20}  Slug{:15}  Available".format(a,a)
        print "="*60
        region = manager.get_all_regions()
        i = 0
        while  i< len(region):
            print region[i]
            i+=1
        time.sleep(1)
        getch.pause()  #Press any key
        return 'info'



# 2 CONFIG  

class Create(Scene):

    def enter(self):
        clear()
        tokens="e2bdb654316334703dfa1bf42509f6b36596f71a1cd927b3635bb9574d853c75"
        regions='sgp1'
        images='ubuntu-14-04-x64'
        size_slugs='512mb'
        ssh_keys =  "2315109,2315110"
        backups1=True
        print "Default Config"
        print "\tToken: {}\n\tRegion: {}\n\tImage: {}\n\tSize: {}\n\tSSH_KEY: {}\n\tBackups: {}".format(tokens,regions,images,size_slugs,ssh_keys,backups1)
        

        print "How many Droplets?"
        no = input("> ")
        if no == 0:
            return 'config'
        else :
            print "Do you want create %d droplets. Yes/No" %(no)
            choose = raw_input("> ")
            choose = choose.lower()


            if choose == "yes" :
                i = 0
                print "Name: "
                name_input= raw_input(">")
                print "Create %d droplets , with name %s and default config, Yes/No"%(no,name_input)
                confirm = raw_input("> ")
                confirm = confirm.lower()

                if confirm == "yes":
                    i = 0  
                    while i < no:
                        Create_droplet =  digitalocean.Droplet(     
                            token= tokens,
                            name="{}-{}".format(name_input,i),
                            region= regions, # New York 2
                            image=images, # Ubuntu 14.04 x64
                            size_slug=size_slugs,  # 512MB
                            ssh_keys = [2315109,2315110],
                            backups=backups1
                            )
                        Create_droplet.create() 
                        actions = Create_droplet.get_actions()
                        for action in actions:
                            action.load()
        # Once it shows complete, droplet is up and running
                        print action.status
                        i+=1   
                    return 'config'
                else :
                    return 'config'
            else:
                return "config"

class Droplets_action(Scene):

    def enter(self):
        clear()
        i=1
        a = ""
        print "Droplets Action:"
        print "No  ID    {:15}NAME       {:20}IP          {:20}Status".format(a,a,a)
        my_droplets = manager.get_all_droplets()
        

        for a in my_droplets:
            print "%d. "%(i),a
            i+=1
        print "Choose Action: "
        print "\t1. Turn on"
        print "\t2. Turn off"
        print "\t3. Restart"
        print "\t4. Delete"
        print "\t0. Back"
        choose = raw_input("> ")


        if choose == "1":
            print "Turn On:\nPlz! Enter No  .\nOr Enter 0 for ALL! "
            press = input("> ")
            if press == 0:
                print "Turn on....\nSure that Status of every Droplets is Off"
                for drop in my_droplets:
                    drop.power_on() 
            else :
                my_droplets[press-1].power_on()


        if choose == "2":
            print "Turn Off:\nPlz! Enter No  .\nOr Enter 0 for ALL! "
            press = input("> ")


            if press == 0:
                print "Turn off....\nSure that Status of every Droplets is On"
                for drop in my_droplets:
                    drop.power_off() 
            else :
                my_droplets[press-1].power_off()           



        if choose == "3":
            print "Reboot:\nPlz! Enter No  .\nOr Enter 0 for ALL! "
            press = input("> ")

            if press == 0:
                print "Turn off....\nSure that Status of every Droplets is On"
                for drop in my_droplets:
                    drop.reboot() 
            else :
                my_droplets[press-1].reboot()


        if choose == "4":
            print "Delete:\nPlz! Enter No  .\nOr Enter 0 for ALL! "
            press = input("> ")

            if press == 0:
                print "Delete ALL! Are you sure! Yes/No? "
                confirm = raw_input("> ")
                confirm = confirm.lower()

                if confirm == "yes":
                    print "Turn off....\nSure that Status of every Droplets is On"
                    for drop in my_droplets:
                        drop.destroy() 

                else : 
                    return 'action'

            else :
                print "Delete \n[%s]\n Are you sure ! Yes/No?"%my_droplets[press-1]
                confirm = raw_input("> ")
                confirm = confirm.lower()
                if confirm == "yes":
                    my_droplets[press-1].destroy()
                else :
                    return 'action'            
        if choose == "0":
            return 'config'

        time.sleep(1)
        getch.pause()        
        return 'config'
class Show(Scene):

    def enter(self):
        clear()
        print "*"*50
        print "List SSH Key"
        print "*"*50
        list_ssh = manager.get_all_sshkeys()
        i = 0
        while i < len(list_ssh):
            print list_ssh[i]
            print "\n\n\n"
            i+=1
        time.sleep(1)
        getch.pause()        
        return 'config'    

 


class Map(object):

    scenes = {
        'screen': Screen(),
        #Menu 
        'info'  : Information(),
        'config': Config(),
        #function
        'account': Account(),
        'droplets': Droplets(),
        'image' : Image(),
        'region': Region(),


        'create': Create(),
        'action': Droplets_action(),
        'show' : Show()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('screen')
a_game = Engine(a_map)
a_game.play() 