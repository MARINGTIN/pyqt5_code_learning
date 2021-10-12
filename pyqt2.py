""" Nothing """

import re
pattern_n = re.compile('(?<=usr:).*?(?=\|)')
pattern_p = re.compile('(?<=pw:).*?(?=\|)')
pattern_a = re.compile('(?<=age:).')
str_t = "sfaoifisj|pw:dsfhjiofhh|ds"

str_n = re.findall(pattern_p, str_t, flags=0)
print(str_n, type(str_n[0]))
str_n = re.findall(pattern_n, str_t, flags=0)
print(str_n, type(str_n[0]))
# print(str_t)
# print(re.findall('(?<=pw:).*?(?=\|)', str_t, flags=0))

'''
a = 'ls'
b = 1
if b == 1:
    a = 'ms'
print(a, type(a))
'''
