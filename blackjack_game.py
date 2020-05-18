import random
suits=('Hearts','Diamonds ','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','King','Queen','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'King':10,'Queen':10,'Ace':11}
playing=True

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank+" of "+self.suit

#-------now we store the 52 card object in a list so that we can later shuffle it
class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))#we will have a list of a bunch of card classes
    #this below function will only be called if we print out our deck..basically a list of objects
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp+='\n'+card.__str__()#print out string representation of each indivisual card
        return "The deck has:"  +deck_comp
    def shuffle(self):
        random.shuffle(self.deck)#does not return anything just shuffles the deck

    def deal(self):
        single_card=self.deck.pop()#grab the deck attribute of this deck class and pop of a card item and store to single_card
        return single_card

#the below class will represent what card is currently in someones hand
#we will call deal function,grabbing a card and placing it into someones hand
class Hand:
    def __init__(self):
        self.cards=[] #empty list to start with as we did in the Deck class
        self.value=0  #starts with zero value it is the current sum for the value in the hand
        self.aces=0   #attribute to keep track of aces

    def add_card(self,card):
        #card passed in will be from the deck...Deck.deal(0 --->single Card(suit,rank)
        self.cards.append(card)
        self.value+=values[card.rank]#add the value of the card acc to rank from values dictionary to the value of card in hand
        if card.rank=='Ace':
            self.aces+=1
    def adjust_for_ace(self):
        #if the total value>21 and i still have a ace
        #then change ace from 11 to 1
        while self.value>21 and self.aces>0:
            self.value-=10
            self.aces-=1#now our ace will act as 1

class Chips:

    def __init__(self,total=100):
        self.total=total
        self.bet=0

    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet

    def take_bet(self,chips):
        while True:

            try:
                chips.bet=int(input("how many chips would you like to bet:"))
            except:
                print("sorry please provide an integer")
            else:
                if chips.bet>chips.total:
                    print("sorry you do not have enough chips!!you have {}".__format__(chips.total))
                else:
                    break
    def hit(self,deck,hand):
        single_card=deck.deal()
        hand.add_card(single_card)
        hand.adjust_for_ace()

    def hit_or_stand(self,deck,hand):
        global playing

        while True:
            x=input('Hit or stand?Enter h or s')

            if x[0].lower()=='h':
                self.hit(deck,hand)
            elif x[0].lower()=='s':
                print("player stands dealers turn")
                playing=False
            else:
                print("sorry i didnt get it please enter h or s only")
                continue
            break
    def show_some(self,player,dealer):
        print("DEALERS HAND:")
        print("one card hidden")
        print(dealer.cards[1])
        print("\n")
        print("PLAYERS HAND:")
        for card in player.cards:
            print(card)

    def show_all(self,player,dealer):
        print("DEALERS HAND:")
        for card in dealer.cards:
            print(card)
        print("PLAYERS HAND")
        for card in player.cards:
            print(card)


    def player_bursts(self,player,dealer,chips):
        print("PLAYER BURST")
        chips.lose_bet()

    def player_wins(self,player,dealer,chips):
        print("PLAYER WINS CONGRATULATIONS")
        chips.win_bet()

    def dealer_burst(self,player,dealer,chips):
        print("DEALER BURST")
        chips.win_bet()

    def dealer_wins(self,player,dealer,chips):
        print("DEALER WINS")
        chips.lose_bet()

    def push(self,player,dealer,chips):
        print("Delaer and player tie!!PUSH")
#Actual game
while True:
    print("WELCOME TO BLACKJACK")

    deck=Deck()
    deck.shuffle()

    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #set player chips
    player_chips=Chips()

    #make the player bet
    player_chips.take_bet(player_chips)

    #show cards but keep 1 dealer card hidden
    player_chips.show_some(player_hand,dealer_hand)

    while playing:

        #prompt for player to hit or stand
        player_chips.hit_or_stand(deck,player_hand)

        #show cards but keep one dealer card hidden
        player_chips.show_some(player_hand,dealer_hand)

        #if players hand exceeds 21 ,run player_bursts() and break out of the loop

        if player_hand.value>21:
            player_chips.player_bursts(player_hand,dealer_hand,player_chips)
            break

        #if player has not busted,play the dealers and until the dealer reaches 17
        if player_hand.value<=21:

            while dealer_hand.value<=17:

                player_chips.hit_or_stand(deck,dealer_hand)
                player_chips.show_all(player_hand,dealer_hand)


        #different winning senarios
        if dealer_hand.value>21:
            player_chips.dealer_burst(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            player_chips.dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value<player_hand.value:
            player_chips.player_wins(player_hand,dealer_hand,player_chips)
        else:
            player_chips.push(player_hand,dealer_hand,player_chips)

    print("\n Player total chips are at:{}".format(player_chips.total))
    #ask player to play again
    new_game=input("would you like to play another hand y/n:")

    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("THANK YOU FOR PLAYING")
        break



















