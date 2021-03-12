# Stanca Aurelian Rares - 324 CB - Noiembrie 2020
# 
# Pentru step efectiv impart tot inputul in stari, tranzitii all of that si dupa
# incep sa fac un step din TM cu toate if-urile alea. M-am folosit de secventele
# alea de if-uri si la accept() si la k_accept(). Most def era cel mai curat sa
# folosesc step() si nu ca dai copy paste mindlessly.
# Ca sa faca doar un step folosesc break & la final mai folosesc si o variabila
# found ca sa verific daca a fost gasit in tabelul de tranzitii sau nu.
# 
# More or less aceleasi chestii si la accept()/k_accept() 
# 
# 
# Feedback: usoara tema dar super misto - 7 hours max.

import re # Regex pentru replace
import sys 

def readTM(TM):
    for i in range(0, len(TM)):
        TM[i] = TM[i].replace('\n', '')
    # Get rid de '\n'-uri
    return TM

def step(TM): # Step
    listaStari = TM[1].split()
    TMStari = TM[4:]
    for i in range(0, len(TMStari)):
        j = list(TMStari[i].split(" "))
        
    cuvinte = TM[1].split(' ')
    
    for i in range(0, len(cuvinte)):
        cuvinte[i] = re.split(r'[,()]', cuvinte[i])
        cuvinte[i].pop(0) # Get rid of spatii goale
        cuvinte[i].pop()
    
    for i in range(len(cuvinte)):
        found = 0
        
        for j in range(len(TMStari)):
            k = list(TMStari[j].split(" "))
            
            if cuvinte[i][1] == k[0] and cuvinte[i][2][0] == k[1]:
                found = 1
                
                cuvinte[i][1] = cuvinte[i][1].replace(cuvinte[i][1], k[2])
                cuvinte[i][2] = cuvinte[i][2].replace(cuvinte[i][2][0], k[3], 1)
                
                if k[4] == 'L':
                    if len(cuvinte[i][0]) == 1:
                        cuvinte[i][2] = cuvinte[i][0][-1] + cuvinte[i][2]
                        cuvinte[i][0] = '#'
                    else:
                        cuvinte[i][2] = cuvinte[i][0][-1] + cuvinte[i][2]
                        cuvinte[i][0] = cuvinte[i][0][:-1]
                elif k[4] == 'R':
                    if len(cuvinte[i][2]) == 1:
                        cuvinte[i][0] = cuvinte[i][0] + cuvinte[i][2][0]
                        cuvinte[i][2] = '#'
                    else:
                        cuvinte[i][0] = cuvinte[i][0] + cuvinte[i][2][0]
                        cuvinte[i][2] = cuvinte[i][2].replace(cuvinte[i][2][0], '', 1)

                break
        if found == 0:
            cuvinte[i][1] = cuvinte[i][1].replace(cuvinte[i][1], 'X')
    
    # Folosesc variabila found ca sa vad daca exista o tranzitie pentru starea
    # respectiva. Daca nu exista schimb
    
    for i in range(len(cuvinte)):
        if i != (len(cuvinte) - 1):
            if cuvinte[i][1] != 'X':
                print("(" + cuvinte[i][0] + "," + cuvinte[i][1] + "," + cuvinte[i][2] + ")", end=' ')
            else:
                print("False", end=' ')
        else:
            if cuvinte[i][1] != 'X':
                print("(" + cuvinte[i][0] + "," + cuvinte[i][1] + "," + cuvinte[i][2] + ")", end='')
            else:
                print("False", end='')

def accept(TM): #ACCEPT
    listaStari = TM[1].split()
    TMStari = TM[4:]
    for i in range(0, len(TMStari)):
        j = list(TMStari[i].split(" "))
        
    cuvinte = TM[1].split(' ')
    
    stariFinale = TM[3].split(' ')
    
    for i in range(0, len(cuvinte)):
        cuvinte[i] = re.split(r'[,()]', cuvinte[i])
    
    for i in range(len(cuvinte)):
        cuvinte[i].append('0')
        cuvinte[i].append('#')
        cuvinte[i].reverse()
    
    for i in range(len(cuvinte)):
        found = 1
        ok = 0
        while 1:
            if found == 0:
                cuvinte[i][1] = cuvinte[i][1].replace(cuvinte[i][1], 'X')
                break
            
            for k in range(len(stariFinale)):
                if stariFinale[k] == cuvinte[i][1]:
                    cuvinte[i][1] = cuvinte[i][1].replace(cuvinte[i][1], 'Y')
                    ok = 1
                    break
                    # Y - accepta
                    # X - n-accepta
            
            if ok == 1:
                break
            
            found = 0
                
            for j in range(len(TMStari)):
                k = list(TMStari[j].split(" "))
                
                if cuvinte[i][1] == k[0] and cuvinte[i][2][0] == k[1]:
                    found = 1 # Daca a gasit starea coresp cuvantului
                    
                    cuvinte[i][1] = cuvinte[i][1].replace(cuvinte[i][1], k[2])
                    cuvinte[i][2] = cuvinte[i][2].replace(cuvinte[i][2][0], k[3], 1)
                    
                    if k[4] == 'L':
                        if len(cuvinte[i][0]) == 1:
                            cuvinte[i][2] = cuvinte[i][0][-1] + cuvinte[i][2]
                            cuvinte[i][0] = '#'
                        else:
                            cuvinte[i][2] = cuvinte[i][0][-1] + cuvinte[i][2]
                            cuvinte[i][0] = cuvinte[i][0][:-1]
                    elif k[4] == 'R':
                        if len(cuvinte[i][2]) == 1:
                            cuvinte[i][0] = cuvinte[i][0] + cuvinte[i][2][0]
                            cuvinte[i][2] = '#'
                        else:
                            cuvinte[i][0] = cuvinte[i][0] + cuvinte[i][2][0]
                            cuvinte[i][2] = cuvinte[i][2].replace(cuvinte[i][2][0], '', 1)
    for i in range(len(cuvinte)):
        if i != (len(cuvinte) - 1):
            if cuvinte[i][1] != 'X':
                print("True", end=' ')
            else:
                print("False", end=' ')
        else:
            if cuvinte[i][1] != 'X':
                print("True", end ='')
            else:
                print("False", end='')
                
def k_accept(TM): #KACCEPT
    listaStari = TM[1].split()
    TMStari = TM[4:]
    for i in range(0, len(TMStari)):
        j = list(TMStari[i].split(" "))
        
    cuvinte = TM[1].split(' ')
    
    stariFinale = TM[3].split(' ')
    
    for i in range(0, len(cuvinte)):
        cuvinte[i] = re.split(r'[,]', cuvinte[i])
    
    for i in range(len(cuvinte)):
        cuvinte[i].reverse()
        
    for i in range(len(cuvinte)):
        cuvinte[i].append('0')
        cuvinte[i].append('#')
        cuvinte[i].reverse()
    
    for i in range(len(cuvinte)):
        found = 1
        ok = 0
        
        for n in range(0, int(cuvinte[i][3])):
            for k in range(len(stariFinale)):
                if stariFinale[k] == cuvinte[i][1]:
                    cuvinte[i][1] = cuvinte[i][1].replace(cuvinte[i][1], 'Y')
                    ok = 1
                    break
                
            if ok == 1:
                break
            
            if found == 0:
                cuvinte[i][1] = cuvinte[i][1].replace(cuvinte[i][1], 'X')
                print(stariFinale, cuvinte[i][1])
                break
            
            found = 0
                
            for j in range(len(TMStari)):
                k = list(TMStari[j].split(" "))
                
                if cuvinte[i][1] == k[0] and cuvinte[i][2][0] == k[1]:
                    found = 1 # Daca a gasit starea coresp cuvantului
                    
                    cuvinte[i][1] = cuvinte[i][1].replace(cuvinte[i][1], k[2])
                    cuvinte[i][2] = cuvinte[i][2].replace(cuvinte[i][2][0], k[3], 1)
                    
                    if k[4] == 'L':
                        if len(cuvinte[i][0]) == 1:
                            cuvinte[i][2] = cuvinte[i][0][-1] + cuvinte[i][2]
                            cuvinte[i][0] = '#'
                        else:
                            cuvinte[i][2] = cuvinte[i][0][-1] + cuvinte[i][2]
                            cuvinte[i][0] = cuvinte[i][0][:-1]
                    elif k[4] == 'R':
                        if len(cuvinte[i][2]) == 1:
                            cuvinte[i][0] = cuvinte[i][0] + cuvinte[i][2][0]
                            cuvinte[i][2] = '#'
                        else:
                            cuvinte[i][0] = cuvinte[i][0] + cuvinte[i][2][0]
                            cuvinte[i][2] = cuvinte[i][2].replace(cuvinte[i][2][0], '', 1)
                    break
    
            if found == 0 or ok == 1:
                break
            
        for k in range(len(stariFinale)):
            if stariFinale[k] == cuvinte[i][1]:
                cuvinte[i][1] = cuvinte[i][1].replace(cuvinte[i][1], 'Y')
                ok = 1

    for i in range(len(cuvinte)):
        if i != (len(cuvinte) - 1):
            if cuvinte[i][1] == 'Y':
                print("True", end=' ')
            else:
                print("False", end=' ')
        else:
            if cuvinte[i][1] == 'Y':
                print("True", end ='')
            else:
                print("False", end='')
        
input = sys.stdin.readlines()

TM = readTM(input)

if TM[0] == "step":
    step(input)
elif TM[0] == "accept":   
    accept(input)
elif TM[0] == "k_accept":
    k_accept(input)