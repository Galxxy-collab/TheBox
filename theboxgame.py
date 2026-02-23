'''
-------------------------------------------------------------------------------
Name:  main.py
Purpose: The box is a text based adventure game that requires the user to think outside the box. Doing this will result in winning. This is my CPT for Grade 11, computer science.
 
Author:   Eric A.
 
Created:  05/12/2022
------------------------------------------------------------------------------
'''
# library imports (for stoping time, typing one character at a time, and coloured text)
import time
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init()

# code used to make each character type at a certain speed (0.1 seconds) as well as loading the game for the user
def write(wel_loading, speed=0.1):
  for char in wel_loading:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(speed)
  print("")

# loading for the game
wel_loading = "Loading..."
write(wel_loading)
time.sleep(2)

# this function is used to sleep time for 1 second
def times():
  time.sleep(1)

# dev note (When the first input statment appears, if you write lvl and then the number of the level you wish to go to, it will take you straight to that level. The only exception is lvl1 since you can simply right "yes" to go there.)
# show a logo to the game and introduce the inspiration for the game
the_box = "\n𝑻𝒉𝒆 𝑩𝒐𝒙"
write(the_box)
times()
backrooms = "\n𝑰𝒏𝒔𝒑𝒊𝒓𝒆𝒅 𝒃𝒚 𝒕𝒉𝒆 𝑩𝒂𝒄𝒌𝒓𝒐𝒐𝒎𝒔"
write(backrooms)
times()

# level 1 (The user first gets a glimpse of the box. They then have the choice between grabbing an item or not.)
times()
def lvl1():
  times()
  lev1_text1 = "\nAh the box, what a wonderful place"
  write(lev1_text1)
  dots = "..."
  write(dots)
  times()
  lev1_text2 = "not really."
  write(lev1_text2)
  times()
  obj1_text = "Ooo looks like I see something shiny\nI wonder what it could be...\nMaybe an iPhone 6?"
  write(obj1_text)
  times()
  obj1_text2 = "highly doubt that."
  write(obj1_text2)
  times()
  obj1 = input("\nShould I grab this item?: (y/n) ")

  if obj1 == "y":
    print(Fore.GREEN+"You recived an iPhone 6!",Fore.RESET)
  elif obj1 == "n":
    print(Fore.RED+"I'll just walk past it then.",Fore.RESET)

  while obj1 != "y" and obj1 != "n":
    print("That's invalid, try again.")
    obj1 = input("\nShould I grab this item?: (y/n) ")
    if obj1 == "y":
      print(Fore.GREEN+"You recived an iPhone!",Fore.RESET)
    elif obj1 == "n":
      print(Fore.RED+"I'll just walk past it then.",Fore.RESET)
  times()

# room 1 in level 1 (This leads the user back to where they first started)
  def room1():
    def rint1():
      r1_exit = "Oh it's a hole in the ground.\nThis might be my chance to escape.\nDon't care I'm risking it!!!"
      write(r1_exit)
      times()
      r1_exitF = "Dam I'm back at the start.\nMan wt--"
      write(r1_exitF)
      times()
      lvl1()

    # if the user answers "n", they move on
    room1_text1 = "\nWell where do I go now..."
    write(room1_text1)
    room1_text2 = "I think there's only one option which is  straight.\nBut who knows..."
    write(room1_text2)
    times()
    room1_input1 = input("\nShould I enter this room (y/n)?: ")

    if room1_input1 == "y":
      enter_room1 = "Alright, let's enter the room!"
      write(enter_room1)
      rint1()
  
    elif room1_input1 == "n":
      turn_around1 = "I'm gonna turn around."
      write(turn_around1)
      lvl2()
      
    while room1_input1 != "y" and room1_input1 != "n":
      print("That's invalid.")
      room1_input1 = input("Should I enter this room or go back (y/n)?: ")
      if room1_input1 == "y":
        print("Alright, let's enter the room!")
        rint1()
      elif room1_input1 == "n":
        print("I'm gonna turn around.")
  room1()

# level 2 (This is the hardest level in the box. There are 5 doors that each have different descions in them. Door 1 leads to death by snakes, door 2 is a room full of fortnite kids with the only way getting out is to crank 90s given by the hint. Door 3 and 4 are exactly the same both leading to death and descions. And finally door 5 is the bed room which both options lead to death. Now if the user enters 6, they loom up to find a hole in the roof as a ladder comes down to get them to the next level. Lots of if, elif, and else statements were used.)
def lvl2():
  times()
  lev2_text1 = "\nLooks like that was right.\nThere's a second door, guess imma go in it."
  write(lev2_text1)
  times()
  lev2_text2 = "There is 5 different doors.\nThis be mad confusing."
  write(lev2_text2)
  times()
  lev2_desi1 = int(input("\nWhich door do I go in?: "))

  if lev2_desi1 == 1:
    door1 = "\nWhy is there so many snakes!"
    write(door1)
    door1_text2 = "OH No AHHH"
    write(door1_text2)
    time.sleep(2)
    print(Fore.RED+"YOU DIED",Fore.RESET)
    exit()

  elif lev2_desi1 == 2:
    door2 = "\nThis big red door seems like the right option"
    write(door2)
    times()
    dots2 = "..."
    write(dots2)
    times()
    door2_text1 = "Why is there a bunch of fortnite kids cranking like crazy.\nWish I was back in the 90s."
    write(door2_text1)
    times()
    door2_des = input("\nWhat should I do to the kids? (hit them or join them): ")
    door2_des_low = door2_des.lower()
    if door2_des_low == "hit them":
      revenge1 = "It's time to get my revenge after all these years!!"
      write(revenge1)
      times()
      revenge1_text1 = "Oh no LOOKS LIKE THEY'RE TURNING ON ME!!!"
      write(revenge1_text1)
      time.sleep(2)
      print(Fore.RED+"YOU DIED",Fore.RESET)
      exit()
    elif door2_des_low == "join them":
      sweat1 = "Let me ask them if I can join"
      write(sweat1)
      times()
      dots3 = "..."
      write(dots3)
      times()
      sweat2 = "They agreed on one condition."
      write(sweat2)
      sweat3 = "I have to beat them in a 1v1."
      write(sweat3)
      sweat4 = input("Do I accept the 1v1 offer? (y/n): ")
      sweat4_low = sweat4.lower()
      if sweat4_low == "y":
        sweat5 = "Alr let's see how this goes."
        write(sweat5)
        time.sleep(3)
        sweat6 = "So, I lost..."
        write(sweat6)
        times()
        sweat7 = "Now they're making me go back where I came from and they called me a l-l-loser :("
        write(sweat7)
        sweat8 = "Now I gotta go back to the doors..."
        write(sweat8)
        lvl2()
      elif sweat4_low == "n":
        sweat9 = "They're asking me to go back where I came from."
        write(sweat9)
        sweat10 = "Guess I have no choice..."
        write(sweat10)
        lvl2()
    elif door2_des_low == "cranking 90s":
      sweat11 = "I'm so good at this shi"
      write(sweat11)
      times()
      sweat_item = "looks like they're giving me something"
      write(sweat_item)
      times()
      print(Fore.GREEN+"You recieved a keyboard!",Fore.RESET)
      times()
      sweat12 = "Woah looks like that was good.\nNow I'm in the third room."
      write(sweat12)
      lvl3()
    else:
     invalid1_door2 = "Invalid response gotta retry..."
     write(invalid1_door2)
     lvl2()

  elif lev2_desi1 == 3 or lev2_desi1 == 4:
    door3_4 = "\nThis looks like a good option"
    write(door3_4)
    door3_text1 = "Ooo looks like there's an item on the ground for me to grab!"
    write(door3_text1)
    times()
    print(Fore.GREEN+"You recieved a Apple TV!",Fore.RESET)
    door3_text2 = "Huh an Apple Tv, I have no idea what imma do with this.\nGuess I'll just keep it in my pocket for now."
    write(door3_text2)
    times()
    door3_option = input("Should I continue going forward?: ")
    door3_lower = door3_option.lower()
    if door3_lower == "yes":
      door3_yes = "Alright imma go forward.\nOh no looks like there's some kind of creature.\nTHERE IS NO ESCAPE!"
      write(door3_yes)
      time.sleep(2)
      print(Fore.RED+"You Died.",Fore.RESET)
      exit()
    elif door3_lower == "no":
      door3_no = "Guess imma go back."
      write(door3_no)
      times()
      door3_no1 = "Wait why is there only one door now."
      write(door3_no1)
      door3_no2 = "Guess I'm going to go in it."
      write(door3_no2)
      times()
      door3_no3 = "Wait there's a sign.\nIt says turn around."
      write(door3_no3)
      dots4 = "..."
      write(dots4)
      door3_no4 = "Uh oh."
      write(door3_no4)
      time.sleep(2)
      print(Fore.RED+"You Died.",Fore.RESET)
      exit()
    else:
      door3_invalid1 = "Invalid response. Die"
      write(door3_invalid1)
      print(Fore.RED+"You Died.",Fore.RESET)
      exit()
  elif lev2_desi1 == 5:
    door5_text1 = "\nI should open up door 5 cause it's lucky."
    write(door5_text1)
    door5_text2 = "Looks like there's a bunch of beds\nNow that I mention it, I'm kinda feeling tired.\nMaybe I should rest on the bed."
    write(door5_text2)
    times()
    door5_option = input("Should I sleep?(flip the bed/sleep): ")
    door5_lower = door5_option.lower()
    if door5_lower == "flip the bed":
      door5_flip1 = "Alright imma flip the bed."
      write(door5_flip1)
      print("3")
      times()
      print("2")
      times()
      print("1")
      times()
      door5_flip2 = "FLIPPP!!!"
      write(door5_flip2)
      times()
      door5_flip3 = "Looks like there's a knife.\nImma try to pick it up."
      write(door5_flip3)
      time.sleep(2)
      door5_flip4 = "I... uh .... go-t-t ... stabb-ed"
      write(door5_flip4)
      time.sleep(2)
      print(Fore.RED+"You Died.",Fore.RESET)
      exit()
    elif door5_lower == "sleep":
      door5_sleep1 = "Well time to go to bed."
      write(door5_sleep1)
      time.sleep(2)
      door5_sleep2 = "COUPLE HOURS LATER"
      write(door5_sleep2)
      time.sleep(2)
      door5_sleep3 = "Ah that was a good rest.\nWell guess imma go back through that door.\nWait what happened to the door.\nWhy's it gone.\nWHERE DO I GO!"
      write(door5_sleep3)
      time.sleep(2)
      print(Fore.RED+"You drove yourself insane.",Fore.RESET)
      exit()
    else:
      door5_invalid = "Invalid response. This time there is no right answer."
      write(door5_invalid)
      exit()
  elif lev2_desi1 == 6:
    lvl2_up1 = "Oh looks like there's a hole in the roof."
    write(lvl2_up1)
    times()
    lvl2_up2 = "Oh now a ladder's coming down.\nWell despite my gut telling me no, it's better to risk it then to not go at all."
    write(lvl2_up2)
    times()
    climbing1 = "climbing..."
    write(climbing1)
    dots5 = "..."
    write(dots5)
    times()
    lvl2_up3 = "Woah looks like that was good.\nNow I'm in the third room."
    write(lvl2_up3)
    lvl3()
  else:
    invalid_lvl2 = "That's not a number.\nTry again."
    write(invalid_lvl2)
    lvl2()

# level 3 (The user enters a huge parking garage with no cars. Their first two options are to stay put or explore. Staying put will result in death. Exploring the user will find 2 doors. Both doors eventually lead to death. Therefore the correct option is straight which leads to an elevator. Anytime the user enters something invalid, it will either lead to death or they may retry.)
def lvl3():
  times()
  lvl3_text1 = "\nWow now that a big parking garage.\nBut I can barely see anything."
  write(lvl3_text1)
  times()
  dots6 = "..."
  write(dots6)
  times()
  lvl3_text2 = "I think I might go and explore.\nLet's go find if there's a way outa here."
  write(lvl3_text2)
  explore1 = input("\nShould I explore or stay put?: ")
  explore1_lower = explore1.lower()
  if explore1_lower == "explore":
    explore2 = "Alright lets go explore."
    write(explore2)
    explore3 = "Seems like there's no cars here..."
    write(explore3)
    times()
    dots7 = "..."
    write(dots7)
    time.sleep(2)
    explore4 = "Looks like there's two doors.\nI'm tempted to go in them."
    write(explore4)
    explore5 = int(input("Which door do I go into? (1,2 or 3 to continue): "))
    if explore5 == 1:
      explore6 = "Imma open door 1.\nWhy is there a snake choking out a whale...\nI hope it doesn't attack me!"
      write(explore6)
      times()
      explore7 = "AHHH IT's LUnGing At mEEeeEe!"
      write(explore7)
      time.sleep(2)
      print(Fore.RED+"YOU DIED.",Fore.RESET)
      exit()
    elif explore5 == 2:
      explore8 = "Imma open door number 2.\nWhy is there a sign saying 'rem was here'\nSeems to be strange."
      write(explore8)
      times()
      explore9 = "I'm starting to feel some chest pain.\nImma go back."
      write(explore9)
      times()
      explore10 = "couple hours later..."
      write(explore10)
      explore11 = "T-th-is ch-es-t pa-in is un-ber-r-r-r-r-ribleeee"
      write(explore11)
      time.sleep(2)
      print(Fore.RED+"YOU DIED.",Fore.RESET)
      exit()
    elif explore5 == 3:
      explore12 = "Alright I'll look past the doors.\nLet's continue exploring."
      write(explore12)
      time.sleep(2)
      explore13 = "Looks like there's an elevator.\nImma go in it to see if that's the exit!!"
      write(explore13)
      times()
      explore14 = "Ok so the doors just closed...\nOh looks like there's two options.\nWe go to floor 6 or go to floor 10."
      write(explore14)
      lvl4()
    else:
      explore15 = "Invalid.\nYOU MUST RETRY!"
      write(explore15)
      time.sleep(5)
      lvl3()
  elif explore1_lower == "stay put":
    stay_put1 = "\nAlright im gonna stand here."
    write(stay_put1)
    times()
    stay_put2 = "Wait...what was that sound..."
    write(stay_put2)
    times()
    stay_put3 = "There it is again!"
    write(stay_put3)
    time.sleep(2)
    stay_put4 = "WAIT WHATS THAT AHHHH!!!!!!"
    write(stay_put4)
    time.sleep(2)
    print(Fore.RED+"You got smooshed by a 20 by 10 foot boulder(thomp).",Fore.RESET)
    exit()
  else:
      explore15 = "Invalid.\nYOU MUST DIE!"
      write(explore15)
      time.sleep(5)
      print(Fore.RED+"You died for being dumb",Fore.RESET)
      exit()

# level 4 (The user can choose from 2 different floors, floor 6 and floor 10. Floor 6 leads to your nans house. If the user explores downstairs, they die to your nan. If the user stays still then goes upstairs, then they find a portal and go on to the next level. Same concept applies to floor 10 except now it's travis scott's house. If the user ever enters something invalid, they either retry or die.)
def lvl4():
  times()
  lvl4_desi = int(input("\nWhich floor should I choose? (6 or 10): "))
  if lvl4_desi == 6:
    floor6_text1 = "\nAlright let's go to floor 6."
    write(floor6_text1)
    times()
    floor6_text2 = "\nOk seems like the doors are opening."
    write(floor6_text2)
    times()
    floor6_text3 = "That looks like an old house.\nI guess I have no choice but to head inside."
    write(floor6_text3)
    times()
    floor6_text4 = "This is such a nice wooden door.\nNeeds some work tho.\nThis place seems pretty big but there's only one way to find out."
    write(floor6_text4)
    def explore6():
      times()
      floor6_explore = input("\nShould we explore? (yes/no): ")
      floor6_ex_lower = floor6_explore.lower()
      if floor6_ex_lower == "yes":
        floor6_explore1 = "Okay time to explore."
        write(floor6_explore1)
        times()
        floor6_explore2 = "This floor feels a little moist but imma go to the kitchen."
        write(floor6_explore2)
        times()
        floor6_explore3 = "Wait IS THAT MY NAN!!\nOh no that's a big issue.\nSHES GONNA KILL ME!"
        write(floor6_explore3)
        time.sleep(2)
        print(Fore.RED+"You died to ur nan.",Fore.RESET)
        exit()
      elif floor6_ex_lower == "no":
        floor6_ex_no1 = "\nOkay, I'm staying right here then."
        write(floor6_ex_no1)
        times()
        floor6_ex_no2 = "Wait I just heard something upstairs.\nImma go check that out cause honestly at this point,\nI'm down for anything."
        write(floor6_ex_no2)
        times()
        floor6_ex_no3 = "OMG IT'S A PORTAL\nLET'S GOOOOO!!!"
        write(floor6_ex_no3)
        lvl5()
      while floor6_ex_lower != "yes" and floor6_ex_lower != "no":
        floor6_invalid1 = "Invalid response. Must try again."
        write(floor6_invalid1)
        explore6()
    explore6()
  elif lvl4_desi == 10:
    floor10_text1 = "\nAlright let's go to floor 10."
    write(floor10_text1)
    times()
    floor10_text2 = "\nOk seems like the doors are opening."
    write(floor10_text2)
    times()
    floor10_text3 = "\nThat looks like a mansion.\nI guess I have no choice but to head inside."
    write(floor10_text3)
    times()
    floor10_text4 = "This is such a nice golden door.\nNeeds some work tho.\nThis place seems pretty big but there's only one way to find out."
    write(floor10_text4)
    def explore10():
      floor10_explore = input("\nShould we explore? (yes/no): ")
      floor10_ex_lower = floor10_explore.lower()
      if floor10_ex_lower == "yes":
        floor10_explore1 = "\nOkay time to explore."
        write(floor10_explore1)
        times()
        floor10_explore2 = "This floor feels crazy good.\nIt even has diamonds in it."
        write(floor10_explore2)
        times()
        floor10_explore3 = "Wait IS THAT TRAVIS SCOTT!!\nOh no that's a big issue.\nHE's got the BATMAN SUIT!\n I'M GONNA DIE!"
        write(floor10_explore3)
        time.sleep(2)
        print(Fore.RED+"You died to travis lol.",Fore.RESET)
        exit()
      elif floor10_ex_lower == "no":
        floor10_ex_no1 = "\nOkay, I'm staying right here then."
        write(floor10_ex_no1)
        times()
        floor10_ex_no2 = "\nWait I just heard something upstairs.\nImma go check that out cause honestly at this point,\nI'm down for anything."
        write(floor10_ex_no2)
        times()
        floor10_ex_no3 = "OMG IT'S A PORTAL\nLET'S GOOOOO!!!"
        write(floor10_ex_no3)
        lvl5()
      while floor10_ex_lower != "yes" and floor10_ex_lower != "no":
        floor10_invalid1 = "Invalid response. Must try again."
        write(floor10_invalid1)
        explore10()
    explore10()
  else:
    lvl4_invalid = "\nYou know what I'm actually gonna be nice to you.\nInstead of dying, your gonna just retry okay?\nAlright I don't want to you see you back here."
    write(lvl4_invalid)
    times()
    lvl4()

# level 5 (After the user exits the portal, they enter a type of Antartic place that's currently in a blizzard. The user either has the option to go into a cave or continue exploring. If the user continues exploring, they eventualy freeze to death but with an introduction to Invalid Man who becomes mentioned again later. If the user enters the cave, they become warmer but now have the option to light a campfire. If the user doesn't light the campfire, they die for being too cold. If the user lights the campfire, they get warm and recieve a jacket. Then they get another portal for the next level. If the user enters something Invalid, they meet Invalid Man and will most likely die.)
def lvl5():
  times()
  lvl5_text1 = "\nAh finally out the portal."
  write(lvl5_text1)
  dots9 = "..."
  write(dots9)
  times()
  lvl5_text2 = "I-t's f-f-f-freezing here."
  write(lvl5_text2)
  lvl5_text3 = "Looks like I end-d-ed up in a s-s-snowstorm.\nI should have d-d-estroyed the portal.\nLet me go f-f-find s-s-s-helter."
  write(lvl5_text3)
  times()
  lvl5_text4 = "L-l-looks like there's a-a cave."
  write(lvl5_text4)
  times()
  lvl5_desi = input("Should I enter the cave? (yes or no): ")
  lvl5_lower = lvl5_desi.lower()
  if lvl5_lower == "yes":
    cave1 = "Alright l-l-et's enter t-t-the cave."
    write(cave1)
    times()
    cave2 = "\nAh it's a bit better in here.\nOoo looks like there's a campfire."
    write(cave2)
    times()
    campfire1 = input("Should I light the fire? (yes or no): ")
    if campfire1 == "yes":
      campfire2 = "Okay let's light the fire."
      write(campfire2)
      time.sleep(2)
      campfire3 = "\nAhh that's so much warmer.\nProb shouldn't have worn short sleves today but,\ndidn't know that I'd end up in Antartica.\nI should find a way out of this place.\nLooks like so far everythings been random.\nWho knows, maybe that's the way to escape."
      write(campfire3)
      times()
      campfire4 = "I think it's time to leave the cave.\nOh what's this?"
      write(campfire4)
      times()
      print(Fore.GREEN+"You recived an jacket!",Fore.RESET)
      campfire5 = "This should keep me warm now."
      write(campfire5)
      times()
      campfire6 = "What another portal.\nWhat are the odds the obvious was right this time."
      write(campfire6)
      times()
      lvl6()
    if campfire1 == "no":
      campfire7 = "Alright then no campfire."
      write(campfire7)
      time.sleep(2)
      campfire8 = "couple hours later..."
      write(campfire8)
      time.sleep(2)
      campfire9 = "Maybe I-I-I should've l-l-lit t-t-that c-c-campfire."
      write(campfire9)
      times()
      print(Fore.RED+"You died for being too cold.",Fore.RESET)
      exit()
    while campfire1 != "yes" and campfire1 != "no":
      campfire10 = "Last time was the last warning for retries.\nFurther more there is nothing else I can do.\nTherefore you will not continue."
      write(campfire10)
      times()
      print(Fore.RED+"Invalid man is gone...",Fore.RESET)
      exit()
  if lvl5_lower == "no":
    no_cave1 = "W-w-well I think n-n-o cave is b-b-better."
    write(no_cave1)
    time.sleep(5)
    no_cave2 = "Hey there, you probably don't know me but,\nI'm invalid m-"
    write(no_cave2)
    time.sleep(2)
    print(Fore.RED+"THE SECRET MUST NEVER GET OUT...",Fore.RESET)
    exit()
  else:
    lvl5_invalid1 = "Warnings were given before about this issue."
    write(lvl5_invalid1)
    times()
    dots10 = "..."
    write(dots10)
    times()
    lvl5_invalid2 = "If you've never seen or heard me before,\nThen this is bad luck for you.\nUnfortunatly, I am at my limit.\nSo this is goodbye."
    write(lvl5_invalid2)
    time.sleep(2)
    print(Fore.RED+"Goodbye...",Fore.RESET)
    exit()

# level 6 (The user enters a big hotel lobby with no one in there. They go towards another elevator which gives them the option for 4 different floors; The basement, basic floor, advanced floor and ???. If the user chooses basement, they have the option to turn around which lets them retry the floors or continue. If the user continues they go through a door that sends them back to level 2. If the user goes to the 'basic floor', it's an office space which they can either turn around or continue. If they continue, they enter a door that sends them back to level 4. If the user goes to 'advanced floor', they enter a lounge area with the option to turn around or continue. If the user continues, they can pick up an item that they find or leave it, and then they enter another door that sends them back to level 3. If the user picks ???, they get sent to the next level. If the user ever types something invalid, they get sent back to the elevator selection. )
def lvl6():
  times()
  lvl6_text1 = "\nThis just keeps getting weirder."
  write(lvl6_text1)
  times()
  lvl6_text2 = "How do I go from winter,\nall the way to a nice hotel."
  write(lvl6_text2)
  times()
  lvl6_text3 = "Although it's strange how I'm the only one here.\nFeels waaaaay to empty for something this nice."
  write(lvl6_text3)
  times()
  lvl6_text4 = "Looks like there's an elevator.\nGuess it's my only option."
  write(lvl6_text4)
  times()
  lvl6_text5 = "This lobby is bigger than I thought.\nWait is that diamonds?\nHoly this must be something.\nEven those elevator doors have emeralds in them."
  write(lvl6_text5)
  times()
  # this function is used to let the user pick a floor option again.
  def elevator():
    times()
    elevator = int(input("\nWhich floor should I go on?:\n1. Basement\n2.'Basic Floor'\n3.'Advanced Floor'\n4.'???'\n\nPlease enter the number of the floor you wish to go to: "))
    if elevator == 1:
      basement1 = "Alright to the basement we go."
      write(basement1)
      times()
      dots11 = "..."
      write(dots11)
      times()
      basement2 = "This basement gives me an eerie feeling.\nThere's no way this could be good.\nThe elevator door hasn't disappered behind me yet soo that's an option."
      write(basement2)
      basement3 = input("Should I go turn around or continue?: ")
      basement_lower = basement3.lower()
      if basement_lower == "turn around":
        base_turn1 = "I think this is the better option."
        write(base_turn1)
        times()
        elevator()
      elif basement_lower == "continue":
        base_con1 = "Guess I'll go against my gut."
        write(base_con1)
        times()
        base_con2 = "Why does the ground feel musty?\nAnd as I thought the door disappeared...\nGreeeeaaaat"
        write(base_con2)
        times()
        base_con3 = "Wait there's a door,\nI only got the one option,\ngo\nthrough\nthe\ndoor."
        write(base_con3)
        times()
        base_con4 = "Oh it's,\njust another portal...\nTime to go in it."
        write(base_con4)
        times()
        base_con5 = "Wait why does my head feel fuzzy..."
        write(base_con5)
        times()
        lvl2()
      else:
        base_invalid = "Oops wrong answer.\nTry again."
        write(base_invalid)
        times()
        elevator()
    if elevator == 2:
      basicroom1 = "Alright to the 'basic room' we go."
      write(basicroom1)
      times()
      dots12 = "..."
      write(dots12)
      times()
      basicroom2 = "This 'basic room' is strange.\nWhy are there so many office chairs?\nThe elevator door hasn't disappered behind me yet soo that's an option."
      write(basicroom2)
      basicroom3 = input("Should I go turn around or continue?: ")
      basicroom_lower = basicroom3.lower()
      if basicroom_lower == "turn around":
        basic_turn1 = "I think this is the better option."
        write(basic_turn1)
        times()
        elevator()
      elif basicroom_lower == "continue":
        basic_con1 = "Guess I'll go against my gut."
        write(basic_con1)
        times()
        basic_con2 = "These office cubicals are strange.\nAnd as I thought the door disappeared...\nGreeeeaaaat\nLooks like each cubical has a person's name.\nJamal Jefferson\nMaria Bardwash\nJoe Smith\nJohn Doe\neven Joane Lasert."
        write(basic_con2)
        times()
        basic_con3 = "Wait there's a door,\nI only got the one option,\ngo\nthrough\nthe\ndoor."
        write(basic_con3)
        times()
        basic_con4 = "Oh it's,\njust another portal...\nTime to go in it."
        write(basic_con4)
        times()
        basic_con5 = "Wait why does my head feel fuzzy..."
        write(basic_con5)
        times()
        lvl4()
      else:
        basic_invalid = "Oops wrong answer.\nTry again."
        write(basic_invalid)
        times()
        elevator()
    if elevator == 3:
      adroom1 = "Alright to the 'advanced room' we go."
      write(adroom1)
      times()
      dots8 = "..."
      write(dots8)
      times()
      adroom2 = "This 'advanced room' is strange.\nWhy are there so many lounges?\nCrazy to think people can relax in a place like this...\nThe elevator door hasn't disappered behind me yet soo that's an option."
      write(adroom2)
      adroom3 = input("Should I go turn around or continue?: ")
      adroom_lower = adroom3.lower()
      if adroom_lower == "turn around":
        ad_turn1 = "I think this is the better option."
        write(ad_turn1)
        times()
        elevator()
      elif adroom_lower == "continue":
        ad_con1 = "Guess I'll go against my gut."
        write(ad_con1)
        times()
        ad_con2 = "These lounges look comfy\nAnd as I thought the door disappeared...\nGreeeeaaaat\nLooks like each lounge has its own name.\nChill lounge\nWork lounge\nRandom lounge\nBed lounge\neven Random lounge."
        write(ad_con2)
        times()
        ad_item1 = "Wait looks like there's an item."
        write(ad_item1)
        times()
        dots13 = "..."
        write(dots13)
        times()
        ad_item2 = input("Should I grab the item?(y/n): ")
        ad_lower = ad_item2.lower
        if ad_lower == "y":
          print(Fore.GREEN+"You obtained John Doe's Pen!",Fore.RESET)
          times()
          ad_item3 = "Well I should continue going forward.\nDon't know what imma do with the pen but I guess I have it now."
          write(ad_item3)
          times()
          ad_item4 = "Wait there's another door\nI should probablly go through it."
          write(ad_item4)
          times()
          ad_item5 = "Oh it's a portal.\nWell guess I should go through it."
          write(ad_item5)
          lvl7()
        elif ad_lower == "n":
          ad_item6 = "Okay I'll walk past is then."
          write(ad_item6)
          times()
        ad_con3 = "Wait there's a door,\nI only got the one option,\ngo\nthrough\nthe\ndoor."
        write(ad_con3)
        times()
        ad_con4 = "Oh it's,\njust another portal...\nTime to go in it."
        write(ad_con4)
        times()
        ad_con5 = "Wait why does my head feel fuzzy..."
        write(ad_con5)
        times()
        lvl3()
      else:
          print(Fore.BLUE+"Too lazy to print in other lines.\nTry again.",Fore.RESET)
          elevator()
    if elevator == 4:
      quesroom1 = "Okay I guess I'll go to ???"
      write(quesroom1)
      times()
      lvl7()
    else:
      ele_invalid = "Oops miss type.\nTry again."
      write(ele_invalid)
      times()
  elevator()
      
# the function used to call level 7 as a whole
def lvl7():
# level 7 part 1 (User enters a server room with lots of computer. They see one in the middle with a password lock. The user can either search for the password or look around the computer. If the answer is invalid, the user may retry.)  
  def lvl7pt1():
    times()
    lvl7_text1 = "\nThis room is crazzzy.\nSo many computers everywhere!\nHow could someone stay in a room like this.\nHowever it looks like there's a main computer down that server hallway.\nSeems it's my only option."
    write(lvl7_text1)
    times()
    lvl7_text2 = "\nwalking slowly..."
    write(lvl7_text2)
    times()
    lvl7_text3 = "\nThere's a lot of servers in here.\nThe noise of all of them might get annoying...\nOOoo my fav number, 6."
    write(lvl7_text3)
    times()
    lvl7_text4 = "Okay finally at the computer.\nIt says 'Invalid man's computer'\nI wonder who Invalid Man is.\nLooks like it needs a password.\nI should probably search around for it."
    write(lvl7_text4)
    times()
    lvl7_text5 = input("\nShould I search around for the password? (y/n): ")
    lvl7_ex_low = lvl7_text5.lower()
    if lvl7_ex_low == "y":
      lvl7_text6 = "Alright time to explore."
      write(lvl7_text6)
      times()
      lvl7_text7 = "Looks like it's no where around the other computers.\nMaybe I should go back to the main computer and say something random."
      write(lvl7_text7)
      time.sleep(2)
    elif lvl7_ex_low == "n":
      lvl7_text8 = "Alright I'll just stay here then.\nIf I had to guess the password, it might just be something random."
      write(lvl7_text8)
      time.sleep(2)
    while lvl7_ex_low != "y" and lvl7_ex_low != "n":
      lvl7_ex_invalid = "'THIS INVALID RESPONSE WAS BROUGHT TO YOU BUY, invalid man...'\nPLEASE TRY AGAIN."
      write(lvl7_ex_invalid)
      times()
      lvl7pt1()
  lvl7pt1()
  
# level 7 part 2 (The user now has access to the computer however, now Invalid Man trys to talk to them. He lists numbers that should be remmbered in the future.)
  def lvl7pt2():
    times()
    print(Fore.GREEN+"\nACCESS GRANTED!",Fore.RESET)
    times()
    lvl7_text9 = "\nAin't no way that was the password."
    write(lvl7_text9)
    times()
    dots14 = "..."
    write(dots14)
    times()
    lvl7_text10 = "₩ɆⱠ₵Ø₥Ɇ ₮Ø ł₦V₳ⱠłĐ ₥₳₦'₴ ₵Ø₥₱Ʉ₮ɆⱤ"
    write(lvl7_text10)
    times()
    lvl7_text11 = "\nł'VɆ ⱠɆ₣₮ ₮Ⱨł₴ ₥Ɇ₴₴₳₲Ɇ ₴₱Ɇ₵ł₣ł₵₳ⱠⱠɎ ₣ØⱤ ɎØɄ..\n₣ØⱤ ł₦₮ⱤØĐɄ₵₮łØ₦, ł ₳₥ ł₦V₳ⱠłĐ ₥₳₦\n₳₦Đ ₮Ⱨł₴ ł₴ ₩ⱧɆⱤɆ ɆVɆⱤɎ₮Ⱨł₦₲ ł₴ ₥₳ĐɆ.\nł'₥ ₭ł₦Đ₳ ₮ⱧɆ ₥ł₦ł ฿Ø₴₴ ₳ⱤØɄ₦Đ ⱧɆⱤɆ.\n₮ⱧɆⱤɆ'₴ ₴Ø₥ɆØ₦Ɇ ₩ⱧØ'₴ Ⱨł₲ⱧɆⱤ ⱧɆⱤɆ..\nɎØɄⱤ JØ฿ ł₴ ₮Ø ₣ł₦Đ Ⱨł₥...\nⱤɆ₥Ɇ₥฿ɆⱤ ₮ⱧɆ ₦Ʉ₥฿ɆⱤ₴ ł'₥ ₳฿ØɄ₮ ₮Ø ₮ɆⱠⱠ ɎØɄ.\n₮ⱧɆɎ ₵₳₦ ฿Ɇ Ʉ₴ɆĐ ₮Ø Ʉ₦ⱠØ₵₭ ₳ ₴₱Ɇ₵ł₳Ⱡ ĐØØⱤ Ⱡ₳₮ɆⱤ Ø₦.\n"
    write(lvl7_text11)
    times()
    lvl7_list = [34,56,7,69,2,6,94]
    print(lvl7_list[0])
    times()
    print(lvl7_list[1])
    times()
    print(lvl7_list[2])
    times()
    print(lvl7_list[3])
    times()
    print(lvl7_list[4])
    times()
    print(lvl7_list[5])
    times()
    print(lvl7_list[6])
    time.sleep(2)
    lvl7_text12 = "\n₱ⱠɆ₳₴Ɇ ⱤɆ₥Ɇ₥฿ɆⱤ ₮ⱧɆ₴Ɇ ₦Ʉ₥฿ɆⱤ₴.\nł₮ ₩łⱠⱠ ⱧɆⱠ₱ ₴₳VɆ ₮ⱧɆ ฿ØӾ.\n₩Ɇ'ⱤɆ ₵ØɄ₦₮ł₦₲ Ø₦ ɎØɄ Ɽ₳₦Đ-Đ-Đ-Đ-Ø-"
    write(lvl7_text12)
    times()
    print(Fore.RED+"\nPROCESS DIED.",Fore.RESET)
    times()
    dots15 = "\n..."
    write(dots15)
    times()
    lvl7_text14 = "\nWell looks like I gotta remember those numbers...\nOh wait there's a key,\nmaybe that unlocks that door over there.\nOnly one way to find out!"
    write(lvl7_text14)
    times()
    lvl7_text15 = "Oh so, that worked.\nAnother elevator seriously.\nKINDA GETTING OLD!"
    write(lvl7_text15)
    time.sleep(2)
    lvl7_text16 = "Oh wait, it's just paper.\nMan wt-\nAnyways looks like it's actually stairs going up.\nNo choice but to walk up them.\nHopefully I don't see anything on the way."
    write(lvl7_text16)
    times()
    lvl8()
  lvl7pt2()
# function for level 8, as a whole, that will be called later
def lvl8():
  times()
  lvl8_text1 = "\nThese stairs are sooo tirrrring..."
  write(lvl8_text1)
  times()
  lvl8_text2 = "Can it just be over alreaddy.."
  write(lvl8_text2)
  times()
  lvl8_text3 = "FINALLY A DOOR!\nI'VE BEEN CLIMBING FOR 30 MIN STRAIGHT!"
  write(lvl8_text3)
  times()
  lvl8_text4 = "Woah that a lot of clouds.\nOh wait I'm also standing on clouds.\nIt's so fluffy."
  write(lvl8_text4)
  times()
  lvl8_text5 = "Woah it looks like I have looooow gravity.\nI think I should explore on top of the clouds with this...\nMy choices are left or right."
  write(lvl8_text5)
  times()
  # the user desides whether to go left or right. Left leads the user to a door which requires a password. If correct, you find a piece of paper that tells important information. Right leads to a door that goes back to level 5. Invalid response restarts the level.
  def lvl8pt1():
    times()
    lvl8_desi1 = input("\nGo left or right?: ")
    lvl8_lower1 = lvl8_desi1.lower()
    if lvl8_lower1 == "left":
      lvl8_left1 = "I think left is the best option."
      write(lvl8_left1)
      times()
      lvl8_left2 = "Oh looks like there's a door on that cloud over there.\nMaybe I should jump up to there."
      write(lvl8_left2)
      times()
      dots16 = "..."
      write(dots16)
      times()
      lvl8_left3 = "Ok now this door requires a number to open.\nIt says"
      write(lvl8_left3)
      times()
      lvl8_door1 = int(input("What is my favourite number?: "))
      if lvl8_door1 == 6:
        lvl8_pass1 = "\nOh looks like that was right.\nNice."
        write(lvl8_pass1)
        times()
        lvl8_pass2 = "Oh there's a piece of paper.\nI wonder what it says.."
        write(lvl8_pass2)
        times()
        paper1 = "\n'If your reading this, we need help.\nWith the boss missing and everything, all we could do is hold clues around here.\nHopefully he's able to see it.\nLong story short as he was testing his game,\nhe accidentally got trapped inside of it.\nNow our job is to get him out.\nHopefully this reaches him.\nBye for now.'"
        write(paper1)
        time.sleep(2)
        lvl8_pass3 = "\nWell I have no idea who this boss is but I hope they find him.\nWait I'm kinda remembering that I was a boss of some sort.\nEh whatever doesn't matter.\nLet me put this paper in my pocket for now."
        write(lvl8_pass3)
        print(Fore.GREEN+"You put the paper in your pocket.",Fore.RESET)
        times()
        lvl8_pass4 = "\nOh what's that sound.\nOoo another door at the center,\nmy fav...\nAnyways I feel like I would want to go through that door\ndespite the gut feeling."
        write(lvl8_pass4)
        times()
      while lvl8_door1 != 6:
        pass_invalid1 = "\nINCORRECT ANSWER"
        write(pass_invalid1)
        times()
        lvl8pt1()
    if lvl8_lower1 == "right":
      lvl8_right1 = "Alright I'm feeling right."
      write(lvl8_right1)
      times()
      lvl8_right2 = "\nOh another door.\nNeeds a pass.\nLooks like it might be able to fit the word 'random' again."
      write(lvl8_right2)
      times()
      lvl8_right3 = "\nOh looks like that worked.\nOh another portal...\nfun...\nWell time to go in it, again."
      write(lvl8_right3)
      times()
      lvl5()
    while lvl8_lower1 != "left" and lvl8_lower1 != "right":
      lvl8_invalid1 = "\nHey it's me again, Invalid Man.\nYour here cause you entered something invalid,\nsilly you.\nBut very typical.\nYou've made it this far so I won't punish you as bad."
      write(lvl8_invalid1)
      times()
      lvl8()
  lvl8pt1()
  
  # level 8 part 2 (You try to escape as the clouds disappear fast. You then enter level 9.)
  def lvl8pt2():
    times()
    lvl8_text6 = "\nOk time to see what this door in the center is about.\nWait looks like some clouds are disappering.\nBETTER GO FAST!\nCOME ON KEY FITTTT!!"
    write(lvl8_text6)
    times()
    lvl8_text7 = "\nAh finally in.\nPretty cold in this room.\nLet me try to find the lights."
    write(lvl8_text7)
    times()
    lvl9()
  lvl8pt2()

# the 9th level is just a hallway with a little bit of water on the ground, boxes on shelves and the user has to enter the 7 numbers Invalid Man gave before.
def lvl9():
  times()
  lvl9_text1 = "\nFianlly found the lights.\nEw the ground seems a bit moist.\nOh there's another door.\nI have a feeling this might be the last one!\nBut first things first,\nI have to walk down this long hallway."
  write(lvl9_text1)
  times()
  lvl9_text2 = "As I thought this floor is really moist.\nIt's almost like it rained in here.\nBut that's not physically possible.\nBut everything in here is random anyways.\nAlways happens in the box."
  write(lvl9_text2)
  times()
  dots17 = "..."
  write(dots17)
  times()
  lvl9_text3 = "Okay finally at the door.\nLooks like it requires 7 numbers.\nWAIT, Invalid Man's numbers!\nHope I remember them."
  write(lvl9_text3)
  times()
  # this function is used so if the user enters any of the numbers incorrect, they may retry after answering a trick math question. If not, the code dies and the secret is never let out.
  def lvl9door():
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    num3 = int(input("Number 3: "))
    num4 = int(input("Number 4: "))
    num5 = int(input("Number 5: "))
    num6 = int(input("Number 6: "))
    num7 = int(input("Number 7: "))
    if num1 == 34 and num2 == 56 and num3 == 7 and num4 == 69 and num5 == 2 and num6 == 6 and num7 == 94:
      print(Fore.GREEN+"\nCorrect!",Fore.RESET)
      times()
      lvl9_text4 = "\nYes, I got it right!\nGood thing I remembered those numbers.\nNow it's time to open the door!"
      write(lvl9_text4)
      times()
      lvl10()
    while num1 != 34 and num2 != 56 and num3 == 7 and num4 == 69 and num5 == 2 and num6 == 6 and num7 == 94:
      print(Fore.RED+"Incorrect, try answering this question.",Fore.RESET)
      trick_math = int(input("What is 9 + 10?: "))
      if trick_math == 21:
        print(Fore.GREEN+"\nCorrect! You may retry.",Fore.RESET)
        lvl9door()
      elif trick_math == 19:
        print(Fore.RED+"Incorrect, you thought it was that simple...",Fore.RESET)
        exit()
      else:
        print(Fore.RED+"Incorrect.\nNo more retrying for you.",Fore.RESET)
        time.sleep(2)
        print(Fore.RED+"You died to the Hallway.",Fore.RESET)
        exit()
  lvl9door()

# if the user completes the game, congratulate them on beating the game!
def donegame():
  print(Fore.GREEN+"Congratulations on beating The Box!\nNow the secret has been revealed that you are Random Man!",Fore.RESET)

# level 10 (The user enters the final room, where they will find out the big secret)
def lvl10():
  times()
  lvl10_text1 = "\nThis is a pretty nice computer room.\nThe strange thing is I oddly recognize it.\nMaybe I've seen it in a dream?"
  write(lvl10_text1)
  times()
  lvl10_text2 = "\n𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕓𝕒𝕔𝕜 ℝ𝕒𝕟𝕕𝕠𝕞 𝕄𝕒𝕟."
  write(lvl10_text2)
  times()
  lvl10_text3 = "\nWoah the computer's talking to me\nagain..."
  write(lvl10_text3)
  times()
  lvl10_text4 = "\n𝕐𝕖𝕤 𝕀 𝕒𝕞,\n𝕪𝕠𝕦 𝕞𝕒𝕪 𝕟𝕠𝕥 𝕣𝕖𝕞𝕖𝕞𝕓𝕖𝕣 𝕗𝕠𝕣 𝕣𝕚𝕘𝕙𝕥 𝕟𝕠𝕨 𝕓𝕦𝕥 𝕪𝕠𝕦 𝕡𝕣𝕠𝕘𝕣𝕒𝕞𝕖𝕕 𝕞𝕖."
  write(lvl10_text4)
  times()
  lvl10_text5 = "\nWhaaat that's crazy.\nBy the way, what's the question?"
  write(lvl10_text5)
  times()
  lvl10_num = int(input("\n𝕎𝕙𝕒𝕥'𝕤 𝕥𝕙𝕖 𝟞𝕥𝕙 𝕟𝕦𝕞𝕓𝕖𝕣 𝕀𝕟𝕧𝕒𝕝𝕚𝕕 𝕄𝕒𝕟 𝕥𝕠𝕝𝕕 𝕪𝕠𝕦? "))
  if lvl10_num == 6:
    print(Fore.GREEN+"𝔾𝕠𝕠𝕕 𝕪𝕠𝕦 𝕣𝕖𝕞𝕖𝕞𝕓𝕖𝕣𝕖𝕕.",Fore.RESET)
    times()
    lvl10_text6 = "\nℕ𝕠𝕨 𝕀 𝕔𝕒𝕟 𝕥𝕖𝕝𝕝 𝕪𝕠𝕦 𝕥𝕙𝕖 𝕨𝕙𝕠𝕝𝕖 𝕓𝕒𝕔𝕜 𝕤𝕥𝕠𝕣𝕪."
    write(lvl10_text6)
    time.sleep(3)
    
    # this text gives the user the backstory behind everything, this is my favourite part of the whole game.
    lvl10_text7 = "\n𝕀𝕥 𝕒𝕝𝕝 𝕤𝕥𝕒𝕣𝕥𝕖𝕕 𝕨𝕙𝕖𝕟 𝕪𝕠𝕦, ℝ𝕒𝕟𝕕𝕠𝕞 𝕄𝕒𝕟, 𝕔𝕣𝕖𝕒𝕥𝕖𝕕 𝕥𝕙𝕚𝕤 𝕡𝕝𝕒𝕔𝕖 𝕥𝕙𝕒𝕥 𝕨𝕖 𝕔𝕒𝕝𝕝 𝕋𝕙𝕖 𝔹𝕠𝕩.\n𝕐𝕠𝕦 𝕙𝕚𝕣𝕖𝕕 𝕞𝕒𝕟𝕪 𝕕𝕚𝕗𝕗𝕖𝕣𝕖𝕟𝕥 𝕡𝕖𝕠𝕡𝕝𝕖, 𝕚𝕟𝕔𝕝𝕦𝕕𝕚𝕟𝕘 𝕪𝕠𝕦𝕣 𝕓𝕖𝕤𝕥 𝕗𝕣𝕚𝕖𝕟𝕕.\n𝕐𝕠𝕦 𝕟𝕒𝕞𝕖𝕕 𝕙𝕚𝕞 '𝕀𝕟𝕧𝕒𝕝𝕚𝕕 𝕄𝕒𝕟', 𝕒𝕟𝕕 𝕡𝕣𝕠𝕧𝕚𝕕𝕖𝕕 𝕙𝕚𝕞 𝕨𝕚𝕥𝕙 𝕒𝕟 𝕚𝕟𝕗𝕚𝕟𝕚𝕥𝕖 𝕤𝕦𝕡𝕡𝕝𝕪 𝕠𝕗 ℙ𝕣𝕚𝕞𝕖.\n𝕆𝕗 𝕔𝕠𝕦𝕣𝕤𝕖 𝕜𝕟𝕠𝕨𝕚𝕟𝕘 𝕪𝕠𝕦 𝕓𝕠𝕤𝕤, 𝕪𝕠𝕦 𝕕𝕣𝕒𝕟𝕜 𝕒𝕝𝕞𝕠𝕤𝕥 𝕒𝕝𝕝 𝕠𝕗 𝕚𝕥..\n𝕋𝕙𝕖𝕟 𝕠𝕟𝕖 𝕕𝕒𝕪, 𝕪𝕠𝕦 𝕨𝕖𝕣𝕖 𝕥𝕖𝕤𝕥𝕚𝕟𝕘 𝕠𝕦𝕥 𝕋𝕙𝕖 𝔹𝕠𝕩,\n𝕥𝕠 𝕤𝕖𝕖 𝕚𝕗 𝕨𝕒𝕤 𝕣𝕖𝕒𝕕𝕪 𝕗𝕠𝕣 𝕥𝕙𝕖 𝕞𝕠𝕟𝕖𝕪 𝕔𝕠𝕞𝕡𝕖𝕥𝕚𝕥𝕚𝕠𝕟 𝕪𝕠𝕦 𝕙𝕒𝕕 𝕚𝕟 𝕞𝕚𝕟𝕕.\n𝕋𝕙𝕖𝕟 𝕒𝕝𝕝 𝕠𝕗 𝕒 𝕤𝕦𝕕𝕕𝕖𝕟, 𝕀𝕟𝕧𝕒𝕝𝕚𝕕 𝕄𝕒𝕟 𝕝𝕠𝕤𝕥 𝕔𝕠𝕟𝕟𝕖𝕔𝕥𝕚𝕠𝕟 𝕨𝕚𝕥𝕙 𝕪𝕠𝕦𝕣 𝕔𝕠𝕞𝕞𝕦𝕟𝕚𝕔𝕒𝕥𝕚𝕠𝕟 𝕤𝕪𝕤𝕥𝕖𝕞,\n𝕒𝕟𝕕 𝕨𝕖 𝕦𝕤𝕖𝕕 𝕥𝕙𝕖 𝕤𝕖𝕔𝕦𝕣𝕚𝕥𝕪 𝕔𝕒𝕞𝕖𝕣𝕒𝕤 𝕥𝕠 𝕗𝕚𝕟𝕕 𝕪𝕠𝕦.\n𝕎𝕖 𝕗𝕠𝕦𝕟𝕕 𝕪𝕠𝕦 𝕒𝕥 𝕝𝕖𝕧𝕖𝕝 𝟙 𝕨𝕚𝕥𝕙 𝕪𝕠𝕦𝕣 𝕞𝕚𝕟𝕕 𝕔𝕠𝕞𝕡𝕝𝕖𝕥𝕖𝕝𝕪 𝕨𝕚𝕡𝕖𝕕 𝕠𝕦𝕥.\n𝕐𝕠𝕦 𝕨𝕖𝕣𝕖 𝕦𝕟𝕔𝕠𝕟𝕤𝕔𝕚𝕠𝕦𝕤 𝕗𝕠𝕣 𝕒 𝕘𝕠𝕠𝕕 𝕨𝕖𝕖𝕜,\n𝕤𝕠 𝕨𝕖 𝕤𝕖𝕥 𝕦𝕡 𝕔𝕝𝕦𝕖𝕤 𝕒𝕣𝕠𝕦𝕟𝕕 𝕋𝕙𝕖 𝔹𝕠𝕩 𝕗𝕠𝕣 𝕪𝕠𝕦 𝕥𝕠 𝕗𝕠𝕝𝕝𝕠𝕨.\n𝕆𝕗 𝕔𝕠𝕦𝕣𝕤𝕖 𝕤𝕚𝕟𝕔𝕖 𝕪𝕠𝕦 𝕞𝕒𝕕𝕖 𝕚𝕥 𝕥𝕙𝕚𝕤 𝕗𝕒𝕣,\n𝕋𝕙𝕖 𝕠𝕥𝕙𝕖𝕣 𝕕𝕖𝕔𝕚𝕤𝕚𝕠𝕟𝕤 𝕨𝕠𝕦𝕝𝕕'𝕧𝕖 𝕝𝕖𝕒𝕕 𝕥𝕠 𝕕𝕖𝕒𝕥𝕙,\n𝕤𝕠 𝕚𝕥'𝕤 𝕒 𝕘𝕠𝕠𝕕 𝕥𝕙𝕚𝕟𝕘 𝕥𝕙𝕒𝕥 𝕪𝕠𝕦𝕣 𝕙𝕖𝕣𝕖 𝕟𝕠𝕨.\n𝔸𝕟𝕪𝕨𝕒𝕪𝕤 𝕟𝕠𝕨 𝕥𝕙𝕒𝕥 𝕪𝕠𝕦 𝕜𝕟𝕠𝕨 𝕥𝕙𝕖 𝕓𝕒𝕔𝕜𝕤𝕥𝕠𝕣𝕪,\n𝕪𝕠𝕦𝕣 𝕞𝕖𝕞𝕠𝕣𝕪 𝕞𝕦𝕤𝕥 𝕓𝕖 𝕣𝕖𝕤𝕥𝕠𝕣𝕖𝕕..."
    write(lvl10_text7)
    time.sleep(2)
    lvl10_text8 = "\n𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕓𝕒𝕔𝕜 ℝ𝕒𝕟𝕕𝕠𝕞 𝕄𝕒𝕟........."
    write(lvl10_text8)
    time.sleep(2)
    donegame()
  else:
    print(Fore.RED+"ℍ𝕠𝕨 𝕔𝕠𝕦𝕝𝕕 𝕪𝕠𝕦 𝕟𝕠𝕥 𝕣𝕖𝕞𝕖𝕞𝕓𝕖𝕣.\n𝕐𝕠𝕦 𝕒𝕣𝕖 𝕟𝕠𝕥 𝕥𝕙𝕖 ℝ𝕒𝕟𝕕𝕠𝕞 𝕄𝕒𝕟 𝕀 𝕜𝕟𝕠𝕨...",Fore.RESET)
    time.sleep(2)
    exit()

# welcome the user to the game and call each level when stated (used for developer mode/testing)
welcome = "\nWelcome to the box!"
write(welcome)

# dev note (When the first input statment appears, if you write lvl and then the number of the level you wish to go to, it will take you straight to that level. The only exception is lvl1 since you can simply right "yes" to go there.)
times()
started = input("\nIf you wish to start, please enter (yes): ")
started_low = started.lower()
if started_low == "yes":
  con_1 = "\nGreat, we can continue."
  write(con_1)
  times()
  lvl1()
  lvl2()
  lvl3()
  lvl4()
  lvl5()
  lvl6()
  lvl7()
  lvl8()
  lvl9()
  lvl10()
if started_low == "lvl2":
  con_2 = "\nGreat, we can continue."
  write(con_2)
  lvl2()
if started_low == "lvl3":
  con_3 = "\nGreat, we can continue."
  write(con_3)
  lvl3()
if started_low == "lvl4":
  con_4 = "\nGreat, we can continue."
  write(con_4)
  lvl4()
if started_low == "lvl5":
  con_5 = "\nGreat, we can continue."
  write(con_5)
  lvl5()
if started_low == "lvl6":
  con_6 = "\nGreat, we can continue."
  write(con_6)
  lvl6()
if started_low == "lvl7":
  con_7 = "\nGreat, we can continue."
  write(con_7)
  lvl7()
if started_low == "lvl8":
  con_8 = "\nGreat, we can continue."
  write(con_8)
  lvl8()
if started_low == "lvl9":
  con_9 = "\nGreat, we can continue."
  write(con_9)
  lvl9()
if started_low == "lvl10":
  con_10 = "\nGreat, we can continue."
  write(con_10)
  lvl10()
while started_low != "yes" and started_low != "lvl2" and started_low != "lvl3" and started_low != "lvl4" and started_low != "lvl5" and started_low != "lvl6" and started_low != "lvl7" and started_low != "lvl8" and started_low != "lvl9" and started_low != "lvl10":
  wel_invalid = "You mustn't say anything else."
  write(wel_invalid)
  times()
  exit() 

# all the functions used to call each level
# lvl1()
# lvl2()
# lvl3()
# lvl4()
# lvl5()
# lvl6()
# lvl7()
# lvl8()
# lvl9()
# lvl10()