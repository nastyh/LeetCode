 def numberToWords(num):  # O(N) and space? Keeping dictionaries? 
        ## RC ##
        ## APPROACH : BRUTE FORCE ##
        ## 1. For a two digit number if there is no ones digit 20 -> twenty + " " (number generally), dont leave the space behind, use if else case with "" (empty).
        # Similarly for 20,000 etc.
        
    one_digit = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }

    two_digit = {
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen'
    }
    
    tens = {
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty',
        5: 'Fifty',
        6: 'Sixty',
        7: 'Seventy',
        8: 'Eighty',
        9: 'Ninety'
    }
    
    def get_three_digit_num(num):
        if( not num ) : return ""
        if( not num// 100 ): return get_two_digit_num(num)
        return one_digit[ num // 100 ] + " Hundred" + ((" " + get_two_digit_num( num % 100 )) if( num % 100 ) else "")
    
    def get_two_digit_num( num ):
        if not num:
            return ''
        elif num < 10:
            return one_digit[ num ]
        elif num < 20:
            return two_digit[ num ]
                # edge case 1
        return tens[ num//10 ] + ((" " + one_digit[ num % 10 ]) if( num % 10 ) else "")
    
    # edge case
    if(num == 0): return "Zero"
    
    billion = num // 1000000000
    million = (num - billion * 1000000000) // 1000000
    thousand = (num - billion * 1000000000 - million * 1000000) // 1000
    last_three = num - billion * 1000000000 - million * 1000000 - thousand * 1000
    
    result = ''
    if billion:        
        result = get_three_digit_num(billion) + ' Billion'
    if million:
        # space only when prev result is not None
        result += ' ' if result else ''    
        result += get_three_digit_num(million) + ' Million'
    if thousand:
        result += ' ' if result else ''
        result += get_three_digit_num(thousand) + ' Thousand'
    if last_three:
        result += ' ' if result else ''
        result += get_three_digit_num(last_three)
    return result

def numberToWords(num):
    def convert(n):
        units_words = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        tens_words = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        teens_words = ['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        
        n, units = divmod(n, 10)            
        n, tens = divmod(n, 10)
        hundreds = n
        
        s = ""
        if hundreds:
            s += units_words[hundreds] + " Hundred"
            
        if tens == 1 and units > 0:
            s += (" " if s else "") + teens_words[units]
        else:
            if tens:
                s += (" " if s else "") + tens_words[tens]
            if units:
                s += (" " if s else "") + units_words[units]
                
        return s
    result = ""
    powers = [(10**9, ' Billion'), (10**6, ' Million'), (10**3, ' Thousand'), (1, '')]        
    for power, word in powers:
        triad = (num // power) % 10**3
        if triad:
            result += (" " if result else "") + convert(triad) + word
    return result or 'Zero'