# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:01:44 2022

@author: custom
"""
from tkinter import *
#from tkinter.ttk import *
import random
from PIL import Image, ImageTk

master = Tk()
 
def resize_cards(card):
    our_card_img = Image.open(card)
    our_card_resize_image = our_card_img.resize((150,218))
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)
    return our_card_image
    
master.geometry("900x500")
master.title("ACEY DUCEY")
#master.configure(background="green")'

def shuffle_1():
    
    # clear all the old cards from previus the game
    global card_back_Image_1
    card_back_Image_1 = resize_cards(f'cards/Card Back.png')
    
    Card_3_label.config(image = card_back_Image_1)
    Card_2_label.config(image = card_back_Image_1)
    Card_1_label.config(image = card_back_Image_1)
    
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2, 15)
	# 11 = Jack, 12=Queen, 13=King, 14 = Ace

    global deck
    deck =[]

    for suit in suits:
            for value in values:
                   deck.append(f'{value}_of_{suit}')
	# Create our players
    
    global player
    
    player = []
     
    card1 = random.choice(deck)
    deck.remove(card1)
    player.append(card1)
    # Card_1_label.config(text = card)
    
    global Card1_image
    Card1_image = resize_cards(f'cards/{card1}.png')
    Card_1_label.config(image=Card1_image)
    
    card2 = random.choice(deck)
    deck.remove(card2)
    player.append(card2)
    #Card_2_label.config(text = card)
    global Card2_image
    Card2_image = resize_cards(f'cards/{card2}.png')
    Card_2_label.config(image=Card2_image)
    
def shuffle_1_assisted_basic():
    
    # clear all the old cards from previus the game
    global card_back_Image_1
    card_back_Image_1 = resize_cards(f'cards/Card Back.png')
    
    Card_3_label.config(image = card_back_Image_1)
    Card_2_label.config(image = card_back_Image_1)
    Card_1_label.config(image = card_back_Image_1)
    
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2, 15)
	# 11 = Jack, 12=Queen, 13=King, 14 = Ace

    global deck
    deck =[]

    for suit in suits:
            for value in values:
                   deck.append(f'{value}_of_{suit}')
	# Create our players
    
    global player
    
    player = []
     
    card1 = random.choice(deck)
    deck.remove(card1)
    player.append(card1)
    # Card_1_label.config(text = card)
    
    global Card1_image
    Card1_image = resize_cards(f'cards/{card1}.png')
    Card_1_label.config(image=Card1_image)
    
    card2 = random.choice(deck)
    deck.remove(card2)
    player.append(card2)
    #Card_2_label.config(text = card)
    global Card2_image
    Card2_image = resize_cards(f'cards/{card2}.png')
    Card_2_label.config(image=Card2_image)
    
    find_odds_basic()
    
def find_odds_basic():  
    
    hand = []
    hand = [eval(item.split('_',1)[0]) for item in player]
    deck_size = len(deck)
  
  # Find what card is low and which is high
    if hand[0] > hand[1]:
        min_card = hand[1]
        max_card = hand[0]
    else:
        min_card = hand[0]
        max_card = hand[1]
    
        

    deck_odds = [eval(item.split('_',1)[0]) for item in deck]
  # Going through full deck and checking % of cards which are "in"
    in_count = 0
    for i in range(deck_size):
        
            
        if (deck_odds[i] < max_card) and (deck_odds[i] > min_card):
              in_count += 1
        in_odds = round((in_count/deck_size)*100,2)
        out_odds = round((1-in_count/deck_size)*100,2)
           
    print ('% Chance in:',in_odds,'while', '% Chance out:',out_odds)
    
def shuffle_1_assisted_deluxe():
    pass
    
def find_odds_deluxe():
    pass


def shuffle_1_deluxe():
    global card_back_Image_1
    card_back_Image_1 = resize_cards(f'cards/Card Back.png')
    # clear all the old cards from previus the game
    Card_3_label.config(image = card_back_Image_1)
    Card_2_label.config(image = card_back_Image_1)
    Card_1_label.config(image = card_back_Image_1)
    
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2, 15)
	# 11 = Jack, 12=Queen, 13=King, 14 = Ace

    global deck
    deck =[]

    for suit in suits:
            for value in values:
                   deck.append(f'{value}_of_{suit}')
	# Create our players
    
    global player
    
    player = []
     
    card1 = random.choice(deck)
    deck.remove(card1)
    player.append(card1)
    # Card_1_label.config(text = card)
    
    global Card1_image
    Card1_image = resize_cards(f'cards/{card1}.png')
    Card_1_label.config(image=Card1_image)
    
    card2 = random.choice(deck)
    deck.remove(card2)
    player.append(card2)
    #Card_2_label.config(text = card)
    global Card2_image
    Card2_image = resize_cards(f'cards/{card2}.png')
    Card_2_label.config(image=Card2_image)
  
    
    
def player_in():
    
    player_card = random.choice(deck)
    deck.remove(player_card)
    player.append(player_card)
    #Card_3_label.config(text = player_card)
    
    global Card3_image
    Card3_image = resize_cards(f'cards/{player_card}.png')
    Card_3_label.config(image=Card3_image)
    check()
    

def player_out():
    
    player_card = random.choice(deck)
    deck.remove(player_card)
    player.append(player_card)
    #Card_3_label.config(text = player_card)
    global Card3_image
    Card3_image = resize_cards(f'cards/{player_card}.png')
    Card_3_label.config(image=Card3_image)
    
    check_out()
    
def player_in_deluxe():
    
    player_card = random.choice(deck)
    deck.remove(player_card)
    player.append(player_card)
    #Card_3_label.config(text = player_card)
    
    global Card3_image
    Card3_image = resize_cards(f'cards/{player_card}.png')
    Card_3_label.config(image=Card3_image)
    check_deluxe()
    

def player_out_deluxe():
    
    player_card = random.choice(deck)
    deck.remove(player_card)
    player.append(player_card)
    #Card_3_label.config(text = player_card)
    global Card3_image
    Card3_image = resize_cards(f'cards/{player_card}.png')
    Card_3_label.config(image=Card3_image)
    
    check_out_deluxe()
    
def check():
    
    result = [item.split('_',1)[0] for item in player]
    for i in range(0, len(result)):
        
        result[i] = int(result[i])
        
    print(result)
    
    if (result[0]<=result[2]<=result[1]) or (result[1]<=result[2]<=result[0]):
        
        win()
    else:
        
        lose()
        
def check_out():
    
    result = [item.split('_',1)[0] for item in player]
    for i in range(0, len(result)):
        
        result[i] = int(result[i])
        
    print(result)
    
    if (result[0]>result[2]>result[1]) or (result[1]>result[2]>result[0]):
        
        lose()
    else:
        
        win()
        
def check_deluxe():
    
    result = [item.split('_',1)[0] for item in player]
    result2 = [item.split('_',2)[2] for item in player]
    # Card ranks
    #1 = clubs, 2 = diamonds, 3= hearts, 4= spades
    account = []
    for i in result2:
        print(i)
        if i == 'clubs':
            account.append(int(1))
        elif i == 'diamonds':
            account.append(int(2))
        elif i == 'hearts':
            account.append(int(3))
        elif i == 'spades':
            account.append(int(4))
        
    for i in range(0, len(result)):
        result[i] = int(result[i])
        
    if result[2] == result[0]:
        if account[2]<account[0]:
            lose()
        else:
            win()
            
    elif result[2] == result[1]:
        if account[2]<account[1]:   
            lose()
        else:
            win()

    if (result[0]<result[2]<result[1]) or (result[1]<result[2]<result[0]):
        win()
        
    else:
        
        lose()
        
        
def check_out_deluxe():
    
    result = [item.split('_',1)[0] for item in player]
    result2 = [item.split('_',2)[2] for item in player]
    # Card ranks
    #1 = clubs, 2 = diamonds, 3= hearts, 4= spades
    account = []
    for i in result2:
        print(i)
        if i == 'clubs':
            account.append(int(1))
        elif i == 'diamonds':
            account.append(int(2))
        elif i == 'hearts':
            account.append(int(3))
        elif i == 'spades':
            account.append(int(4))
        
    #print(account)
    
    for i in range(0, len(result)):
        
        result[i] = int(result[i])
        
    #print(result)
    
    if result[2] == result[0]:
        
        if account[2]>account[0]:
            
            win()
        else:
            lose()
            
    
    elif result[2] == result[1]:
        
        if account[2]>account[1]:
            
            win()
        else:
            
            lose()
    
    
    if (result[0]<result[2]<result[1]) or (result[1]<result[2]<result[0]):
        
        lose()
        
    else:
        
        win()
    
def win():
    
    my_frame = Frame(newWindow, bg = "green")
    my_frame.pack(pady=20)
    
    Win_frame = LabelFrame(my_frame, text=" YOU WIN", bd = 0)
    Win_frame.grid(row=0, column=4, padx=10, ipadx=10)
    
    Win_label = Label(Win_frame, text='')
    Win_label.grid(row = 0, column = 4, pady=20, padx = 20)
    
    pass

def lose():
    
    my_frame = Frame(newWindow, bg = "green")
    my_frame.pack(pady=20)
    
    lose_frame = LabelFrame(my_frame, text=" YOU LOSE", bd = 0)
    lose_frame.grid(row=0, column=4, padx=20, ipadx=20)
    
    lose_label = Label(lose_frame, text='')
    lose_label.grid(row = 0, column = 4, pady=20, padx = 20)
    
    pass

def player_1():
    global newWindow
    newWindow = Toplevel(master)
    newWindow.title("New Window")
    newWindow.geometry("900x500")
    newWindow.configure(background = "green")
    Label(newWindow, text ="Welcome to the game", bg = 'green', font='broadway 18').pack()
    
    my_frame = Frame(newWindow, bg = "green")
    my_frame.pack(pady=20) 

    global Card_1_label, Card_2_label, Card_3_label

    # Create Frames For Cards
    Card_1_frame = LabelFrame(my_frame, text="Card 1", bd = 0)
    Card_1_frame.grid(row=0, column=0, padx=20, ipadx=20)

    Card_2_frame = LabelFrame(my_frame, text="Card 2", bd = 0)
    Card_2_frame.grid(row=0, column=1, ipadx=20)
    
    Card_3_frame = LabelFrame(my_frame, text="Card 3", bd = 0)
    Card_3_frame.grid(row=0, column=2, ipadx=20)

    # Put cards in frames
    Card_1_label = Label(Card_1_frame, text='')
    Card_1_label.grid(row = 0, column = 0, pady=20, padx = 20)

    Card_2_label = Label(Card_2_frame, text='')
    Card_2_label.grid(row = 0, column = 1, pady=20, padx = 20)
    
    Card_3_label = Label(Card_3_frame, text='')
    Card_3_label.grid(row = 0, column = 3, pady=20, padx = 20)
    
    #button frame
    button_frame = Frame(newWindow, bg = "green")
    button_frame.pack(pady= 20)
    
    In_button = Button(button_frame, text = "Next card is in between", font = ("Helvetica", 14), command = player_in)
    In_button.grid(row = 0, column = 2)

    Out_button = Button(button_frame, text = "Next card is NOT in between", font = ("Helvetica", 14), command= player_out)
    Out_button.grid(row = 0, column = 3)
    # Create a couple buttons
    shuffle_button = Button(button_frame, text=" Get Cards", font=("Helvetica", 14), command=shuffle_1)
    shuffle_button.grid(row = 0, column = 0)

def player_1_deluxe():
    global newWindow
    newWindow = Toplevel(master)
    newWindow.title("New Window")
    newWindow.geometry("900x500")
    newWindow.configure(background = "green")
    Label(newWindow, text ="Welcome to the Deluxe mode", bg = 'green', font='broadway 18').pack()
    
    my_frame = Frame(newWindow, bg = "green")
    my_frame.pack(pady=20) 

    global Card_1_label, Card_2_label, Card_3_label

    # Create Frames For Cards
    Card_1_frame = LabelFrame(my_frame, text="Card 1", bd = 0)
    Card_1_frame.grid(row=0, column=0, padx=20, ipadx=20)

    Card_2_frame = LabelFrame(my_frame, text="Card 2", bd = 0)
    Card_2_frame.grid(row=0, column=1, ipadx=20)
    
    Card_3_frame = LabelFrame(my_frame, text="Card 3", bd = 0)
    Card_3_frame.grid(row=0, column=2, ipadx=20)

    # Put cards in frames
    Card_1_label = Label(Card_1_frame, text='')
    Card_1_label.grid(row = 0, column = 0, pady=20, padx = 20)

    Card_2_label = Label(Card_2_frame, text='')
    Card_2_label.grid(row = 0, column = 1, pady=20, padx = 20)
    
    Card_3_label = Label(Card_3_frame, text='')
    Card_3_label.grid(row = 0, column = 3, pady=20, padx = 20)
    
   
    
    
    #button frame
    button_frame = Frame(newWindow, bg = "green")
    button_frame.pack(pady= 20)
    
    In_button = Button(button_frame, text = "Next card is in between", font = ("Helvetica", 14), command = player_in_deluxe)
    In_button.grid(row = 0, column = 2)

    Out_button = Button(button_frame, text = "Next card is NOT in between", font = ("Helvetica", 14), command= player_out_deluxe)
    Out_button.grid(row = 0, column = 3)
    # Create a couple buttons
    shuffle_button = Button(button_frame, text=" Get Cards", font=("Helvetica", 14), command=shuffle_1_deluxe)
    shuffle_button.grid(row = 0, column = 0)
    # card_button = Button(button_frame, text="Get Cards", font=("Helvetica", 14)) #command=deal_cards)
    # card_button.grid(row = 0, column = 1)

def player_1_assisted():
    global newWindow
    newWindow = Toplevel(master)
    newWindow.title("New Window")
    newWindow.geometry("900x500")
    newWindow.configure(background = "green")
    Label(newWindow, text ="Welcome to the game", bg = 'green', font='broadway 18').pack()
    
    my_frame = Frame(newWindow, bg = "green")
    my_frame.pack(pady=20) 

    global Card_1_label, Card_2_label, Card_3_label

    # Create Frames For Cards
    Card_1_frame = LabelFrame(my_frame, text="Card 1", bd = 0)
    Card_1_frame.grid(row=0, column=0, padx=20, ipadx=20)

    Card_2_frame = LabelFrame(my_frame, text="Card 2", bd = 0)
    Card_2_frame.grid(row=0, column=1, ipadx=20)
    
    Card_3_frame = LabelFrame(my_frame, text="Card 3", bd = 0)
    Card_3_frame.grid(row=0, column=2, ipadx=20)

    # Put cards in frames
    Card_1_label = Label(Card_1_frame, text='')
    Card_1_label.grid(row = 0, column = 0, pady=20, padx = 20)

    Card_2_label = Label(Card_2_frame, text='')
    Card_2_label.grid(row = 0, column = 1, pady=20, padx = 20)
    
    Card_3_label = Label(Card_3_frame, text='')
    Card_3_label.grid(row = 0, column = 3, pady=20, padx = 20)
    
    #button frame
    button_frame = Frame(newWindow, bg = "green")
    button_frame.pack(pady= 20)
    
    In_button = Button(button_frame, text = "Next card is in between", font = ("Helvetica", 14), command = player_in)
    In_button.grid(row = 0, column = 2)

    Out_button = Button(button_frame, text = "Next card is NOT in between", font = ("Helvetica", 14), command= player_out)
    Out_button.grid(row = 0, column = 3)
    # Create a couple buttons
    shuffle_button = Button(button_frame, text=" Get Cards", font=("Helvetica", 14), command=shuffle_1)
    shuffle_button.grid(row = 0, column = 0)
    
    probability_button = Button(button_frame, text="Probability", font=("Helvetica", 14), command=shuffle_1_assisted_basic)
    probability_button.grid(row = 0, column = 5)
    
    

def player_2():
    
    newWindow = Toplevel(master)
    newWindow.title("New Window")
    newWindow.geometry("900x500")
    newWindow.configure(bg = 'green')
    Label(newWindow, text ="Welcome to the game", bg = 'green', font='broadway 18').pack()
    pass

def player_2_deluxe():
    
    newWindow = Toplevel(master)
    newWindow.title("New Window")
    newWindow.geometry("900x500")
    newWindow.configure(bg = 'green')
    Label(newWindow, text ="Welcome to the game", bg = 'green', font='broadway 18').pack()
    pass
# function to open a new window
# on a button click
def Basic_Acey_Ducey():
     
    newWindow = Toplevel(master)
    newWindow.title("LIFE IS A GAME - PLAY TO WIN")
    newWindow.geometry("900x500")
    newWindow.configure(bg = 'green')
    Label(newWindow, text ="Welcome to Basic Acey Ducey", font='broadway 18', bg = 'green').pack()
    Label(newWindow, text = "how many players are there?", bg = 'green', font='castellar 10 bold').pack()
        
    button_player_1 = Button(newWindow, text = "1 Player", command = player_1, activebackground="#87C1FF", activeforeground="#fff", font= 'castellar 12 bold')
    button_player_1.pack(pady = 10)
    button_player_1.bind("<Enter>", on_enter)
    button_player_1.bind("<Leave>", on_leave)
    
    button_player_2 = Button(newWindow, text = "2 Players", command = player_2,  activebackground="#87C1FF", activeforeground="#fff", font= 'castellar 12 bold')
    button_player_2.pack(pady = 10)
    button_player_2.bind("<Enter>", on_enter)
    button_player_2.bind("<Leave>", on_leave)
    

    
    
def Deluxe_Acey_Ducey():
    
    newWindow = Toplevel(master)
    newWindow.title("New Window")
    newWindow.geometry("900x500")
    newWindow.configure(bg = 'green')
    Label(newWindow, text ="Welcome to Deluxe Acey Ducey", font='broadway 18', bg = 'green').pack()
    
    Label(newWindow, text = "how many players are there?", bg = 'green', font='castellar 10 bold').pack()
    
    button_player_1 = Button(newWindow, text = "1 Player", command = player_1_deluxe, activebackground="#87C1FF", activeforeground="#fff", font= 'castellar 12 bold')
    button_player_1.pack(pady = 10)
    button_player_1.bind("<Enter>", on_enter)
    button_player_1.bind("<Leave>", on_leave)
    
    button_player_2 = Button(newWindow, text = "2 Players", command = player_2_deluxe, activebackground="#87C1FF", activeforeground="#fff", font= 'castellar 12 bold')
    button_player_2.pack(pady = 10)
    button_player_2.bind("<Enter>", on_enter)
    button_player_2.bind("<Leave>", on_leave)

 
def Assisted_Basic_Acey_Ducey():
     
    newWindow = Toplevel(master)
    newWindow.title("New Window")
    newWindow.geometry("900x500")
    newWindow.configure(bg = 'green')
 
    Label(newWindow,
          text ="Welcome to Asissted Basic Acey Ducey", font='broadway 18', bg = 'green').pack()
    
    Label(newWindow, text = "how many players are there?", bg = 'green', font='castellar 10 bold').pack()
    
    button_player_1 = Button(newWindow, text = "1 Player", command = player_1_assisted, activebackground="#87C1FF", activeforeground="#fff", font= 'castellar 12 bold')
    button_player_1.pack(pady = 10)
    button_player_1.bind("<Enter>", on_enter)
    button_player_1.bind("<Leave>", on_leave)
    
    button_player_2 = Button(newWindow, text = "2 Players", activebackground="#87C1FF", activeforeground="#fff", font= 'castellar 12 bold')
    button_player_2.pack(pady = 10)
    button_player_2.bind("<Enter>", on_enter)
    button_player_2.bind("<Leave>", on_leave)
    

def Assisted_Deluxe_Acey_Ducey():

    newWindow = Toplevel(master)
    newWindow.title("New Window")
 
    newWindow.geometry("900x500")
    newWindow.configure(bg = 'green')
 
    Label(newWindow, text ="Welcome to Assisted Deluxe Acey Ducey", font='broadway 18', bg = 'green').pack()
    
    Label(newWindow, text = "how many players are there?", bg = 'green', font='castellar 10 bold').pack()
    
    button_player_1 = Button(newWindow, text = "1 Player", font= 'castellar 12 bold')
    button_player_1.pack(pady = 10)
    button_player_1.bind("<Enter>", on_enter)
    button_player_1.bind("<Leave>", on_leave)
    
    button_player_2 = Button(newWindow, text = "2 Players", font= 'castellar 12 bold')
    button_player_2.pack(pady = 20)
    button_player_2.bind("<Enter>", on_enter)
    button_player_2.bind("<Leave>", on_leave)

# MAIN WINDOW BUTTONS

def on_enter(e):
    e.widget['background'] = "#FF6863"

def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'
    
master.configure(bg='green')
label = Label(master, text ="LIFE IS A GAME - PLAY TO WIN!", font='broadway 18')
label.pack(pady = 10)
label.configure(bg = 'green')

btn_1 = Button(master, text =" BASIC ACEY DUCEY ", command = Basic_Acey_Ducey, activebackground="#87C1FF", activeforeground="#fff", font= 'castellar 12 bold')
btn_1.pack(pady = 10)
btn_1.bind("<Enter>", on_enter)
btn_1.bind("<Leave>", on_leave)

btn_2 = Button(master, text =" DELUXE ACEY DUCEY ",command = Deluxe_Acey_Ducey, activebackground="#87C1FF", activeforeground="#fff", font= 'castellar 12 bold')
btn_2.pack(pady = 10)
btn_2.bind("<Enter>", on_enter)
btn_2.bind("<Leave>", on_leave)
     
btn_3 = Button(master, text = " ASSISSTED BASIC ACEY DUCEY", command = Assisted_Basic_Acey_Ducey, activebackground="#87C1FF", activeforeground="#fff", font= 'castellar 12 bold')
btn_3.pack(pady = 10)
btn_3.bind("<Enter>", on_enter)
btn_3.bind("<Leave>", on_leave)

btn_4 = Button(master, text =" ASSISSTED DELUX ACEY DUCEY", command = Assisted_Deluxe_Acey_Ducey, activebackground="#87C1FF", activeforeground="#fff", font= 'castellar 12 bold')
btn_4.pack(pady = 10)
btn_4.bind("<Enter>", on_enter)
btn_4.bind("<Leave>", on_leave)

########## LARISSA MODIFIED CODE, IMAGE HERE ##########
cards = Image.open("transparent_cards2.png")
resized_img = cards.resize((250,200))
img = ImageTk.PhotoImage(resized_img)
label_image = Label(master, image = img)
label_image.pack(pady = 20)
mainloop()

# label = Label(master, text ="LIFE IS A GAME - PLAY TO WIN!")
# label.pack(pady = 10)
 
# btn_1 = Button(master, text =" BASIC ACEY DUCEY ", command = Basic_Acey_Ducey)
# btn_1.pack(pady = 10)

# btn_2 = Button(master, text =" DELUXE ACEY DUCEY ",command = Deluxe_Acey_Ducey)
# btn_2.pack(pady = 10)
 
# btn_3 = Button(master, text = " ASSISSTED BASIC ACEY DUCEY", command = Assisted_Basic_Acey_Ducey)
# btn_3.pack(pady = 10)

# btn_4 = Button(master, text =" ASSISSTED DELUX ACEY DUCEY", command = Assisted_Deluxe_Acey_Ducey)
# btn_4.pack(pady = 10)
 
# mainloop, runs infinitely