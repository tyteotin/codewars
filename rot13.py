"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using "encode" in Python is considered cheating.
"""
import string
def rot13(message):
    print message
    msg = ""
    for i in message:
        if((i >= 'a' and i <= 'm') or (i >= 'A' and i <= 'M')):
            msg+= chr(ord(i) + 13)
        elif((i > 'm' and i <= 'z') or (i > 'M' and i <= 'Z')):
            msg+= chr(ord(i) - 13)
        else:
            msg+= i
    return msg