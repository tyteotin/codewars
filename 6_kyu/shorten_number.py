"""
Ok, here is a new one that they asked me to do with an interview/production setting in mind.

You might know and possibly even Angular.js; among other things, it lets you create your own filters that work as functions you put in your pages to do something specific to her kind of data, like shortening it to display it with a more concise notation.

In this case, I will ask you to create a function which return another function (or process, in Ruby) that shortens numbers which are too long, given an initial arrays of values to replace the Xth power of a given base; if the input of the returned function is not a numerical string, it should return the input itself as a string.

An example which could be worth more than a thousand words:

filter1 = shorten_number(['','k','m'],1000)
filter1('234324') == '234k'
filter1('98234324') == '98m'
filter1([1,2,3]) == '[1,2,3]'
filter2 = shorten_number(['B','KB','MB','GB'],1024)
filter2('32') == '32B'
filter2('2100') == '2KB';
filter2('pippi') == 'pippi'
If you like to test yourself with actual work/interview related kata, please also consider this one about building a breadcrumb generator
"""

import math
def shorten_number(suffixes, base):
    def lmd(x):
        if(isinstance(x, basestring) == False):
            return str(x)
        elif(x.isdigit() == False):
            return x
        else:
            x = int(x)
            count = 0
            div_res = x/base            
            while(div_res >= 1):
                div_res /= base
                if(count >= len(suffixes) - 1):
                    break
                count += 1            
            remnant = int(x/math.pow(base, count))
            return str(remnant) + suffixes[count]                   
    return lmd
