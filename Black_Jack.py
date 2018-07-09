from random import shuffle


def deck():
    'Ace'
    K = 10
    Q = 10
    J = 10
    cards = [
        2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, 'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10,
        J, Q, K, 'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, 'Ace', 2, 3, 4, 5,
        6, 7, 8, 9, 10, J, Q, K, 'Ace'
    ]
    return cards


def black_jack():
    cards = deck()
    for _ in range(11):
        shuffle(cards)
    player1_hand = cards[:2]
    dealer_hand = cards[50:]
    print(player1_hand)
    print(dealer_hand[0], '?')
    player1_turn(player1_hand, cards)
    dealers_turn(dealer_hand, cards)
    who_wins(player1_hand, dealer_hand)


def player1_turn(player1_hand, cards):
    while True:
        print("Player 1's turn")
        deal = input('Hit me or Stay? ').capitalize().strip()
        if deal == 'Hit me':
            player1_hand.append(cards.pop())
            total = hand_value(player1_hand)
            print(player1_hand)
            if total > 21:
                print('Bust')
                break
            elif total == 21:
                print('BLACKJACK!')
                break
            continue
            print("Player's Hand", player1_hand)
        elif deal == 'Stay':
            break
        else:
            print('Hit me or Stay? ')
        return player1_hand


def betting():
    while True:
        bet = input('How many caps are you exchanging for chips? ')
        if bet.isdigit()


def dealers_turn(dealer_hand, cards):
    while True:
        print("Dealer's turn")
        if hand_value(dealer_hand) < 17:
            dealer_hand.append(cards.pop())
            print("Dealer's hand:", dealer_hand[0], '?', dealer_hand[2:],
                  hand_value(dealer_hand))
        else:
            break


def hand_value(hand):
    hand_total = 0
    aces = 0
    for card in hand:
        if card == 'Ace':
            aces += 1
        else:
            hand_total = hand_total + card
    if aces == 0:
        return hand_total
    else:
        gap = 11 + (aces - 1)
        if hand_total + gap <= 21:
            return hand_total + gap
        else:
            return hand_total + aces


def black_jack_greetings():
    while True:
        response = input('Would you like to join us for a game of Blackjack? ')
        if response == 'Yes':
            print('Then welcome to the Sierra Madre Casino. ')
            return response
        if response == 'No':
            print('Then I hope you have a glorious day sir. ')
            exit()
        else:
            print('Yes or No ')


def who_wins(player1_hand, dealer_hand):
    player, dealer = hand_value(player1_hand), hand_value(dealer_hand)
    print('Player{}, total {} '.format(player1_hand, player))
    print('Dealer{}, total {} '.format(dealer_hand, dealer))
    if player > 21:
        print('Bust')
        print('Dealer Wins!')
    elif player == 21 and dealer != 21:
        print('BLACKJACK!!')
    elif dealer > 17:
        print('Bust')
        print('You Win!')
    elif dealer == player:
        print('Push')
    elif player > dealer:
        print('You Win!')
    else:
        print('Dealer Wins!')


def tutorial():
    print('Then would you like a tutorial? ')
    if input() == 'Yes':
        print(
            'Blackjack is a game of probability.  In order to win you must be the first to score a Blackjack without busting.  If your cards add up to be higher than twenty-one you will bust. '
        )
    if input() == 'No':
        print('Is your luck at 10 then')
    print("You know what nevermind shall we just get started already? ")


def main():
    while True:
        choice = black_jack_greetings()
        if choice == 'Yes':
            black_jack()


if __name__ == '__main__':
    main()
