from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # CREATE A CARD
                created_card = Card(suit, rank)
                # APPEND THE CREATED CARD TO THE DECK
                self.all_cards.append(created_card)
        # SHUFFLE THE CREATED DECK
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one_card(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        #  ADD LIST OF MULTIPLE CARDS. NOTE USE OF EXTEND()
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        # ADD SINGLE CARD i.e. APPEND
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {self.all_cards}'


player_one = Player('One')
player_two = Player("Two")
new_deck = Deck()
# SPLIT THE DECK BETWEEN TWO PLAYERS
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0
while game_on:
    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.all_cards) == 0:
        print(f'Player One has no cards left. Player Two WINS!!!')
        game_on = False
        break
    elif len(player_two.all_cards) == 0:
        print(f'Player Two has no cards left. Player One WINS!!!')
        game_on = False
        break

    # START A NEW ROUND
    # PLAYER ONE CURRENT DEALING CARDS ON TABLE
    player_one_cards = []
    player_one_cards.append(player_one.remove_one_card())
# PLAYER TWO CURRENT DEALING CARDS ON TABLE
    player_two_cards = []
    player_two_cards.append(player_two.remove_one_card())

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print('WAR!')
            if len(player_one.all_cards) < 5:
                print(f'Player One does not have enough cards for war. Player Two WINS!')
                game_on= False
                break
            elif len(player_two.all_cards) < 5:
                print(f'Player Two does not have enough for war. Player One WINS!')
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one_card())
                    player_two_cards.append(player_two.remove_one_card())