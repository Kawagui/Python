import math

def letter_to_number(letter):
    """Convert a letter to a number (a=1, b=2, ..., z=26)"""
    return ord(letter.lower()) - ord('a') + 1

def name_to_value(name):
    """Convert a name to a numerical value by summing the values of its letters"""
    return sum(letter_to_number(letter) for letter in name if letter.isalpha())

def complex_combination(value1, value2):
    """Combine the two values using a complex formula"""
    product = value1 * value2
    sum_square = value1**2 + value2**2
    trig_part = math.sin(product) + math.cos(sum_square)
    combined_value = product + sum_square + trig_part
    return combined_value

def normalize_value(value, scale=100):
    """Normalize the value to a range from 0 to scale with multiple decimal places"""
    normalized_value = (value % scale) + (value % 1)
    return round(normalized_value, 4)  # Adjust the number of decimal places as needed

def love_calculator(name1, name2):
    """Calculate the compatibility percentage between two names with decimal places"""
    value1 = name_to_value(name1)
    value2 = name_to_value(name2)
    combined_value = complex_combination(value1, value2)
    compatibility = normalize_value(combined_value)
    return round(compatibility, 2)
