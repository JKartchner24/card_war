from random import shuffle


suites = 'H D S C'.split()
card_ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

print("Welcome to War!")

class deck:
    def __init__ (self):
        self.theDeck = [(s,r) for s in suites for r in card_ranks ]
        print("The deck has been created")

    def split_in_half(self):
        return (self.theDeck[:26],self.theDeck[26:])
        
    def shuffle(self):
        shuffle(self.theDeck)
        print("Shuffling!")

class Hand:
    def __init__(self,cards):
        self.cards = cards

    def add_card(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, hand, name):
        self.hand = hand
        self.name = name

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has played: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) <3:
          return war_cards
        else:
          for x in range(3):
            war_cards.append(self.hand.cards.pop())
          return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) != 0

d = deck()
d.shuffle()
cut1,cut2 = d.split_in_half()

comp = Player(Hand(cut1),"Computer Player")
name = input("Enter Your Name: ")
user = Player(Hand(cut2),name)

while user.still_has_cards() and comp.still_has_cards():
    print("Next Round!")
    print("Here is the Score!")
    print(user.name+" has "+str(len(user.hand.cards))+" cards left")
    print(comp.name+" has "+str(len(comp.hand.cards))+" cards left")
    print("Now play a card!")
    print("\n")

    cards_on_table = []
    computer_card = comp.play_card()
    player_card = user.play_card()

    cards_on_table.append(computer_card)
    cards_on_table.append(player_card)

    if computer_card[1] == player_card[1]:
        print(computer_card[1])
        print("WAR HAS BEGUN!")
        cards_on_table.extend(user.remove_war_cards())
        cards_on_table.extend(comp.remove_war_cards())

        try:
            computer_card = comp.play_card()
            player_card = user.play_card()

            cards_on_table.append(computer_card)
            cards_on_table.append(player_card)

            if card_ranks.index(computer_card[1]) < card_ranks.index(player_card[1]):
                user.hand.add_card(cards_on_table)
            elif card_ranks.index(computer_card[1]) == card_ranks.index(player_card[1]):
                print("NOW WE HAVE DOUBLE WAR!")
                cards_on_table.extend(user.remove_war_cards())
                cards_on_table.extend(comp.remove_war_cards())
                try:
                    computer_card = comp.play_card()
                    player_card = user.play_card()

                    cards_on_table.append(computer_card)
                    cards_on_table.append(player_card)
                    if card_ranks.index(computer_card[1]) < card_ranks.index(player_card[1]):
                        user.hand.add_card(cards_on_table)

                    else:
                        comp.hand.add_card(cards_on_table)

                except:
                    print("Not Enough Cards for Double War")
                    break
            else:
                comp.hand.add_card(cards_on_table)

        except:
            print("Not enough cards left in deck for War, Game over")
            break;

    else:
        if card_ranks.index(computer_card[1]) < card_ranks.index(player_card[1]):
            user.hand.add_card(cards_on_table)
        else:
            comp.hand.add_card(cards_on_table)
    if len(user.hand.cards)>len(comp.hand.cards):
        print(user.name+" has Won!")
    else:
        print("Computer Player has Won!")
else:
    if len(user.hand.cards)==0:
        print("Game Over! Computer Player has Won!")
    else:
        print("Game Over! "+user.name+" has Won!")