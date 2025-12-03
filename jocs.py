#Joc 1


import random             
def janken():             
   opcions = ["pedra", "paper", "tisora"]  


   vict_us = 0           
   vict_robot = 0        


   for _ in range(3):       # Bucle que es repetirÃ  3 rondes
       usuari = input("Tria (pedra/paper/tisora): ").lower() 
       robot_tria = random.choice(opcions)                   


       print("El robot tria:", robot_tria)                   


       if usuari == robot_tria:                              
           print("Empat")


       elif (usuari == "pedra" and robot_tria == "tisora") or \
            (usuari == "paper" and robot_tria == "pedra") or \
            (usuari == "tisora" and robot_tria == "paper"):  
           print("Guanyes la ronda!")
           vict_us += 1                                      


       else:                                                 
           print("El robot guanya la ronda!")
           vict_robot += 1                                   


   if vict_us > vict_robot:
       print("Has guanyat la partida!")                     
   elif vict_robot > vict_us:
       print("El robot ha guanyat la partida!")              
   else:
       print("Empat final!")                                 




#Joc 2


import random


def Endevinar():
   numero = random.randint(1,100)
   intents = 0


   print("He pensat un nÃºmero entre 1 i 100.")


   while True:
       usuari = int(input("Introdueix un nÃºmero:"))
       intents += 1


       if usuari < numero:
           print("Massa baix.")
       elif usuari > numero:
           print("Massa alt.")
       else:
           print("Correcte!!")
           break
