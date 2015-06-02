#  a test on vim
from re import *   # Loads the regular expression module.
from random import choice # Loads the choice function from ramdom module


#These are all the maps used in the rules


CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}

DAMAGE = [", wakakakaka!! Kan pai!!(Cheers!!)",
         ". Bee Do Bee Do Bee Do!",
         "! Luk at tu!(Look at you!) HAHA!"]

INSIDE = ["Sa la ka! (How dare you!) Banana belongs to me!",
          "Baboi (Toy), you ain't gonna mess around with Minion!"]


def introduce():
   #introduction of the agent to the user
   return("""Bello! Bello! I am Minion Bob. Me want banana! Don't try
         to steal banana from me. """)

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
         
         if wordlist.count("food") > 0:
            return "Bananananana."

         if wordlist.count("suck") > 0:
            return "Poka?! (What!)"

         if wordlist.count("run") > 0 :
            return target + ", wakaka, I' ll catch you!~"

         if wordlist[0:3] == 'let me go':
            return target + "! No no no, give me banana!"

         return choice(INSIDE)

   else:
      return ("Empty string! ERROR!")

def agentName():
   'Return the name of this Agent'
   return "Minion Bob"

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



#print(respond("Hello", {'Character':"PacMan",'Inside': True, 'Damage': False}))



