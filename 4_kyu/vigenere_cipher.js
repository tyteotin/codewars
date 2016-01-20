/*
The Vigenère cipher is a classic cipher originally developed by Italian cryptographer Giovan Battista Bellaso and published in 1553.
It is named after a later French cryptographer Blaise de Vigenère, who had developed a stronger autokey cipher (a cipher that 
incorporates the message of the text into the key).

The cipher is easy to understand and implement, but survived three centuries of attempts to break it, earning it the nickname "le 
chiffre indéchiffrable" or "the indecipherable cipher."

From Wikipedia:

The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters 
of a keyword. It is a simple form of polyalphabetic substitution.
(...)

In a Caesar cipher, each letter of the alphabet is shifted along some number of places; for example, in a Caesar cipher of shift 3,
A would become D, B would become E, Y would become B and so on. The Vigenère cipher consists of several Caesar ciphers in sequence
with different shift values.
Assume the key is repeated for the length of the text, character by character. Note that some implementations repeat the key over
characters only if they are part of the alphabet, and that is not the case here.

The shift is derived by applying a Caesar shift to a character with the corresponding index of the key in the alphabet.

Visual representation (suggested by OverZealous)

message: my secret code i want to secure
key:     passwordpasswordpasswordpasswor
Write a class that, when given a key and an alphabet, can be used to encode and decode from the cipher.

E.g.

var alphabet = 'abcdefghijklmnopqrstuvwxyz';
var key = 'password';

// creates a cipher helper with each letter substituted
// by the corresponding character in the key
var c = new VigenèreCipher(key, alphabet);

c.encode('codewars'); // returns 'rovwsoiv'
c.decode('laxxhsj'); // returns 'waffles'
Any character not in the alphabet must be left alone.

E.g. (following from above)

c.encode('CODEWARS'); // returns 'CODEWARS'
*/
function VigenèreCipher(key, abc) {
  var key = key;
  var abc = abc;
  var key_length = key.length;
  var abc_length = abc.length;
  
  this.encode = function (str) {
    var key_index = 0;
    var shift = 0;
    var res = "";

    for(i = 0; i < str.length; i++) {
      if(abc.indexOf(str[i]) != -1) {
        shift = abc.indexOf(str[i]) + abc.indexOf(key[key_index]);
        if(shift >= abc_length) {
          res += abc[0 + (shift - abc_length)];
        }
        else {
          res += abc[shift];
        }
        
      }
      else {
        res += str[i];
      }
      key_index += 1;
      if(key_index >= key_length) {
        key_index = 0;
      }
    }  
    return res;
  };
  
  
  this.decode = function (str) {
    var append_count = str.length/key_length;
    var decode_key = key;
    if(str.length%key_length != 0) {
      append_count += 1;
    }
    for(var i = 0; i < append_count; i++){
      decode_key += key;
    }
    
    decode_key = decode_key.slice(0, str.length);
    var res = "";
    var shift = 0;
    for(var i = 0; i < str.length; i++) {
      if(abc.indexOf(str[i]) != -1) {
        shift = abc.indexOf(str[i]) - abc.indexOf(decode_key[i]);
        if(shift < 0) {
          shift = abc_length + shift;
          res +=  abc[shift];
        }
        else {
          res += abc[shift];
        }
      }
      else {
        res += str[i];
      }
    }
    return res;
  };
}
