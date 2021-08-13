############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

        # Fill in the rest

    def add_pairings(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code(new_code)

        # Fill in the rest




def make_melon_types():
    """Returns a list of current melon types."""
    all_melon_types = ["musk", "cas", "cren", "yw"]
    
    musk = MelonType(
    "musk",
    "Muskmelon",
    1998,
    "green",
    True,
    True
    )

    cas = MelonType(
    "cas",
    "Casaba",
    2003,
    "orange",
    False,
    False
    )
    
    cren = MelonType(
    "cren",
    "Crenshaw",
    1996,
    "green",
    False,
    False
    )

    yw = MelonType(
    "yw",
    "Yellow Watermelon",
    2013,
    "yellow",
    False,
    True
    )
    

    musk.add_pairings("mint")
    cas.add_pairings(["strawberry","mint"])
    cren.add_pairings("proscuitto")
    yw.add_pairings("ice cream")


    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    # self.pairing("{} pairs with".format(melon))
    melon_types.pairing("{}.name pairs with".format(melon))

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



