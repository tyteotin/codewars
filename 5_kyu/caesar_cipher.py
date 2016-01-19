"""
Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the 
alphabet by however many spots the cipher was initialized to.

For example:

c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES'
If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
"""

class CaesarCipher(object):
    
    def __init__(self, shift):
        self.s = shift

    def encode(self, str):
        upperCase = str.upper()
        bound = ord('Z') - self.s
        res = ""
        for i in upperCase:
            if(i.isalpha()):
                if(ord(i) > bound):
                    res+=chr(ord('A') + (ord(i)-bound-1))                    
                else:
                    res+=chr(ord(i)+self.s)                
            else:
                res+=i
        return res            
        
    def decode(self, arg):
        bound = ord('A') + self.s
        res = ""
        for i in arg:
            if(i.isalpha()):
                if(ord(i) < bound):
                    res+=chr(ord('Z') - (bound-ord(i)-1))                    
                else:
                    res+=chr(ord(i)-self.s)                
            else:
                res+=i
        return res       
