import random

def get_voice():
    voice_dict = {}

    #Generate weight
    weights = ["light", "strong"]
    voice_dict["weight"] = random.choice(weights)

    #Generate spacial
    spacial = ["direct", "indirect"]
    voice_dict["spacial"] = random.choice(spacial)

    #Generate timing
    timings = ["sudden", "sustained"]
    voice_dict["timing"] = random.choice(timings)

    return voice_dict
