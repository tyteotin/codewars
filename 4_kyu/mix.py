"""
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings will be in decreasing order of their length and when they have the same length sorted alphabetically; the different groups will be separated by '/'.

Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
"""


def mix(s1, s2):
    if(len(s1) > len(s2)):
        pad = " " * (len(s1)-len(s2))
        s2+= pad
    else:
        pad = " " * (len(s2)-len(s1))
        s1+= pad

    alphabet_s1 = [0] * 26
    alphabet_s2 = [0] * 26
    
    for i in range(0, len(s1), 1):
        if(ord(s1[i]) >= 97 and ord(s1[i]) <= 122):
            alphabet_s1[ord(s1[i])-97] += 1
        if(ord(s2[i]) >= 97 and ord(s2[i]) <= 122):
            alphabet_s2[ord(s2[i])-97] += 1
    
    compare_result = []
    max_freq = max(alphabet_s1) if max(alphabet_s1) > max(alphabet_s2) else max(alphabet_s2)
    for i in range(0, len(alphabet_s1), 1):
        if(alphabet_s1[i] > 1 or alphabet_s2[i] > 1):
            if(alphabet_s1[i] > alphabet_s2[i]):
                compare_result.append([alphabet_s1[i], '1', chr(i+97)])
            elif(alphabet_s1[i] < alphabet_s2[i]):
                compare_result.append([alphabet_s2[i], '2', chr(i+97)])
            else:
                compare_result.append([alphabet_s1[i], '=', chr(i+97)])

    res = ""
    while(max_freq > 1):
        str_1 = ""
        str_2 = ""
        str_eq = ""
        for i in compare_result:
            if(i[0] == max_freq):
                if(i[1] == '1'):
                    str_1 += i[1] + ":" + i[2] * i[0] + "/"
                elif(i[1] == '2'):
                    str_2 += i[1] + ":" + i[2] * i[0] + "/"
                else:
                    str_eq += i[1] + ":" + i[2] * i[0] + "/"
        res += str_1 + str_2 + str_eq
        max_freq -= 1
    res = res[:-1]

    return res
