suits = 'CDHS'
ranks = '23456789TJQKA'

from abc import ABCMeta, abstractmethod

class Card(metaclass=ABCMeta):
    """Abstact class for playing cards
    """
    def __init__(self, rank_suit):
        if rank_suit[0] not in ranks or rank_suit[1] not in suits:
            raise ValueError(f'{rank_suit}: illegal card')
        self.card = rank_suit
        
    def __repr__(self):
        return self.card
    
    @abstractmethod
    def value(self):
        """Subclasses should implement this method
        """
        raise NotImplementedError("value method not implemented")

    # card comparison operators
    def __gt__(self, other): return self.value() > other.value()
    def __ge__(self, other): return self.value() >= other.value()
    def __lt__(self, other): return self.value() < other.value()
    def __le__(self, other): return self.value() <= other.value()
    def __eq__(self, other): return self.value() == other.value()
    def __ne__(self, other): return self.value() != other.value()


class PKCard(Card):

    def value(self):
        order = dict(zip(ranks, range(2, 2 + len(ranks))))
        for i in order.keys():
            if self.card[0] == i: return order[i]

if __name__ == '__main__':
    c1 = PKCard('QC')
    c2 = PKCard('9D')
    c3 = PKCard('9C')
    print(f'{c1} {c2} {c3}')

    # comparison
    print(c1 > c2 == c3)

    # sorting
    cards = [c1, c2, c3, PKCard('AS'), PKCard('2D')]
    sorted_cards = sorted(cards)
    print(sorted_cards)
    cards.sort()
    print(cards)



import random
class Deck():
    def __init__(self, cls):
        self.deck = [cls(r+s) for r in ranks for s in suits] 

    def shuffle(self):
        return random.shuffle(self.deck)

    def pop(self):
        return self.deck.pop()

    def __str__(self):
        return f'{self.deck}'

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, index):
        return self.deck[index]

if __name__ == '__main__':
    deck = Deck(PKCard)  # deck of poker cards
    deck.shuffle()
    c = deck[0]
    print('A deck of', c.__class__.__name__)
    print(deck)
    #testing __getitem__ method
    print(deck[-5:])

    while len(deck) >= 10:
        my_hand = []
        your_hand = []
        for i in range(5):
            for hand in (my_hand, your_hand):
                card = deck.pop()
                hand.append(card)
        my_hand.sort(reverse=True)
        your_hand.sort(reverse=True)
        print(my_hand, '>', your_hand, '?', my_hand > your_hand)


class Hands:

    def __init__(self, cards):
        if len(cards) != 5:
            raise ValueError('not 5 cards')
        self.cards = sorted(cards, reverse=True) #내림차순으로 정리

    def is_flush(self, cards):
        if(self.cards[0][1] == self.cards[1][1] and self.cards[1][1] == self.cards[2][1] and self.cards[2][1] == self.cards[3][1] and self.cards[3][1] == self.cards[4][1]):
            return True
        else: False
     
    def is_straight(self, cards):
        if((self.cards[0][0] - 1) == self.cards[1][0] and (self.cards[1][0] - 1) == self.cards[2][0] == (self.cards[2][0] - 1) == self.cards[3][0] == (self.cards[3][0] - 1) == self.cards[4][0]):
            return True
        else: False
        
    def classify_by_rank(self, cards):
        tmp = dict()

        pass

    def find_a_kind(self, cards):
        count = 0
        for i in range(1, 5, -1):
            if self.cards[0][i] == self.cards[0][i-1]:
                count += 1
        if self.cards[0][1] == self.cards[0][0]:
            count += 1
        
        if count == 3:
            return 'Full House'
        elif count == 2:
            return 'two Pair'
        elif count == 1:
            return 'one Pair'

    def tell_hand_ranking(self, cards):
    
        pass
    
if __name__ == '__main__':
    import sys
    def test(did_pass):
        """  Print the result of a test.  """
        linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
        if did_pass:
            msg = "Test at line {0} ok.".format(linenum)
        else:
            msg = ("Test at line {0} FAILED.".format(linenum))
        print(msg)

#     # your test cases here
    #test1
    test(Hands([PKCard('QC'), PKCard('9C'), PKCard('QS'), PKCard('2D'), PKCard('QC')])==)
    test(Hands([PKCard('AS'), PKCard('AC'), PKCard('AD'), PKCard('2D'), PKCard('QC')])==)



#     pass

