import re
def validIPAddress(IP):       

    reg_v6 = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    r_v4 = r'(([2][0-5][0-5])|([1][0-9][0-9])|([1-9][0-9])|([0-9]))'
    reg_v4 = re.compile(r'^(' + r_v4 + r'\.){3}' + r_v4 + r'$')
    if re.search(reg_v6, IP): return 'IPv6'
    if re.search(reg_v4, IP): return 'IPv4'
    return 'Neither'

def validIPAddress_alt(IP):
    colons = IP.count(':')
    dots = IP.count('.')

    if colons and dots:
        return 'Neither'

    if dots == 3:
        nums = IP.split('.')
        for num in nums:
            if not (num.isdigit() and num == str(int(num)) and 0<=int(num)<=255):
                break
        else:
            return 'IPv4'

    elif colons == 7:
        nums = IP.split(':')
        for num in nums:
            if not (num.isalnum() and len(num)<5):
                return 'Neither'
            else:
                for letter in num:
                    if letter.isalpha():
                        if not letter.lower() < 'g':
                            return 'Neither'
        return 'IPv6'
    return 'Neither'