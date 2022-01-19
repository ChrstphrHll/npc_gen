import random, json

months = {
    "Avanent": 34,
    "Corelent": 33,
    "Melorent": 32,
    "Moradent": 29,
    "Iounent": 29,
    "Pelent": 32,
    "Korent": 33,
    "Ravenent": 28
}

suffixes = [
    "st",
    "nd",
    "rd",
    "th",
    "th",
    "th",
    "th",
    "th",
    "th",
    "th",
    "th",
    "th",
    "th",
    "th",
    "th",
    "th",
    "th",
    "th",
    "th",
    "th",
    "st",
    "nd",
    "rd",
    "th",
    "th",
    "th",
    "th",
    "th",
    "th",
    "th",
    "st",
    "nd",
    "rd",
    "th",
    "th",
    "th",
    "th",
    "th",
]

def get_bday():
    month = random.choice(list(months.keys()))
    month_numeric = list(months.keys()).index(month)
    day = random.randint(1, months[month])
    suffix = suffixes[day - 1]

    readable_template = f"{day}{suffix} of {month}"

    return {
        "numeric": f"{month_numeric}/{day}",
        "written": readable_template
    }