from .Table import Table, MultiRoll

hair_uncommon = Table(
    ("blue", 4),
    ("green", 4),
    ("pink", 4),
    ("violet", 4),
    ("turquoise", 2)
)

hair_color = Table(
    ("black", 25),
    ("brown", 25),
    ("red", 20),
    ("orange", 20),
    ("blonde", 20),
    ("white", 20),
    (hair_uncommon, 10)
)

short_hair = Table(
    ("parted to the left", 5),
    ("parted to the right", 5),
    (MultiRoll("kept back by a {} headband", hair_uncommon), 5),
    ("a tousled bed head", 5),
    ("geled back", 5),
    ("a buzz cut", 1),
)

medium_hair = Table(
    ("done up in a top knot", 5),
    (MultiRoll("braided with {} ribbon (med)", hair_uncommon), 5),
    ("put back in a short pony tail", 5),
    ("loose around the shoulders", 5),
    ("parted to the side, slightly obscuring an eye", 5),
    ("pulled to the side and buzzed on the right", 2),
    ("pulled to the side and buzzed on the left", 2),
)

long_hair = Table(
    ("put up in a large bun", 5),
    (MultiRoll("braided with {} ribbon (long)", hair_uncommon), 5),
    ("put back in a long pony tail", 5),
    ("hanging down to their back", 5),
    ("hanging down to their legs", 2),    
)

hair_length = Table(
    (short_hair, 20),
    (medium_hair, 20),
    (long_hair, 20)
)

hair_texture = Table(
    ("straight", [1,30]),
    ("wavy", [31,60]),
    ("curly", [61,90]),
    ("frizzy", 5)
)

hair = MultiRoll(
    "{} {} hair that's {}",
    hair_texture,
    hair_color,
    hair_length
)

def gen_hair():
    return hair.roll()