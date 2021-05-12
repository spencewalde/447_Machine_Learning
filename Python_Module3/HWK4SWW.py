import pcn_logic_eg
import numpy as np

Xorinput = np.array([[0,0,0],[0,0,1],[0,1,0],[1,0,0],[1,0,1],[1,1,0],[0,1,1],[1,1,1]])
Xorexpected = np.array([[0], [1], [1], [0], [1], [0], [0], [1]])
NAndinput = np.array([[0,0],[0,1],[1,0],[1,1]])
NAndexpected = np.array([[1],[1],[1],[0]]) 
NotAinput = np.array([[0],[1]])
NotAexpected = np.array([[1],[0]])


p=pcn_logic_eg.pcn(Xorinput, Xorexpected)
p.pcntrain(Xorinput, Xorexpected, .25,25)
print('///////////////////END of XOR////////////////')

p=pcn_logic_eg.pcn(NAndinput, NAndexpected)
p.pcntrain(NAndinput, NAndexpected, .25,8)
print('///////////////////END of NAND////////////////')

p=pcn_logic_eg.pcn(NotAinput, NotAexpected)
p.pcntrain(NotAinput, NotAexpected, .25,5)
print('///////////////////END of NOTA////////////////')