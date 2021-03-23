"""
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
Given a string and a rotation factor, return an encrypted string.
Signature
string rotationalCipher(string input, int rotationFactor)
Input
1 <= |input| <= 1,000,000
0 <= rotationFactor <= 1,000,000
Output
Return the result of rotating input a number of times equal to rotationFactor.
Example 1
input = Zebra-493?
rotationFactor = 3
output = Cheud-726?

Example 2
input = abcdefghijklmNOPQRSTUVWXYZ0123456789
rotationFactor = 39
output = nopqrstuvwxyzABCDEFGHIJKLM9012345678
"""
import string
def rotational(input, rotationFactor):  # O(n) to traverse the string, O(1) to store the alphabet and the digits
    """
    Build a dictionary: d = {a: 0, b: 1, z: 25, A: 0, B: 1, Z: 25}
    With digits, it's easy. Add rotation_factor. If the number is > 9, (example: 9 + 3), need to % 10 it.
    So 12 becomes 2, i.e. the third digits in the sequence '0123456789', i.e. 2
    If it's a character, use the dictionary to get a count.
    If a count > 25, then we need to % 26.
    But we need to take care of capital letters and take a new letter not from the dictionary but from 
    either letters_small or letters_capital
    In all other cases, just add to res whatever the symbol is 
    """
    res = ''
    d = {}
    letters_small = string.ascii_lowercase  # abc...z
    letters_capital = string.ascii_uppercase  # ABC..Z
    for k, v in enumerate(letters_small):
        d[v] = k
    for k, v in enumerate(letters_capital):
        d[v] = k
    digits = string.digits
    for ix in range(len(input)):
        if input[ix].isdigit():
            new_ix = (int(input[ix]) + rotationFactor)
            if new_ix >= 10:  # number is too large
                new_ix = new_ix % 10
            res += digits[new_ix]
        elif input[ix].isalpha():
            new_ix = d[input[ix]] + rotationFactor
            if new_ix >= 26:  # character is too large
                new_ix = new_ix % 26
            if input[ix].isupper():  # depending on whether it's a capital letter or no, we substitute it using a proper source 
                res += letters_capital[new_ix]
            else:
                res += letters_small[new_ix]
        else:
            res += input[ix]
    return res 


if __name__ == '__main__':
    print(rotational('Zebra-493?', 3))
    print(rotational('abcdefghijklmNOPQRSTUVWXYZ0123456789', 39))