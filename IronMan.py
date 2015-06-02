

from re import *   # Loads the regular expression module.
from random import choice # Loads the choice function from ramdom module


#These are all the maps used in the rules


CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}

DAMAGE = ["I am the one and only IronMan. Hahahaha!",
         "Don't let me catch you again!",
         "JARVIS, calculate! Let's get ready for next attack."]

         

INSIDE = ["JARVIS, we have an intruder!",
          "How dare you wander around in my private property!"]


def introduce():
    return '''Hi, I'm Iron Man. If you try to get into my private property,
            I will bomb you!'''

# Name of Agent
def agentName():
    return '''Iron Man'''


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
      if situation['Inside'] == True :
         target = situation['Character']
         if situation['Damage'] == True :
            return choice(DAMAGE)
             #get away, run, 
         if wordlist.count("run") > 0 :
           return target + ", I can fly!"
         #don't bother me, 
         if wordlist[0:3] == 'let me go':
           return "Oh, U can't escape from me."

         if wordlist.count("food") > 0:
            return "Want some bullets?"

         if wordlist.count("suck") > 0:
            return "How dare you?"
         
         return choice(INSIDE)
   else:
      return ("Empty string! ERROR!")

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




#print(respond("Hello", {'Character':"PacMan",'Inside': True, 'Damage': True}))


