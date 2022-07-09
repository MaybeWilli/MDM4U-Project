import pygame
import random

pygame.init()

window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Jojos Bizzare Data Management Project!")

#main menu and arrow variables
needsArrow = True
isMainMenu = True
isRunning = True
mainMenuArrowX = [250, 250]
mainMenuArrowY = [350, 550]
mainMenuState = 0
fightArrowX = 25
fightArrowY = [550, 600, 650]
fightState = 0
explainArrowX = [25, 455]
explainArrowY = 725
activeFightState = 0
isExplain = False
explainState = 0
isChoose = False
chooseState = 0
chooseArrowX = [25, 25, 25, 425, 425, 425]
chooseArrowX2 = [25, 425]
chooseArrowY = [600, 640, 680, 600, 640, 680]
isAttacking = False
usesCounter = 20
effectiveCounter = 40
attackWorks = False
isAttacked = False
diavoloEffectiveCounter = 40
diavoloAttackWorks = False
diavoloUsesCounter = 20
isCredits = True
canClick = True

#fight and revelant variables
isFight = False
isAttacks = True
diavoloDamageCounter = -1
diavoloHealth = 100
charactersAlive = 3
#jotaro
jotaroAlive = True
jotaroDamage = 50
num1 = -1
num2 = -1
#dio
dioAlive = True
dioDamage = 40
#johnny
johnnyAlive = True
#dice
val = 0

#image importing
#main menu
arrow = pygame.image.load("Arrow.png") #100, 25
playButton = pygame.image.load("PlayButton.png") #150, 100
creditButton = pygame.image.load("CreditButton.png")
titleText = pygame.image.load("Title.png") #250, 100
diceText = pygame.image.load("Dice_selector.png")
diceText2 = pygame.image.load("Dice_selector2.png")
diceText3 = pygame.image.load("Dice_selector3.png")

#fight
diavolo = pygame.image.load("Data_diavolo.png") #300, 300
jotaro = pygame.image.load("JotaroFrames/Data_jotaro.png") #200, 200
attackText = pygame.image.load("Attacks.png") #800, 250
jotaroExplain = pygame.image.load("Jotaro_Explanation.png")
explains = [jotaroExplain, pygame.image.load("Dio_Explanation.png"), pygame.image.load("Johnny_Explanation.png")]
wasEffective = pygame.image.load("Quite_effective.png")
notEffective = pygame.image.load("Not_effective.png")
uses = [pygame.image.load("Whack_used.png"), pygame.image.load("Road_used.png"), pygame.image.load("Spin_used.png")]
dice = [pygame.image.load("Dice1.png"), pygame.image.load("Dice2.png"), pygame.image.load("Dice3.png"), pygame.image.load("Dice4.png"), pygame.image.load("Dice5.png"), pygame.image.load("Dice6.png")]
greenBackground = pygame.image.load("Green_background.png")
redBackground = pygame.image.load("Red_background.png")
donutText = pygame.image.load("Donut.png")
dio = pygame.image.load("Data_dio.png")
johnny = pygame.image.load("Data_johnny.png")
tusk = pygame.image.load("Data_tusk.png")
zaWarudo = pygame.image.load("Data_warudo.png")
starPlatinum = pygame.image.load("Data_platinum.png")
kingCrimson = pygame.image.load("Data_crimson.png")
wins = [pygame.image.load("Win1.png"), pygame.image.load("Win2.png"), pygame.image.load("Win3.png")]
loseText = pygame.image.load("Lose.png")

#sounds
music = pygame.mixer.music.load("il_vento_doro.mp3")
roadRollerSound = pygame.mixer.Sound("ROAD_ROLLER_DA.mp3")
kingCrimsonSound = pygame.mixer.Sound("Diavolo_King_Crimson.mp3")
starPlatinumSound = pygame.mixer.Sound("Star_platinum.mp3")
tuskSound = pygame.mixer.Sound("Tusk_cry.mp3")

while (isRunning and diavoloHealth > 0 and charactersAlive > 0):
  pygame.time.delay(100) #framerate controller
  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      isRunning = False
      isCredits = False

  keys = pygame.key.get_pressed()

  #drawing parts
  window.fill((200, 200, 200))

  if (needsArrow): #if arrow should be drawn
  
    if (isMainMenu):
      window.blit(playButton, (375, 325))
      window.blit(creditButton, (375, 525))
      window.blit(titleText, (275, 100))
      if (keys[pygame.K_DOWN] and mainMenuState == 0):
        mainMenuState = 1
      elif (keys[pygame.K_UP] and mainMenuState == 1):
        mainMenuState = 0
      window.blit(arrow, (mainMenuArrowX[mainMenuState], mainMenuArrowY[mainMenuState]))
      
      if (keys[pygame.K_RETURN]):
        if (mainMenuState==0):
          #switch to other mode
          isMainMenu = False
          isFight = True
          pygame.mixer.music.play(-1)
        else:
          print("That feature hasn't been added yet! L.")
          
    elif (isFight):
      pygame.draw.rect(window, (0, 0, 0), (450, 300, 300, 5))
      pygame.draw.rect(window, (0, 0, 0), (50, 500, 400, 5))
      #text
      if (isAttacks):
        window.blit(attackText, (0, 525))
        if (keys[pygame.K_DOWN] and fightState != 2):
          fightState += 1
        elif (keys[pygame.K_UP] and fightState != 0):
          fightState -= 1
        window.blit(arrow, (fightArrowX, fightArrowY[fightState]))
        
      elif (isExplain):
        window.blit(explains[activeFightState], (0, 525))
        if (keys[pygame.K_RIGHT] and explainState == 0):
          explainState = 1
        elif (keys[pygame.K_LEFT] and explainState == 1):
          explainState = 0
        window.blit(arrow, (explainArrowX[explainState], explainArrowY))
      
      elif (isChoose):
        if (activeFightState == 0):
          window.blit(diceText, (0, 525))
          if (keys[pygame.K_DOWN] and chooseState != 5):
            chooseState += 1
          elif (keys[pygame.K_UP] and chooseState != 0):
            chooseState -= 1
          window.blit(arrow, (chooseArrowX[chooseState], chooseArrowY[chooseState]))
          
          #draw the dice
          if (num1 != -1):
            window.blit(dice[num1-1], (500, 350))
          if (num2 != -1):
            window.blit(dice[num2-1], (600, 350))
            
        elif (activeFightState == 1): #Dio!
          window.blit(diceText2, (0, 525))
          if (keys[pygame.K_RIGHT] and chooseState == 0):
            chooseState = 1
          elif (keys[pygame.K_LEFT] and chooseState == 1):
            chooseState = 0
          window.blit(arrow, (chooseArrowX2[chooseState], 600))
          
        elif (activeFightState == 2):
          window.blit(diceText3, (0, 525))
          if (keys[pygame.K_DOWN] and chooseState != 5):
            chooseState += 1
          elif (keys[pygame.K_UP] and chooseState != 0):
            chooseState -= 1
          window.blit(arrow, (chooseArrowX[chooseState], chooseArrowY[chooseState]))
        
        if (keys[pygame.K_z]):
          num1 = -1
          num2 = -1
          isChoose = False
          isAttacks = True
          
      elif (isAttacking): #used, then is effective, and whatnot
        if (usesCounter > 0):
          usesCounter -= 1
          window.blit(uses[activeFightState], (0, 525))
          if (activeFightState == 0):
            pygame.mixer.music.pause()
            if(usesCounter == 19):
              starPlatinumSound.play()
            window.blit(dice[num1-1], (500, 350))
            window.blit(dice[num2-1], (600, 350))
            window.blit(starPlatinum, (50, 300))
          elif (activeFightState == 1):
            pygame.mixer.music.pause()
            if(usesCounter == 19):
              roadRollerSound.play()
            window.blit(zaWarudo, (150, 300))
            if (num1 == 0):
              window.blit(dice[0], (450, 350))
              window.blit(dice[1], (530, 350))
              window.blit(dice[2], (610, 350))
            else:
              window.blit(dice[3], (450, 350))
              window.blit(dice[4], (530, 350))
              window.blit(dice[5], (610, 350))
          else:
            pygame.mixer.music.pause()
            if(usesCounter == 19):
              tuskSound.play()
            window.blit(dice[num1-1], (500, 350))
            window.blit(tusk, (250, 300))
        elif (effectiveCounter >= 0): #decide the dice roll's effectiveness
          if(usesCounter == 0):
            val = random.randint(1, 6)
          usesCounter = -1
          effectiveCounter -= 1
          if (activeFightState == 0):
            if (val == num1 or val == num2):
              window.blit(greenBackground, (695, 345))
              window.blit(dice[val-1], (700, 350))
              window.blit(wasEffective, (0, 525))
              attackWorks = True
            else:
              window.blit(redBackground, (695, 345))
              window.blit(dice[val-1], (700, 350))
              window.blit(notEffective, (0, 525))
              attackWorks = False
            window.blit(dice[num1-1], (500, 350))
            window.blit(dice[num2-1], (600, 350))
            window.blit(starPlatinum, (50, 300))
          elif (activeFightState == 1):
            if ((num1 == 0 and val <= 3) or (num1 == 1 and val > 3)):
              window.blit(greenBackground, (695, 345))
              window.blit(dice[val-1], (700, 350))
              window.blit(wasEffective, (0, 525))
              attackWorks = True
            else:
              window.blit(redBackground, (695, 345))
              window.blit(dice[val-1], (700, 350))
              window.blit(notEffective, (0, 525))
              attackWorks = False
            window.blit(zaWarudo, (150, 300))
            if (num1 == 0):
              window.blit(dice[0], (450, 350))
              window.blit(dice[1], (530, 350))
              window.blit(dice[2], (610, 350))
            else:
              window.blit(dice[3], (450, 350))
              window.blit(dice[4], (530, 350))
              window.blit(dice[5], (610, 350))
          elif (activeFightState == 2):
            if (val == num1):
              window.blit(greenBackground, (695, 345))
              window.blit(dice[val-1], (700, 350))
              window.blit(wasEffective, (0, 525))
              attackWorks = True
            else:
              window.blit(redBackground, (695, 345))
              window.blit(dice[val-1], (700, 350))
              window.blit(notEffective, (0, 525))
              attackWorks = False
            window.blit(dice[num1-1], (500, 350))
            window.blit(tusk, (250, 300))
          if (effectiveCounter == 0):
            if (activeFightState == 0 and attackWorks):
              diavoloHealth -= jotaroDamage
            elif (activeFightState == 1 and attackWorks):
              diavoloHealth -= 40
            elif (attackWorks):
              diavoloHealth = 0
		        
            if (activeFightState == 1):
              pygame.mixer.music.unpause()
		        
            if (diavoloHealth > 0):
              isAttacked = True
              isAttacking = False
            else:
              isRunning = False
        #window.blit(dice[num1-1], (500, 350))
        #window.blit(dice[num2-1], (600, 350))
      

      elif (isAttacked):
        if (diavoloUsesCounter > 0):
          diavoloUsesCounter -= 1
          window.blit(donutText, (0, 525))
          window.blit(donutText, (0, 525))
          window.blit(kingCrimson, (450, 0))
          pygame.mixer.music.pause()
          if (diavoloUsesCounter == 19):
            kingCrimsonSound.play()
        elif(diavoloEffectiveCounter > 0): #decide diavolo attack effectiveness
          if (diavoloUsesCounter == 0):
            val = random.randint(1, 6)
          diavoloUsesCounter = -1
          window.blit(kingCrimson, (450, 0))
          diavoloEffectiveCounter -= 1
          if (val <= 3):
            window.blit(greenBackground, (695, 345))
            window.blit(dice[val-1], (700, 350))
            window.blit(wasEffective, (0, 525))
            attackWorks = True
          else:
            window.blit(redBackground, (695, 345))
            window.blit(dice[val-1], (700, 350))
            window.blit(notEffective, (0, 525))
            attackWorks = False
        elif (diavoloEffectiveCounter == 0):
          if (activeFightState == 0 and attackWorks):
            jotaroAlive = False
          elif (activeFightState == 1 and attackWorks):
            dioAlive = False
          elif(attackWorks):
            johnnyAlive = False
            
          if (attackWorks):
            charactersAlive -= 1
            if (charactersAlive == 0):
              break;
          pygame.mixer.music.unpause()
          isAttacked = False
          isAttacks = True
          num1 = -1
          num2 = -1
          usesCounter = 20
          effectiveCounter = 40
          diavoloEffectiveCounter = 40
          diavoloUsesCounter = 20 
          chooseState = 0
          explainState = 0
          mainMenuState = 0
       
        window.blit(dice[0], (450, 350))
        window.blit(dice[1], (530, 350))
        window.blit(dice[2], (610, 350))
          
      
      #diavolo
      if (diavoloHealth > 0):
        pygame.draw.rect(window, (0, 255, 0), (500, 30, (diavoloHealth * 2), 5))
        window.blit(diavolo, (450, 0))
      
      #characters
      if (jotaroAlive):
        window.blit(jotaro, (50, 300))
      if (dioAlive):
        window.blit(dio, (150, 300))
      if (johnnyAlive):
        window.blit(johnny, (250, 300))
      
      #actually pressing enter
      if (keys[pygame.K_RETURN] and canClick):
        canClick = False
        if (isAttacks):
          if ((fightState == 0 and jotaroAlive) or (fightState == 1 and dioAlive) or (fightState == 2 and johnnyAlive)):
            isAttacks = False
            isExplain = True
            activeFightState = fightState
        elif (isExplain):
          if (explainState == 0):
            isAttacks = True
            isExplain = False
          else:
            isExplain = False
            isChoose = True
        elif (isChoose):
          if (activeFightState == 0): #2 meters attack
            if (num1 == -1):
              num1 = chooseState+1
            elif (num2 == -1):
              num2 = chooseState+1
            else:
              isChoose = False
              isAttacking = True
          elif(activeFightState == 1):
            num1 = chooseState
            isChoose = False
            isAttacking = True
          elif(activeFightState == 2):
            num1 = chooseState+1
            isChoose = False
            isAttacking = True
      else:
        canClick = True
        
  pygame.display.update()

while (isCredits):
  pygame.time.delay(100) #framerate controller
  for event in pygame.event.get():
    if (event.type == pygame.QUIT):
      isCredits = False

  keys = pygame.key.get_pressed()
  window.fill((200, 200, 200))
  
  if (charactersAlive > 0):
    window.blit(wins[3-charactersAlive], (0, 525))
    #characters
    if (jotaroAlive):
      window.blit(jotaro, (50, 300))
    if (dioAlive):
      window.blit(dio, (150, 300))
    if (johnnyAlive):
      window.blit(johnny, (250, 300))
  else:
    window.blit(loseText, (0, 525))
  pygame.display.update()

pygame.quit()
