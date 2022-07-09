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
isRules = False;
busyCounter = 30;
damageDealt = 0

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
dioDamage = 50
#johnny
johnnyAlive = True
#dice
val = 0

#image importing
#main menu
arrow = pygame.image.load("Arrow.png") #100, 25
playButton = pygame.image.load("PlayButton.png") #150, 100
rulesButton = pygame.image.load("RulesButton.png")
titleText = pygame.image.load("Title.png") #250, 100
rules = pygame.image.load("Rules.png") #800, 800
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
prizes = [pygame.image.load("Prize1.png"), pygame.image.load("Prize2.png"), pygame.image.load("Prize3.png"), pygame.image.load("Prize4.png"), pygame.image.load("Prize5.png")]
busyText = [pygame.image.load("Jotaro_busy.png"), pygame.image.load("Dio_busy.png"), pygame.image.load("Johnny_busy.png")]

#animations
jotaroFrames = [pygame.image.load("JotaroFrames/Jotaro_attack1.png"), pygame.image.load("JotaroFrames/Jotaro_attack2.png"), pygame.image.load("JotaroFrames/Jotaro_attack3.png"), pygame.image.load("JotaroFrames/Jotaro_attack4.png"), pygame.image.load("JotaroFrames/Jotaro_attack5.png"), pygame.image.load("JotaroFrames/Jotaro_attack6.png"), pygame.image.load("JotaroFrames/Jotaro_attack7.png"), pygame.image.load("JotaroFrames/Jotaro_attack8.png"), pygame.image.load("JotaroFrames/Jotaro_attack9.png"), pygame.image.load("JotaroFrames/Jotaro_attack10.png")]
jotaroAttackCounter = 0
dioFrames = [pygame.image.load("DioFrames/Dio_attack1.png"), pygame.image.load("DioFrames/Dio_attack2.png"), pygame.image.load("DioFrames/Dio_attack3.png"), pygame.image.load("DioFrames/Dio_attack4.png"), pygame.image.load("DioFrames/Dio_attack5.png"), pygame.image.load("DioFrames/Dio_attack6.png"), pygame.image.load("DioFrames/Dio_attack7.png"), pygame.image.load("DioFrames/Dio_attack8.png"), pygame.image.load("DioFrames/Dio_attack9.png"), pygame.image.load("DioFrames/Dio_attack10.png")]
dioAttackCounter = 0
johnnyFrames = [pygame.image.load("JohnnyFrames/Johnny_attack1.png"), pygame.image.load("JohnnyFrames/Johnny_attack2.png"), pygame.image.load("JohnnyFrames/Johnny_attack3.png"), pygame.image.load("JohnnyFrames/Johnny_attack4.png"), pygame.image.load("JohnnyFrames/Johnny_attack5.png"), pygame.image.load("JohnnyFrames/Johnny_attack6.png"), pygame.image.load("JohnnyFrames/Johnny_attack7.png"), pygame.image.load("JohnnyFrames/Johnny_attack8.png"), pygame.image.load("JohnnyFrames/Johnny_attack9.png"), pygame.image.load("JohnnyFrames/Johnny_attack10.png"), pygame.image.load("JohnnyFrames/Johnny_attack11.png"), pygame.image.load("JohnnyFrames/Johnny_attack12.png"), pygame.image.load("JohnnyFrames/Johnny_attack13.png"), pygame.image.load("JohnnyFrames/Johnny_attack14.png"), pygame.image.load("JohnnyFrames/Johnny_attack15.png"), pygame.image.load("JohnnyFrames/Johnny_attack16.png"), pygame.image.load("JohnnyFrames/Johnny_attack17.png"), pygame.image.load("JohnnyFrames/Johnny_attack18.png"), pygame.image.load("JohnnyFrames/Johnny_attack19.png"), pygame.image.load("JohnnyFrames/Johnny_attack20.png")]
johnnyAttackCounter = 0
diavoloFrames = [diavolo, diavolo, diavolo, pygame.image.load("Data_diavolo4.png"), pygame.image.load("Data_diavolo5.png")]
diavoloFrameCounter = 0;

#sounds
music = pygame.mixer.music.load("il_vento_doro.mp3")
roadRollerSound = pygame.mixer.Sound("ROAD_ROLLER_DA.mp3")
kingCrimsonSound = pygame.mixer.Sound("Diavolo_King_Crimson.mp3")
starPlatinumSound = pygame.mixer.Sound("Star_platinum.mp3")
tuskSound = pygame.mixer.Sound("Tusk_cry.mp3")

while (isRunning and charactersAlive > 0):
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
      window.blit(rulesButton, (375, 525))
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
          isRules = True;
          isMainMenu = False;
          
    elif (isRules):
      window.blit(rules, (0, 0));
      if (keys[pygame.K_z]):
        isRules = False;
        isMainMenu = True;
          
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
        #chooseState = 0
          
      elif (isAttacking): #used, then is effective, and whatnot
        if (usesCounter > 0):
          usesCounter -= 1
          window.blit(uses[activeFightState], (0, 525))
          if (activeFightState == 0):
            pygame.mixer.music.pause()
            jotaroAttackCounter += 1;
            if (jotaroAttackCounter == 10):
              jotaroAttackCounter = 0
            if(usesCounter == 19):
              starPlatinumSound.play()
            window.blit(dice[num1-1], (500, 350))
            window.blit(dice[num2-1], (600, 350))
            window.blit(jotaroFrames[jotaroAttackCounter], (50, 300))
          elif (activeFightState == 1):
            dioAttackCounter += 1;
            if (dioAttackCounter == 10):
              dioAttackCounter = 0
            dioAlive = False
            pygame.mixer.music.pause()
            if(usesCounter == 19):
              roadRollerSound.play()
            window.blit(dioFrames[dioAttackCounter], (150, 300))
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
            window.blit(johnnyFrames[johnnyAttackCounter], (250, 300))
            johnnyAttackCounter += 1
            if(usesCounter == 19):
              tuskSound.play()
            window.blit(dice[num1-1], (500, 350))
        elif (effectiveCounter >= 0): #decide the dice roll's effectiveness
          if(usesCounter == 0):
            val = random.randint(1, 6)
            chooseState = 0
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
            pygame.mixer.music.unpause()
            jotaroAttackCounter = 0
            if (activeFightState == 0 and attackWorks):
              diavoloHealth -= jotaroDamage
              damageDealt += jotaroDamage
              diavoloFrameCounter += 1
            elif (activeFightState == 1 and attackWorks):
              diavoloHealth -= dioDamage
              damageDealt += dioDamage
              diavoloFrameCounter += 1
            elif (attackWorks):
              diavoloHealth -= 100
              damageDealt += 100
              diavoloFrameCounter += 2
              
            if (activeFightState == 0):
              jotaroAlive = False
              charactersAlive -= 1
            elif (activeFightState == 1):
              dioAlive = False
              charactersAlive -= 1
            else:
              johnnyAlive = False
              charactersAlive -= 1;
		        
            #if (activeFightState == 1):
              #pygame.mixer.music.unpause()
		        
            effectiveCounter = -1
        
        elif (busyCounter >= 0):
          busyCounter -= 1
          window.blit(busyText[activeFightState], (0, 525));
        else:
          isAttacking = False
          busyCounter = 30
          effectiveCounter = 40
          usesCounter = 20
          isAttacks = True
          chooseState = 0
          
        #window.blit(dice[num1-1], (500, 350))
        #window.blit(dice[num2-1], (600, 350))
      

      #Choose
          
      #health bar background
      pygame.draw.rect(window, (125, 125, 125), (495, 28.5, 210, 10))
      pygame.draw.rect(window, (175, 175, 175), (500, 30, 200, 5))
      #diavolo
      if (diavoloHealth >= 0):
        pygame.draw.rect(window, (0, 255, 0), (500, 30, (diavoloHealth * 2), 5))
      else:
        pygame.draw.rect(window, (255, 0, 0), (500, 30, ((damageDealt - 100) * 2), 5))
      window.blit(diavoloFrames[diavoloFrameCounter], (450, 0))
      
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
  
  if (damageDealt == 0):
    window.blit(prizes[0], (0, 525))
  elif (damageDealt == 50):
    window.blit(prizes[1], (0, 525))
  elif (damageDealt == 100):
    window.blit(prizes[2], (0, 525))
  elif (damageDealt == 150):
    window.blit(prizes[3], (0, 525))
  else:
    window.blit(prizes[4], (0, 525))
  
  pygame.draw.rect(window, (125, 125, 125), (495, 28.5, 210, 10))
  pygame.draw.rect(window, (175, 175, 175), (500, 30, 200, 5))
  if (diavoloHealth >= 0):
    pygame.draw.rect(window, (0, 255, 0), (500, 30, (diavoloHealth * 2), 5))
  else:
    pygame.draw.rect(window, (255, 0, 0), (500, 30, ((damageDealt - 100) * 2), 5))
  window.blit(diavoloFrames[diavoloFrameCounter], (450, 0))
    
  pygame.display.update()

pygame.quit()
