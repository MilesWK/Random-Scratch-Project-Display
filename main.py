import scratchattach as scratch3
from random import randint
from os import name, system
def clear():
  if name == 'nt':
      _= system('cls')
print('Random Scratch Project Selector \nBy MilesWK')
project = 0
Stop = False
def getRandomId():
    return str(randint(0,9)) +str(randint(0,9)) +str(randint(0,9)) +str(randint(0,9)) +str(randint(0,9)) +str(randint(0,9)) +str(randint(0,9)) +str(randint(0,9)) +str(randint(0,9))
while True:
    while Stop == False:
        try:
            
            NewId = getRandomId()
            projectIsGenuine = True
            NewId = getRandomId()
            project = scratch3.get_project(NewId)
            shared = ''
            shared_letter =1
            print(project.title + ' by ' +project.author)
            print('-----------------------------------------------------')
            print(project.url)
            print('-----------------------------------------------------')
            print('Release Date: '+ shared)
            print('Views: '+str(project.views))
            print('Loves: '+str(project.loves))
            print('Favorites: '+str(project.favorites))
            print('Remixes: '+str(project.remix_count))
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            Stop = True
            input("press Enter for new project> ")
            Stop = False
            clear()
        except:
            NewId = getRandomId()


