import random
import art
def blackJack():
  print(art.logo)

  #define card deck
  cards=["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
  #define new card
  def newCard():
    return random.choice(cards)
  #set get score function
  def getScore(x):
    #set black jack condition
    if len(x)==2 and "A" in x and 10 in x:
      Score="Black Jack"
      return Score
    #set A to 11 
    elif "A" in x:
      x[x.index("A")]=11
    #check if score is over 21
    Score=sum(x)
    if Score<=21:
      return Score
    else:
      #set A to 1 if score is over 21
      if 11 in x:
        x[x.index(11)]=1
      Score=sum(x)    
      return Score
  #set win and lose
  def lose():
    print("You lose.")
    gameStart()
  def win():
    print("You win!")
    gameStart()
  #set player cards 
  playerCards=[newCard(),newCard()]
  #get player score
  def getPlayerScore():
    return getScore(playerCards)
  #set dealer card
  dealerCards=[newCard(),newCard()]
  #get dealer score
  def getDealerScore():
     return getScore(dealerCards)
   

  #define print current information function
  def printPlayerInfo():
   return print(f"Your cards: {playerCards}, current score {getPlayerScore()}")
  def printDealerInfo():
   return print(f"dealer cards:{dealerCards}, current score {getDealerScore()}")
  #print player hand information first time
  printPlayerInfo()
  #print dealer's first card
  print(f"Dealer's first card: {dealerCards[0]}")
  #check to see if player got black jack
  if getPlayerScore()=="Black Jack":
    printDealerInfo()
    win()
  #set a variable for standing status
  stand=False
  #check if player want to hit or stand
  while stand==False:
    hitOrStand=input('Type "y" to get another card, type "n" to pass  ')
    #if hit
    if hitOrStand=="y":
      #add new card to the hands
      playerCards.append(newCard())
      getPlayerScore()
      printPlayerInfo()
      #if player bust
      if getPlayerScore()>21:
        stand=True
        printDealerInfo()
        lose()
      #if stand
    elif hitOrStand=="n":
      stand=True
      
    else:
      print("Invalid input.")
  #print player final information
  print(f"Your final hand:{playerCards}, Your final score:{getPlayerScore()}")
  #let player know dealer's cards
  printDealerInfo()
  #define dealer's action
  def dealerAction():
    #check if dealer gets black jack
    if getDealerScore()=="Black Jack":
     lose()
     #if dealer score is under 17 draw card
    while getDealerScore()<17:
     dealerCards.append(newCard())
     getDealerScore()
     printDealerInfo()
     #if dealer score is under 21 compare score
   if getDealerScore()<=21:
     if getPlayerScore()==getDealerScore():
       print("It's a draw but you lose.")
     elif getPlayerScore()>getDealerScore():
       win()
     else:
       lose()
     #if dealer is over 21 then win
   else:
     win()
     #call dealer action
  dealerAction()
def gameStart():  
  gamestart=input("Play black jack? Type yes to start \n")
  if gamestart=="yes":
     blackJack()
  else:
    while gamestart!="start":
     gamestart=input("Type start when ready.")

gameStart()