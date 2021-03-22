import time
import random

print("Hello, player. You are about to enter a game. You are to find wounder soldiers on the battlefield and you will have to either heal them or bring them to safety.")

ready = input("Are you ready to begin? ")

print(" ")

bandageRolls = 10
stretchersAvaliable = 10
truamaLevel = 5/100
energyLevel = 100/100
rescuedSoldiers = 0/15

status = ("Bandages left: " + str(bandageRolls) + "; Strechers avaliable: " + str(stretchersAvaliable) + "; Truama level: " + str(truamaLevel) + "; energyLevel: " + str(energyLevel) + "; soldiers rescued: " + str(rescuedSoldiers))

#To bandage soldier or to bring soldier to temorary camp, you need to have a soldier first; so I'm not going to add that yet. 

if(ready =='yes' or 'Yes' or 'yeah'):
  startTime = time.time()
  print("You have a few choices. In the next screen click 'A' for a status check; type 'B' for a rest; enter 'C' to call for backup; click 'D' to eat or drink; enter 'E' to check for wounded soldiers, or type 'F' to quit")
  print(" ")
  userOption = input("So, which is it? A, B, C, D, E, or F? Keep in mind that every second you waste may be the second between life and death for a soldier on the battlefield. ")
 while(userOption == 'A'):
    print("You have choosen to check your status")
    print(status)
    userOption = input(("Please choose what to do next. You can choose A, B, C, D, E, or F. Scroll up if you've forgotten which letter represents which action. "))
 while(userOption == 'B'):
    print("You have choosen to rest.")
    truamaLevel -= 10 
    energyLevel += 10
    userOption = input(("Please choose what to do next. You can choose A, B, C, D, E, or F. Scroll up if you've forgotten which letter represents which action. "))
    if(userOption == 'A'):
      print(status)
      userOption = input(("Please choose what to do next. You can choose A, B, C, D, E, or F. Scroll up if you've forgotten which letter represents which action. "))
 while(userOption == 'C'):
    print("You have choosen to call for backup")
    backup = random.randint(1,2)
    if(backup == 1):
      print("Backup is nearby. They are here to assist you.")
      assitance = input("How would you like them to assist you? ")
      if(assitance != 'yay'):
        print("They shall help")
    else:
      print("I'm afraid there is no backup nearby.")
    userOption = input(("Please choose what to do next. You can choose A, B, C, D, E, or F. Scroll up if you've forgotten which letter represents which action. "))
    if(userOption == 'A'):
      print(status)
      userOption = input(("Please choose what to do next. You can choose A, B, C, D, E, or F. Scroll up if you've forgotten which letter represents which action. "))
    if(userOption == 'B'):
      print("You have choosen to rest.")
      energyLevel += 10
      truamaLevel -+ 10
 while(userOption == 'D'):
    print("You have choosen to replenish your energy")
    energyLevel += 10 
    userOption = input(("Please choose what to do next. You can choose A, B, C, D, E, or F. Scroll up if you've forgotten which letter represents which action. "))
    if(userOption == 'A'):
      print(status)
      userOption = input(("Please choose what to do next. You can choose A, B, C, D, E, or F. Scroll up if you've forgotten which letter represents which action. "))
    if(userOption == 'B'):
     print("You have choosen to rest.")
    energyLevel += 10
    truamaLevel -+ 10
    userOption = input(("Please choose what to do next. You can choose A, B, C, D, E, or F. Scroll up if you've forgotten which letter represents which action. "))
    if(userOption == 'C'):
      print("You have choosen to call for backup")
    backup = random.randint(1,2)
    if(backup == 1):
      print("Backup is nearby. They are here to assist you.")
      assitance = input("How would you like them to assist you? ")
      if(assitance != 'yay'):
        print("They shall help")
    else:
      print("I'm afraid there is no backup nearby.")
    userOption = input(("Please choose what to do next. You can choose A, B, C, D, E, or F. Scroll up if you've forgotten which letter represents which action. "))
 while(userOption == 'E'):
    soldiersNearby = random.randint(1,4)
    enemiesNearby = random.randint(1,5)
    if(soldiersNearby == 1 or 2 or 3):
      print("There is a soldier nearby that you need to rescue! ")
      if(enemiesNearby == 1 or 2 or 3):
        print("However, there are also enemy soldiers nearby.")
      yN = input("Will you go try to rescue that soldier?")
      if(yN == 'yes' or 'Yes' or "yea"):
        hurtPossibility = random.randint(1,6)
        print("He seems to need bandages.")
        useBandages = input("Are you going to use bandages? ")
        if(useBandages == 'yes' or 'Yes' or 'yea'):
          if(hurtPossibility == 1):
            print("You got shot from an enemy! You need help quickly!")
            energyLevel -= 50
            hurtBackup = input("Will you call for backup?")
            if(hurtBackup == "yes" or "Yes" or "yea"):
              print("You have been taken to an infirminary and have healed; however, the soldier you were trying to rescue has passed.")
              energyLevel += 60
              truamaLevel -= 10
          print("He is healed!")
          bandageRolls -= 1
          rescuedSoldiers +=1
          truamaLevel -= 10
        else:
          print("You have failed to save the soldier.")
          truamaLevel += 10
      else:
        print("You have failed to save the soldier.")
        truamaLevel += 10
    userOption = input(("Please choose what to do next. You can choose A, B, C, D, E, or F. Scroll up if you've forgotten which letter represents which action. "))
    if(userOption == 'A'):
      print(status)
      userOption = input(("Please choose what to do next. You can choose A, B, C, D, E, or F. Scroll up if you've forgotten which letter represents which action. "))
    if(userOption == 'B'):
     print("You have choosen to rest.")
    energyLevel += 10
    truamaLevel -+ 10
    userOption = input(("Please choose what to do next. You can choose A, B, C, D, E, or F. Scroll up if you've forgotten which letter represents which action. "))
    if(userOption == 'C'):
      print("You have choosen to call for backup")
    backup = random.randint(1,2)
    if(backup == 1):
      print("Backup is nearby. They are here to assist you.")
      assitance = input("How would you like them to assist you? ")
      if(assitance != 'yay'):
        print("They shall help")
    else:
      print("I'm afraid there is no backup nearby.")
    userOption = input(("Please choose what to do next. You can choose A, B, C, D, E, or F. Scroll up if you've forgotten which letter represents which action. "))
    if(userOption == 'D'):
      print("You have choosen to replenish your energy")
    energyLevel += 10 
    userOption = input(("Please choose what to do next. You can choose A, B, C, D, E, or F. Scroll up if you've forgotten which letter represents which action. "))
 while(userOption == 'F'):
    print("You have choosen to quit. Thank you for playing!") 
    break
 while(userOption != 'A' or 'B' or 'C' or "D" or "E" or "F"):
    print("I'm afraid that's an unvalid option. Please choose again.")
    userOption = input("Would you like to choose A, B, C, D, E, or F? ")
  
if(rescuedSoldiers == 15):
  print("CONGRATS!! YOU HAVE RESCUED 15 SOLDIERS AND HAVE WON THE GAME!")
  endTime = time.time()
  print("Plus it only took you " + str((endTime - startTime)/60) + " minutes!" )

if(truamaLevel > 100/100):
  print("You have lost the game. Your truama level is too high. Try again next time.")

if(truamaLevel > 80/100):
  hR = input("You are starting to hallucinate. Would you like to sit down to rest? ")
  if(hR == 'yes' or 'Yes'):
    print("You are not hallicinating as much anymore.")
    truamaLevel -= 20

if(energyLevel < 0/100):
  print("You have expended too much energy, passed out, and got shot from enemies. Try again next time.")

if(hurtBackup == 'no' or 'No' or 'nope'):
  print("You have died from your wound. Better luck next time.")