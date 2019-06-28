# review
print("Hello World!")
num = 100
if num > 10:
    print("something")
#-------------------------------------------------------------------------
# assignment
text = """Python is an interpreted, high-level, 
general-purpose programming language. 
Created by Guido van Rossum and first 
released in 1991, Python has a design 
philosophy that emphasizes code readability,
 notably using significant whitespace. 
 It provides constructs that enable clear 
 programming on both small 
and large scales. Wikipedia"""

vowels = []
consonants = []

words = text.split()
print(words)
# words
# occurances of the or The
#
for word in words:
    if word[0] in "AEIOUaeiou":
        vowels.append(word)
    else:
        consonants.append(word)


print(vowels)
print(consonants)
#------------------------------------------------------------------------------------
# for_and_while
lst = [1, 2, 3, 4, 5, 6, 7, 7, 3, 88, 3]

# generators
for i in range(10):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

#------------------------------
#question_2
text = """Nothing can ever happen twice
in a consequence the sorry fact is
that we arrive here improvised 
and leave w/o the chance to practice   
"""

words = text.split()
length_of_words = []

for w in words:
    temp = len(w)
    length_of_words.append(temp)

print(length_of_words)
print(words)


new_list = zip(words, length_of_words)
print(list(new_list))
#------------------------------------------------------
#end