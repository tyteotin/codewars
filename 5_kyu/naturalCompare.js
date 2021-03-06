/*
Quite some years ago I worked doing a lot of automated document sorting. As part of the we needed to do "natural compare" 
on document titles (and other relevant fields). Natural compare intend to let "file 2" be less than "file 10", while 
normal lexical compare claim the opposite. Solving this issue by normalizing numbers to eg 3 digits, was not an option.

Your task is to make a compare function that given "file 2" and "file 10" will return -1 (as C strcmp). For equal strings 
the return value should be 0 and 1 if the first argument is "greater than" the second.

naturalCompare("file 2", "file 10")   return  -1
naturalCompare("file 2", "file 2")    return 0
naturalCompare("file 10", "file 2")   return 1
If two strings are "natural equal" the shortest must be sorted before the longer version (return 1 since first argument
 is longest):

naturalCompare("file 01", "file 1") === 1
Do not concern yourself with negative (signed) numbers, such as "file -1". This will not form a part of the test - the 
'-' should be considered a non-number character.
*/

function naturalCompare(a,b) {
  // Return -1 if a < b
  // Return 0 if a = b
  // Return 1 if a > b
  var pattern = /\d+/g;
  var f_a = a.match(pattern);
  var f_b = b.match(pattern);
  if(f_a == null || f_b == null) {
    return a.localeCompare(b);
  }
  var rem_pat = /[A-z]+/g;
  var rem_a = a.replace(f_a[0], '');
  var rem_b = b.replace(f_b[0], '');

  if(parseInt(f_a) == parseInt(f_b)) { 
    if(rem_a > rem_b) {
      return 1;
    }
    else if(rem_a < rem_b) {
      return -1;
    }
    else {
      if(f_a[0].length > f_b[0].length) {        
        return 1;
      }
      else if (f_a[0].length < f_b[0].length) {
        return -1;
      }
      else
        return 0;
    }
  }
  else if(parseInt(f_a) > parseInt(f_b)) {
    return 1;
  }
  else 
    return -1;  
}
