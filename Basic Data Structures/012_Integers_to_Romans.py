def intToRoman(num):  # O(1) both
    values = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    res = ''
    while num:   
        for i in values.keys():
            
            div = num // values[i]
            if div > 0:
                for j in range(div):
                    res += i  
                mod = num % values[i]
                num = mod
    return res


def intToRoman_alt(num):
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return thousands[num // 1000] + hundreds[num % 1000 // 100] + tens[num % 100 // 10] + ones[num % 10]


def intToRoman_another(num):
    digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    roman_digits = []
    # Loop through each symbol.
    for value, symbol in digits:
        # We don't want to continue looping if we're done.
        if num == 0: break
        count, num = divmod(num, value)
        # Append "count" copies of "symbol" to roman_digits.
        roman_digits.append(symbol * count)
    return "".join(roman_digits)


def intToRoman_one_more(num):
    """
    The dictionary is sorted, actually. When we do num // base and base is larger than num, it returns 0
    So we get 0 times roman_symbol and nothing is being added to the resulting string 
    But at some point, we get to something like (67 // 50) = 1. And we get 1 * mapping_table[50] = L
    """
    mapping_table = {
        1000 : "M",
        900  : "CM",
        500  : "D",
        400  : "CD",
        100  : "C",
        90   : "XC",
        50   : "L",
        40   : "XL",
        10   : "X",
        9    : "IX",
        5    : "V",
        4    : "IV",
        1    : "I"
        }
        roman_string = ''
		# represent input num in roman number system
        for base, roman_symbol in mapping_table.items():
			# update roman string with corresponding roman symbol
            roman_string += (num // base) * roman_symbol
			# update num as remainder
            num = num % base
        return roman_string
    

if __name__ == '__main__':
    print(intToRoman(4))
    print(intToRoman_alt(11))
    print(intToRoman_alt(1988))