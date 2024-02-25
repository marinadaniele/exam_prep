text = "abcdefg"
print(dir(text))
help(text.isidentifier)
print(text.isidentifier()) # is abcdefg a valid identifier?
print("1234".isidentifier()) # is 1234 a valid identifier?
print("ananananananananananan".count("ana"))
print("ananananananananananan".replace("ana", "banana"))
print("ananananananananananan".find("ana", 1))
print("bbbbbabbbbbbabbbbbbbbabbbabb".split("a"))
print("this is a sentence and I want the words".split(" "))
sentence = "Hello, kind-sir; how many! I be of service today?"
punctuation = ".,;!?-"
# sanitize the sentence
for p in punctuation:
    sentence = sentence.replace(p, " ") # replace the punctuation with nothing
print(sentence)
sentence = sentence.replace("  ", " ") # replace double spaces with single spaces
# split the sentence into words
words = sentence.split(" ")
print(words)

text = "cat"
print(text.upper())
print(text)

name = "John"
second_name = "Bob"
print(f"Hi, {name} how are you? My name is {second_name}")
name = "Jane"
second_name = "Mary"
print(f"Hi, {name} how are you? My name is {second_name}")

#################################################################################################
## string slice

base = "abcdefghijklmnopqrstuvwxyz"

print("here are some slices")
print(base[0:3])
print(base[0:5])
print(base[10:]) # all the way till the end
print(base[:10]) # all the way from the beginning
print(base[:]) # the whole string
print(base[::2]) # every other letter
print(base[5:15:3]) # every third letter from the 5th to the 15th
print(base[::-1]) # the whole string backwards

#################################################################################################
## string backwards
# iterate over a string backwards using while
text = "abcdefghijkl"
i = 0
while i < len(text):
    print(text[len(text)-1-i])
    i += 1