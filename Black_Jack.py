from random import shuffle


def deck():
    A = 11
    K = 10
    Q = 10
    J = 10
    cards = [
        2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J,
        Q, K, A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A, 2, 3, 4, 5, 6, 7, 8,
        9, 10, J, Q, K, A
    ]
    return cards


def black_jack():
    cards = deck()
    for _ in range(11):
        shuffle(cards)
    player_hand = cards[:2]
    dealer_hand = cards[50:]
    print(player_hand)
    print(dealer_hand)


def hit_me():
    print('Hit me or Stay? ')
    if input() == 'Hit me':
        deal_cards()
    if input() == 'Stay':
        return player_hand()


def deal_cards():
    if hit_me() == 'Hit me':
        player_hand.append(cards[:1])
    if hit_me() == 'Stay':
        return player_hand


def player_hand():
    player_hand = deck()[:2]
    while player_hand < 21:
        deal_cards()


def dealer_hand():
    dealer_hand = cards[50:]
    while dealer_hand < 17:
        deal_cards()


def black_jack_greetings():
    input('Would you like to join us for a game of Blackjack? ')
    if input() == 'Yes':
        print(tutorial())
    if input() == 'No':
        print('Then I hope you have a glorious day sir. ')


def who_wins():
    if dealer_hand > 17:
        print('YOU BUST DEALER! PLAYER YOU WIN! ')
    if player_hand > 21:
        print('YOU BUST PLAYER! DEALER YOU WIN! ')


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
    black_jack()
    hit_me()
    cards = deck()


if __name__ == '__main__':
    main()
