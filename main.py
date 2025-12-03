from jocs import janken, endevina     


while True:                           
   print("\n--- MINI ARCADE ---")    
   print("1. Pedra, Paper, Tisora")  
   print("2. Endevinar el NÃºmero")   
   print("S. Sortir")                


   opcio = input("OpciÃ³: ").lower()  


   if opcio == "1":                  
       janken()


   elif opcio == "2":                
       endevina()


   elif opcio == "s":                
       print("AdÃ©u!")
       break                         


   else:                              
       print("OpciÃ³ no vÃ lida.")      


import random
