# From:
# Ramalho, Luciano. Fluent Python: Clear, Concise, and Effective Programming (p. 5). O'Reilly Media. Kindle Edition. 

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')

    suits = 'spades diamonds clubs hearts'. split()

    def __init__( self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

# list comp examples:
#nums = [1, 2, 3, 4, 5]
#m = [n for n in nums]
#m = [n*n for n in nums]
#m = [n for n in nums if n%2 == 0]
#m = [(letter, num) for letter in 'abcd' for num in range(4)]

# zip example:
#a = ['a', 'b', 'c']
#b = [1, 2, 3]
#x = zip(a,b)

# list dict examples:
#names = ['Bruce', 'Clark', 'Peter']
#heros = ['Batman', 'Superman', 'Spiderman']
#m = {name: hero for name, hero in zip (names, heros) if name != 'Peter'}

# Set comp examples:
#m = {n for n in nums} 

# Generator expression:
# use yield instead of return
#m = (x*x for x in [1, 2, 3, 4, 5])

# Returns only next item in list
# Better performance for huge lists

# Fibonacci
#a, b = 0, 1
#for i in range(10):
#	print a
#	a, b = b, a + b

# List and the enumerate function
#fruits = ['Banana', 'Apple', 'Lime']
#list(enumerate(fruits))
#[(0, 'Banana'), (1, 'Apple'), (2, 'Lime')]

# floor division
#17 // 3
#5

# Cubed
#2 ** 3
#8

