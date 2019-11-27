LECTURE 2
3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)]
Python Type "help", "copyright", "credits" or "license" for more information.
#last time
a=5
a
5
id(a)
4353797248
id(5)
4353797248
b=a+2
b
7
id(b)
4353797312
a=10
id(a)
4353797408
id(b)
4353797312
#note the statement b=a+2 doesnt say that b is always 2 more than wahtever value that a has,
#it just says that b gets the value that is 2 more than the value of a at the time of evaluation.
#changing a does not change b
#choose descriptive variables names.
age=78
age
78
#rules for variable names 
#names must start with a letter or an underscore(_)
#other characters can incude letterse,digits,and _


#PYHTON I
#IS CASE SENSITVE 
age=11
aGe=12
id(age)
4353797440
id(aGe)
4353797472
#examples of valid variable names
Electron27=1.245
My_age=39
#examples of invalid names:14u,cu@2pm ie no special characters
#conventions in python:use lower case letters,use underscore to seperate two names
#use kartik_sanwgan not kartiksangwan.this convention is called lowercase pothole.

#form of assignment statements is:

#variable_name=an expression that evaluates to a value
x=3+5*3
x
18

#- is assymetric 
#= is assymetric

#not valid:4=y
#valid:y=4
4=y
Traceback (most recent call last):
  Python Shell, prompt 41, line 1
Syntax Error: can't assign to literal: <string>, line 1, pos 0
######################################################################### DONE 
######################################################################### DONE

LECTURE 3

3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)]
Python Type "help", "copyright", "credits" or "license" for more information.
[evaluate distance_to_origin.py]
repeat_word('Marcie ',3)
'Marcie Marcie Marcie '
repeat_word('Marcie',3)
'MarcieMarcieMarcie'
repeat_word('Buffalo',8)
'BuffaloBuffaloBuffaloBuffaloBuffaloBuffaloBuffaloBuffalo'
 repeat_word('Buffalo ',8)
'Buffalo Buffalo Buffalo Buffalo Buffalo Buffalo Buffalo Buffalo '
repeat_count('hello',0)
Traceback (most recent call last):
  Python Shell, prompt 6, line 1
builtins.NameError: name 'repeat_count' is not defined
repeat_word('hello',0)
''
repeat_word('hello',-2)
''
repeat_word('hello',1.2)
Traceback (most recent call last):
  Python Shell, prompt 9, line 1
  File "/Users/kartiksangwan/Desktop/distance_to_origin.py", line 19, in <module>
    return word*repeat_count
builtins.TypeError: can't multiply sequence by non-int of type 'float'
#cant multiply a string by a float undefined

##########################################
####################################################DONE

#type str objects:indexing, whether or not one str appears in another 
#finding 
#finding the length of str, slicing of a str, converting an object to type str.
s='hello'
s
'hello'
print(s)
hello
len(s)
5
r-'good bye'
Traceback (most recent call last):
  Python Shell, prompt 8, line 1
builtins.NameError: name 'r' is not defined
len(r)
Traceback (most recent call last):
  Python Shell, prompt 9, line 1
builtins.NameError: name 'r' is not defined
r='good bye'
len(r)
8
q = 'hello\n'
len(q)
6
#that means escape sequence has one length
s[0]
'h'
s[1]
'e'
s
'hello'
s[-1]
'o'
s[-2]
'l'
s[len(s)]
Traceback (most recent call last):
  Python Shell, prompt 20, line 1
builtins.IndexError: string index out of range
#error because there is no character at index five as indices start at 0
s[1:3]
'el'
s[1:len(s)]
'ello'
s[1:3489284]
'ello'
#it just goes to the end
s[3:1]
''
#as it is opposite way hence empty string
s[:3]
'hel'
s[2:]
'llo'
s[:]
'hello'
#
#slicing method shown above:
#format is : s[first_index_to_include : first_index_to_not_include]
#there is an optional third parameter - the stride length - distance
#between characters in a slice.the default is 1.
n='jacqueline'
n[1:4]
'acq'
n[1:4:1]
'acq'
n[1:4:2]
'aq'
n[::2]
'jculn'
#every other character starting from the begining upto end.
#negative stride goes backwards
n[3:0:-1]
'qca'
#
#in operator
#
word='dictionary'
'tom' in word
False
'nar' in word
True
'inr' in word
False
'inr' in word[::2]
True
'diane' not in word
True
'ict' not in the word
Traceback (most recent call last):
  Python Shell, prompt 53, line 1
Syntax Error: invalid syntax: <string>, line 1, pos 21
'ict' not in word
False
not 'ict' in word
False
#in is precedence first than not as other way around doesnt make sense.
#read as not('ict' in word)
#empty string
''
''
"" ""
''
len("")
0
"" in word
True
#to convert an object to type str
str(42)
'42'
42 in '1942'
Traceback (most recent call last):
  Python Shell, prompt 65, line 1
builtins.TypeError: 'in <string>' requires string as left operand, not int
#as string cant be compared to a int type value
str(42) in '1942
Traceback (most recent call last):
  Python Shell, prompt 67, line 1
Syntax Error: EOL while scanning string literal: <string>, line 1, pos 17
str(42) in '1942'
True
42 in 1942
Traceback (most recent call last):
  Python Shell, prompt 69, line 1
builtins.TypeError: argument of type 'int' is not iterable
#in cant be used to compare int to int ,but only for str to str comparision 
##
#type bool
#include all operators inequalities
4>3
True
7
7

5>=5
True
4*2
8
4*2>10
False
4!=4.0
False
type(3)!=type('3)
Traceback (most recent call last):
  Python Shell, prompt 80, line 1
Syntax Error: EOL while scanning string literal: <string>, line 1, pos 18
type(3)!=type('3')
True
#we can perform logical expressions using and or not
#in python only 0 is false and only 1 is true but not any other number
42 == true
Traceback (most recent call last):
  Python Shell, prompt 84, line 1
builtins.NameError: name 'true' is not defined
true==42
Traceback (most recent call last):
  Python Shell, prompt 85, line 1
builtins.NameError: name 'true' is not defined
true == 42
Traceback (most recent call last):
  Python Shell, prompt 86, line 1
builtins.NameError: name 'true' is not defined
early=true
Traceback (most recent call last):
  Python Shell, prompt 87, line 1
builtins.NameError: name 'true' is not defined
a=1
a
1
early = True
early
True
#T must be capital in True
42 == True
False
early or 3>4 or false 
True
#or is the short-cirrcuting that is as soon as it encounters true in and long or 
#statement then it gives back true
#in the following example fails 
early and 1/0 == 5
Traceback (most recent call last):
  Python Shell, prompt 98, line 1
builtins.ZeroDivisionError: division by zero
False and 1/0 ==5
False
#this didnt result in and error as due to short circuitnig python didnt even evaluate the second part of the and

#if you know that a second expression will fail,you can guard against 
#failure by checking a condition first
n=0
sun_of_values = 100
sum_of_values / n >7 5
Traceback (most recent call last):
  Python Shell, prompt 105, line 1
Syntax Error: invalid syntax: <string>, line 1, pos 22
n != 0 and sum_of _values / n > 75
Traceback (most recent call last):
  Python Shell, prompt 106, line 1
Syntax Error: invalid syntax: <string>, line 1, pos 25
n != 0 and sum_of_values / n > 75
False

