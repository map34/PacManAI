# dialog.py
# This program runs a dialog between two agents, which must be defined
# elsewhere as separate modules.

import PacMan as agentA
import IronMan as agentB
import RogerFederer as agentC

N_TURNS = 5

turn = 0
print(str(turn)+"A: "+agentA.agentName() + ': ' + agentA.introduce()+"\n")
print(str(turn)+"B: "+agentB.agentName() + ': ' + agentB.introduce()+"\n")
print(str(turn)+"C: "+agentC.agentName() + ': ' + agentC.introduce()+"\n")


remark = "Yo~"
situationA = {'Character':agentB.agentName() , 'Inside': True, 'Damage': False}
situationB = {'Character':agentA.agentName() , 'Inside': True, 'Damage': False}
situationC = {'Character':agentA.agentName() , 'Inside': False, 'Damage': False}

for i in range(N_TURNS):
    turn += 1
    if turn == 3 :
        global situationB
        situationB['Inside'] = False
        global situationC
        situationC['Inside'] = True
        global situationA
        situationA['Character'] = agentC.agentName()
    
    if turn == 4 :
        global situationC
        situationC['Damage'] = True
        global situationA
        situationA['Damage'] = True

    #If agents changed, pacMan responsed to previous agent/ghost.
    remarkA = agentA.respond(remark, situationA)
    print(str(turn)+"A: "+agentA.agentName() + ': ' + remarkA+"\n")

    remarkB = agentB.respond(remarkA, situationB)
    if remarkB != None:
        print(str(turn)+"B: "+agentB.agentName() + ': ' + remarkB+"\n")
        remark = remarkB
    remarkC = agentC.respond(remarkA, situationC)
    if remarkC != None:
        print(str(turn)+"C: "+agentC.agentName() + ': ' + remarkC+"\n")
        remark = remarkC
