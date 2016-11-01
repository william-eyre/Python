import random

class Coin:

    # the __init__ method initialises the sideup data attribute with "heads"

    # the Parameter variable names self: must be present in a method/.
    # you are not required to name it self
    # but this is strongly recommended to confrim with standard practice.
    # when a method is called, Python makes the self paramete reference
    # the specific object that the
    # method is supposed to operate on. The __init__ method is commonly
    # know as an intitializer method becuase it initializes the objects
    # data attributes

    def __init__(self):

        # the sideup attribute is not private
        self.toss()
        # the toss ethod generates a random number
        # in the range of 0 through 1. if the number
        # is 0, then sideup is set to 'heads'
        # otherwise, sideup is set to 'tails'

    def toss(self):  # self will automatically reference the object that the method is to operate on.

        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # the get_sideup method returns the value
    # referenced by sideup
    def get_sideup(self):
        return self.__sideup
