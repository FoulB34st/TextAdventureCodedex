#A terminal adventure game with multiple choices and chances at upgrading a character
import random 

base_dmg = 15 #base damage of your weapon
accuracy = 75 #how likely you are to hit something
health = 100 #your health pool
money = 75
Player_weapon = 1 #a modifier that will increase with different weapons as you find them.
PlayerDay = 1
Main_menu = 0
Event = 0

while health > 0 and Main_menu != 4:

  print('you have {HP} HP, you have ${CASH}, your weapon has a modifier of {W}x'.format(HP = health, CASH = money, W = Player_weapon))
  Main_menu = int(input('Day {D} \n What would you like to do? \n 1) Sleep \n 2) Shop \n 3) Adventure \n 4) Go back to coding \n \n '.format(D=PlayerDay)))
 
  if Main_menu == 1:
    health = health + random.randint(25, 50+PlayerDay)
    PlayerDay += 1
    print('you have sleept through the night and healed to full\n\n')

  while Main_menu == 2:
    print('\n you have $' + str(money) + ' dollars.\n ')
    ShopOptions = int(input("what would you like to buy? \n 1) Bronze Sword $100 \n 2) Iron Sword $200 \n 3) Steel Sword $400 \n 4) Big ol' Unubtainium Sword $550 \n 5) Leave \n "))
    
    if ShopOptions == 1:
      if money < 100:
        print("not enough money\n\n")
      else: 
        money -= 100
        Player_weapon = 2
        print(str(money))
        print('you now have a Bronze Sword!\n\n')

    elif ShopOptions == 2:

      if money < 200:
        print("not enough money\n\n")
      else:
        money -= 200
        Player_weapon = 3
        print(str(money))
        print('you now have a Iron Sword!\n\n')

    elif ShopOptions == 3:
      if money < 400:
        print("not enough money\n\n")
      else:
        money -= 400
        Player_weapon = 4
        print(str(money))
        print('you now have a Steel Sword!\n\n')
    
    elif ShopOptions == 4:
      if money < 550:
        print('Not enough cash!\n\n')
      else:
        money -= 550
        Player_weapon = 5
        print(str(money))
        print("you now have a Big ol' Unubtainium Sword!\n\n")
      

    elif ShopOptions == 5:
      print("I'm always here if you've got the cash! \n \n ")
      Main_menu -= 2
      

  while Main_menu == 3:
    Adventure = int(input("Are you sure you want to adventure? \n Current Gear Success Modifier: {W}, {HP} Health, and ${CASH} \n 1)Embark \n 2) Go back \n \n ".format(W = Player_weapon, HP = health, CASH = money)))
    
    if Adventure == 1:
      print("going on adventure!")
      Event += random.randint(1, 5)
      print(str(Event))

      if Event == 1:
        Bandits = int(input("You've encountered some very kind bandits on the road. They want $30 to pass through their checkpoint. \n 1) Fight \n 2) Pay \n 3) Go another way \n \n "))
        if Bandits == 1:
          print("You've engaged the Bandits in combat!")
          health = (health - random.randint(0, 25+PlayerDay))/Player_weapon
          if health > 0:
            money = money + random.randint(30, 100+PlayerDay)
            print("After the battle you were able to find some extra money for youre inconveniece you now have {HP} Health and ${CASH}.".format(HP = health, CASH = money))
            Event = 0
            Adventure = 0
        elif Bandits == 2:
          money = money - 25
          print("you've paid the bandits to pass through their checkpoint, you now have {HP} Health and ${CASH}.".format(HP = health, CASH = money))
          Event = 0
          Adventure = 0
        elif Bandits == 3:
          print("You've turned tale, and will find another way to adventure! The pride you have in your adventuring capabilities has taken negligable damage.\n \n ")
          Event = 0
          Adventure = 0
      if Event == 2:
        money = money + random.randint(10, 60)
        print("You've found a loose coin purse, someone must have lost it! you now have {HP} Health and ${CASH}.".format(HP = health, CASH = money))
        Event = 0
        Adventure = 0
      if Event == 3:
        print("You've found an oasis would you like to rest? you now have {HP} Health and ${CASH}.".format(HP = health, CASH = money))
        Oasis = int(input(" 1) Rest for the day \n 2) Push on \n \n "))
        if Oasis == 1:
          health = health + random.randint(15, 25+PlayerDay)
          PlayerDay += 1
          print('you have sleept through the night and its is day {D} youve also healed, you now have {HP}'.format(HP = health, D = PlayerDay))
          Event = 0
          Adventure = 0
        elif Oasis == 2:
          print("you've continued on with your journey.\n\n")
          Event = 0
          Adventure = 0
      if Event == 4:
        print("You've been Attacked by a pack of wolves!\n")
        health = (health - random.randint(0, 25+PlayerDay))/Player_weapon
        if health > 0:
          money = money + random.randint(10, 20)
          print("After the battle you were able to take the wolves pelts.") 
          print("A leatherworker has so conveniently walked by after you skinned the wolves! \n He is offering you money for the pelts! You now have {HP} Health and ${CASH}.\n \n ".format(HP = health, CASH = money))
          Event = 0
          Adventure = 0
      if Event == 5:
        print("You've found yourself exactly where you started. you've somehow gone in a circle! you've suffered negligable mental damage\n \n ")
        Event = 0
        Adventure = 0

    if Adventure == 2: 
      Main_menu -= 3
      
  if Main_menu == 4:
    print("Thanks for playing!")

if health <= 0:
  print("You've perished \n GAME OVER ")
else:
  print("You retired with new stories and friends. You lived happily ever after")  
