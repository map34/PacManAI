

from re import *   # Loads the regular expression module.
from random import choice # Loads the choice function from ramdom module


#These are all the maps used in the rules


CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}


DAMAGE = ["That was a Ace!",
         "If you wanna win, you need play harder!",
         "I fear no one."]

         

INSIDE = ["I 'll let the racket do the talking.",
          "Let's have a match."]


def introduce():
   return '''Hi, I'm Roger Federer. If you play tennis with me, you better show me what you all have.
              I will through tennis at you. '''

# Name of Agent
def agentName():
   return '''Roger Federer'''


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
            return target + ", Right after you!"
            #don't bother me,
         if wordlist.count("pellets") > 0:
            return "I can serve u more tennis ball."

         if wordlist.count("suck") > 0:
            return "We ll see about that."

         if wordlist[0:3] == 'let me go':
            return target + ", it doesn't work like that."
            #
         return choice(INSIDE)
   else:
      return ("Empty stirng! ERROR!")

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


