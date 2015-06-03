

from re import *   # Loads the regular expression module.
from random import choice # Loads the choice function from ramdom module


#These are all the maps used in the rules

CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}

DAMAGE = ["Ouch, that hurts!",
          "Stop taking my food!",
          "Yo! You ain't gonna catch me again!",
          "I gotta run!"]

HIDE = ["I am faster than you.", 
         "I want my food!",
         "Woohoo, let's have fun",
         "Too bad you suck!",
         "I m running at lightspeed!",
         "Let me go!"]


def introduce():
   #introduction of the agent to the user
   return("Yo! I am FatBoy")

punctuation_pattern = compile(r"\,|\.|\?|\!|\;|\:")    


#example: situation = {'Character':"PacMan",'Inside': False, 'Damage': False, 'Skill': False}
# a sitution map shows the game state of last move

def respond(inputLine, situation) :
   # remove punctuation
   wordlist = split(' ', remove_punctuation(inputLine))
   # undo any initial capitalization:
   wordlist[0]=wordlist[0].lower()
   mapped_wordlist = you_me_map(wordlist)
   mapped_wordlist[0]=mapped_wordlist[0].capitalize()

   if wordlist[0] != '' :
      #default conversation with ms.pacman only
      target = situation['Character']
      
      #Minion---------------------------------------------------------------------
      if wordlist.count("banana") > 0 :
         # a minion
         return (target + ", I don't wanna ur banana, I just want my food.")
      if wordlist.count("Baboi") > 0:
         return (target + ", What did u just call me?")
      if wordlist.count("Bee") > 0:
         return (target + ", no more Jiberish!")

      
      #Federer---------------------------------------------------------------------
      if wordlist.count("tennis") > 0 :
         return(target + ", don't hit me with ur tennis ball!")

      if wordlist.count("match") > 0 :
         return(target + ", I ain't play a tennis match with u")

      if wordlist.count("Ace") > 0 :
         return(target + ", You got lucky on that one.")

      if wordlist.count("racket") > 0 :
         return (target + ", let me get my food!")

      #Lynch-----------------------------------------------------------------------
      if wordlist.count("skittles") >0 :
         return(target + ", skittles won't help u!")
      
      if wordlist.count("Beast") > 0:
         return(target + "you scared me!")
      
      #IronMan----------------------------------------------------------------------
      if wordlist.count("JARVIS") > 0 :
         return(target + ", it's not fair that you have JARVIS")
      
      if wordlist.count("property") > 0 :
         return (target + ", you are such a rich man.")

      #General analysis on input response--------------------------------------------
      if situation['Damage'] == True:
         return choice(DAMAGE)
      
      if wordlist.count("catch") > 0 or wordlist.count("caught")>0 :
         return ("Oh no, leave me alone!") 

      return choice(HIDE)
   else:
      return ("Empty stirng! ERROR!")

def agentName():
   'Return the name of this Agent'
   return "FatBoy"

def you_me(w):
   'Changes a word from 1st to 2nd person or vice-versa.'
   try:
      result = CASE_MAP[w]
   except KeyError:
      result = w
   return result

def you_me_map(wordlist):
   'Applies YOU-ME to a whole sentence or phrase.'
   return [you_me(w) for w in wordlist]

def remove_punctuation(text):
   'Returns a string without any punctuation.'
   return sub(punctuation_pattern,'', text)

def stringify(wordlist):
   'Create a string from wordlist, but with spaces between words.'
   return ' '.join(wordlist)


