# -*- code: utf-8 -*-

# define string variables with different styles
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# print x and y variables
print (x)
print (y)

# print strings using x and y variables
print ("I said: %r." %x)
print ("I also said: '%s'." % y)

# Boolean variable
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# print joke.. and hilarious variables
print (joke_evaluation % hilarious)

# define two string varibles
w = "This is the left side of..."
e = "a string with a right side."

# print variables "w" and "e"
# + sign concatenates two string variables
print (w + e)

# print some strings
print ("Mary had a little lamb.")
print ("Its fleece was white as %s." % 'snow')
print ("And everywhere that Mary went.")
# print 10 '*' signs to place as seperator
print ("." * 10) # what'd that do?

# define some more variables
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that coma at the end. try removing it to see what happens
print (end1 + end2 + end3 + end4 + end5 + end6)
print (end7 + end8 + end9 + end10 + end11 + end12)

formatter = "%r %r %r %r"

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    ))

# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print ("Here are the days: ", days)
print ("Here are the months: ", months)

print ("""
       There's something going on here.
       With the three double-quotes.
       We'll be able type as much as we like.
       Even 4 lines if we want, or 5, or 6.
       """)
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

while True:
    for i in ["/","-","|","\\","|"]:
        print ("%s\r" % i,)

