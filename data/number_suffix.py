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

def get_number_suffix(number):
    return suffixes[number - 1]

def suffixify_number(number):
    if not isinstance(number, int):
        return ""
    suffix = get_number_suffix(number)
    suffixified_number = str(number) + suffix
    return suffixified_number