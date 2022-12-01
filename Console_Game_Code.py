# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 12:14:33 2022

@author: 19718
"""

import random



'''

CLASS OBJECTS

'''



class Card:
    def __init__(self,color,suit,value,pos=1):
        self.color = color #string
        self.suit = suit #string
        self.value = value #float
        self.pos = pos #int
    def __str__(self): #type print(card object) to return info about the value and suit. The value is rounded when printed because different
                        # suits can have decimal values, which help in gameplay but not user experience
        return "% s of % s" % (round(self.value), self.suit)
    def __repr__(self):
        return "% s of % s (% s)" % (round(self.value), self.suit, self.pos)
        
        
        
'''

ALL FUNCTIONS ARE WRITTEN BELOW

'''        
        
     
        
        
# the build_deck() function returns a list of 52 unique card objects
# g = 1 values for basic games
# g = 2 values for deluxe games (the suits mean more and so decimal values are added to the values)
def build_deck(g=1):
    colors = ["black","red"]
    values = [2,3,4,5,6,7,8,9,10,11,12,13,14] # Ace = 14
    pos = 0
    Deck = [] # KEEPING ALL "HANDS" AS LISTS OF CARD OBJECTS
    for i in colors:      
        if i == "black":
            suits = ["spades","clubs"]
        else:
            suits = ["hearts","diamonds"]    
        for j in suits:
            account = 0
            # If Deluxe game, accounting for different suit hierarchies
            # If Basic game, there is no accounting
            if g == 2:
                if j == "spades":
                    account = 0.4
                elif j == "hearts":
                    account = 0.3
                elif j == "clubs":
                    account = 0.2
                elif j == "diamonds":
                    account = 0.1
            for k in values:
                temp_card = Card(i,j,k+account,pos)
                Deck.append(temp_card)
                pos += 1
    return Deck   
    

# The shuffle() function takes in a list of card objects and randomizes their position.
# returns a list of card objects with a new order, and each card's position now matches
# their order as well. Card object position must always be updated
def shuffle(deck):
    n = len(deck)
    for i in range(n):
        deck[i].pos = random.random()
    deck.sort(key = lambda x: x.pos)  
    return reposition(deck)


# The reposition() function converts the deck card "position" attributes
# to their order integers
# Ex: say a deck has cards with positions (0.21, 0.56, 0.85), the returned positions
# for this deck would be (0,1,2) in their same respective order.
# Ex 2: a deck put through with this list of positions (42,43,45) would return
# (0,1,2) so this helps to normalize decks after an action has been made
def reposition(deck):
    n = len(deck)
    for j in range(n):
        deck[j].pos = j
    return deck



# Equality = "in"
# This function returns a tuple of the odds your next card is inside or outside the
# two cards you have in your hand right now
def find_odds(card1,card2,deck):
  deck_size = len(deck)
  
  # Find what card is low and which is high
  if card1.value > card2.value:
    min_card = card2.value
    max_card = card1.value
  else:
    min_card = card1.value
    max_card = card2.value


  # Going through full deck and checking % of cards which are "in"
  in_count = 0
  for i in range(deck_size):
    if (deck[i].value <= max_card) and (deck[i].value >= min_card):
      in_count += 1
  in_odds = round((in_count/deck_size)*100,2)
  out_odds = round((1-in_count/deck_size)*100,2)

  return (in_odds,out_odds)




# the deal_cards() function will return:
    # 1. a diminished original deck - i.e. there may be 44 cards objects in the deck list 
    # if 4 were dealt to 2 players each)
    # 2. new lists of card objects, depending on how many players there are
    # Variable definitions: d_deck = dealer's deck ; n_players = # of players ; n_cards = # of cards to deal per player
def deal_cards(d_deck, p1_cards = [], p2_cards = [], p3_cards = [], p4_cards = [], n_players = 1, n_cards = 1):
    if n_players == 1:
        p1_cards += d_deck[0:n_cards]
        p1_cards = reposition(p1_cards)
        del d_deck[0:n_cards]
        d_deck = reposition(d_deck)
        return d_deck, p1_cards
    if n_players == 2:
        p1_cards += d_deck[0:2*n_cards-1:2]
        p1_cards = reposition(p1_cards)
        p2_cards += d_deck[1:2*n_cards:2]
        p2_cards = reposition(p2_cards)
        del d_deck[0:2*n_cards]
        d_deck = reposition(d_deck)
        return d_deck, p1_cards, p2_cards
    if n_players == 3:
        p1_cards += d_deck[0:3*n_cards-2:3]
        p1_cards = reposition(p1_cards)
        p2_cards += d_deck[1:3*n_cards-1:3]
        p2_cards = reposition(p2_cards)
        p3_cards += d_deck[2:3*n_cards:3]
        p3_cards = reposition(p3_cards)
        del d_deck[0:3*n_cards]
        d_deck = reposition(d_deck)
        return d_deck, p1_cards, p2_cards, p3_cards
    if n_players == 4:    
        p1_cards += d_deck[0:4*n_cards-3:4]
        p1_cards = reposition(p1_cards)
        p2_cards += d_deck[1:4*n_cards-2:4]
        p2_cards = reposition(p2_cards)
        p3_cards += d_deck[2:4*n_cards-1:4]
        p3_cards = reposition(p3_cards)
        p4_cards += d_deck[3:4*n_cards:4]
        p4_cards = reposition(p4_cards)
        del d_deck[0:4*n_cards]
        d_deck = reposition(d_deck)
        return d_deck, p1_cards, p2_cards, p3_cards, p4_cards
            

### Gameplay Simulation of non-Assisted. Only difference between Basic and Deluxe is the preset card values being slightly different
def PlayAceyDeucey(Deck):
    players = int(input("How many players (1 to 4) are there? "))
    cards = 2
    
    # Setting up all game objects here
    print("Generating House Deck...\n")
    Players = [] #array to hold all player hands
    Player_points = [0]*players #array to hold all player points
    Discard_Pile = []
    
    print("Dealing Cards...\n")
    if players == 1:
        Deck,p1_cards = deal_cards(Deck, n_players=players, n_cards=cards) 
        print("P1 Cards:",p1_cards,"\n")
        Players.append(p1_cards)
        
    elif players == 2:
        Deck,p1_cards,p2_cards = deal_cards(Deck, n_players=players, n_cards=cards) 
        print("P1 Cards:",p1_cards,"\n")
        print("P2 Cards:",p2_cards,"\n")
        Players.append(p1_cards)
        Players.append(p2_cards)
        
    elif players == 3:
        Deck,p1_cards,p2_cards,p3_cards = deal_cards(Deck, n_players=players, n_cards=cards) 
        print("P1 Cards:",p1_cards,"\n")
        print("P2 Cards:",p2_cards,"\n")
        print("P3 Cards:",p3_cards,"\n")
        Players.append(p1_cards)
        Players.append(p2_cards)
        Players.append(p3_cards)
   
    elif players == 4:
        Deck,p1_cards,p2_cards,p3_cards,p4_cards = deal_cards(Deck, n_players=players, n_cards=cards) 
        print("P1 Cards:",p1_cards,"\n")
        print("P2 Cards:",p2_cards,"\n")
        print("P3 Cards:",p3_cards,"\n")
        print("P4 Cards:",p4_cards,"\n")
        Players.append(p1_cards)
        Players.append(p2_cards)
        Players.append(p3_cards)
        Players.append(p4_cards)

        
    ### Starting the Game
    IO = -1
    while IO != "stop":
        for i in range(players):
            input("\nReady Player {0}? Press any key ".format(i+1))
            print("Cards:",Players[i])
            
            # Asking players for "in" or "out". Does not need to account for other inputs,
            # as it will all be preset buttons in the end
            IO = input("In (1) or Out (0)? \"stop\" to end. ")
            
            # Setting data types and implementing stop action if necessary
            if IO == "1":
                IO = 1
                print("Prediction = IN\n")
            elif IO == "0":
                IO = 0
                print("Prediction = OUT\n")
            elif IO == "stop":
                break
                
            # Checking whether "in" or "out" quantitatively. Equality will be counted as "in"
            Deck, Players[i] = deal_cards(Deck,Players[i],n_players=1,n_cards=1)
            val1 = Players[i][0].value
            val2 = Players[i][1].value
            val3 = Players[i][2].value # Newly dealt card
            print("Dealt Card:",Players[i][2])

            
            # Checking if in between/equal or outside
            if (val3>=val1 and val3<=val2) or (val3>=val2 and val3<=val1): # In Between or Equal to
                if IO == 1:
                    print("CORRECT - IN")
                    Player_points[i] += 1
                elif IO == 0:
                    print("INCORRECT - IN")
                    Player_points[i] -= 1
            elif (val3<val1 and val3<val2) or (val3>val2 and val3>val1): # Outside
                if IO == 1:
                    print("INCORRECT - OUT")
                    Player_points[i] -= 1
                elif IO == 0:
                    print("CORRECT - OUT")
                    Player_points[i] += 1
                    
            print("\nPlayer {0} has {1} points\n".format(i+1, Player_points[i]))
            
            #Discarding bottom card of player's hand
            Discard_Pile.append(Players[i][0]) 
            del Players[i][0] 
            Players[i] = reposition(Players[i])
         
        # If the dealer's deck gets diminished too much
        if len(Deck) <= players:
            # moving discarded cards to dealer's deck
            Deck += Discard_Pile
            # resetting discard pile
            Discard_Pile = []
            # shuffling deck
            Deck = shuffle(Deck)
        
  



def PlayAceyDeuceyAssisted(Deck):
    players = int(input("How many players (1 to 4) are there? "))
    cards = 2
    
    # Setting up all game objects here
    print("Generating House Deck...\n")
    Players = [] #array to hold all player hands
    Player_points = [0]*players #array to hold all player points
    Player_odds = [(0,1)]*players
    Discard_Pile = []
    
    print("Dealing Cards...\n")
    if players == 1:
        Deck,p1_cards = deal_cards(Deck, n_players=players, n_cards=cards) 
        print("P1 Cards:",p1_cards,"\n")
        Players.append(p1_cards)
        
    elif players == 2:
        Deck,p1_cards,p2_cards = deal_cards(Deck, n_players=players, n_cards=cards) 
        print("P1 Cards:",p1_cards,"\n")
        print("P2 Cards:",p2_cards,"\n")
        Players.append(p1_cards)
        Players.append(p2_cards)
        
    elif players == 3:
        Deck,p1_cards,p2_cards,p3_cards = deal_cards(Deck, n_players=players, n_cards=cards) 
        print("P1 Cards:",p1_cards,"\n")
        print("P2 Cards:",p2_cards,"\n")
        print("P3 Cards:",p3_cards,"\n")
        Players.append(p1_cards)
        Players.append(p2_cards)
        Players.append(p3_cards)
   
    elif players == 4:
        Deck,p1_cards,p2_cards,p3_cards,p4_cards = deal_cards(Deck, n_players=players, n_cards=cards) 
        print("P1 Cards:",p1_cards,"\n")
        print("P2 Cards:",p2_cards,"\n")
        print("P3 Cards:",p3_cards,"\n")
        print("P4 Cards:",p4_cards,"\n")
        Players.append(p1_cards)
        Players.append(p2_cards)
        Players.append(p3_cards)
        Players.append(p4_cards)

        
    ### Starting the Game
    IO = -1
    while IO != "stop":
        for i in range(players):
            input("\nReady Player {0}? Press any key ".format(i+1))
            print("Cards:",Players[i])
            
            # Using the find_odds function to count cards on the player's behalf.
            # odds is a tuple of (in % chance, out % chance)
            odds = find_odds(Players[i][0],Players[i][1],Deck)
            print("% Chance In =",odds[0],"\n% Chance Out =",odds[1])

            # Asking players for "in" or "out". Does not need to account for other inputs,
            # as it will all be preset buttons in the end
            IO = input("In (1) or Out (0)? \"stop\" to end. ")
            
            # Setting data types and implementing stop action if necessary
            if IO == "1":
                IO = 1
                print("Prediction = IN\n")
            elif IO == "0":
                IO = 0
                print("Prediction = OUT\n")
            elif IO == "stop":
                break
                
            # Checking whether "in" or "out" quantitatively. Equality will be counted as "in"
            Deck, Players[i] = deal_cards(Deck,Players[i],n_players=1,n_cards=1)
            val1 = Players[i][0].value
            val2 = Players[i][1].value
            val3 = Players[i][2].value # Newly dealt card
            print("Dealt Card:",Players[i][2])

            
            # Checking if in between/equal or outside
            if (val3>=val1 and val3<=val2) or (val3>=val2 and val3<=val1): # In Between or Equal to
                if IO == 1:
                    print("CORRECT - IN")
                    Player_points[i] += 1
                elif IO == 0:
                    print("INCORRECT - IN")
                    Player_points[i] -= 1
            elif (val3<val1 and val3<val2) or (val3>val2 and val3>val1): # Outside
                if IO == 1:
                    print("INCORRECT - OUT")
                    Player_points[i] -= 1
                elif IO == 0:
                    print("CORRECT - OUT")
                    Player_points[i] += 1
                    
            print("\nPlayer {0} has {1} points\n".format(i+1, Player_points[i]))
            
            #Discarding bottom card of player's hand
            Discard_Pile.append(Players[i][0]) 
            del Players[i][0] 
            Players[i] = reposition(Players[i])
         
        # If the dealer's deck gets diminished too much
        if len(Deck) <= players:
            # moving discarded cards to dealer's deck
            Deck += Discard_Pile
            # resetting discard pile
            Discard_Pile = []
            # shuffling deck
            Deck = shuffle(Deck)


  
        
'''

RUNNING THE GAME

'''
        
print("(1) - Basic Acey Deucey")
print("(2) - Deluxe Acey Deucey")
print("(3) - Assisted Basic Acey Deucey")
print("(4) - Assisted Deluxe Acey Deucey")
game = int(input())

if game == 1:
    PlayAceyDeucey(shuffle(build_deck(1)))
elif game == 2:
    PlayAceyDeucey(shuffle(build_deck(2)))
elif game == 3:
    PlayAceyDeuceyAssisted(shuffle(build_deck(1)))
elif game == 4:
    PlayAceyDeuceyAssisted(shuffle(build_deck(2)))