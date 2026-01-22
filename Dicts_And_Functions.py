"""
This allows me to practice Dictionaries and Functions.

Here, for example, I made a dictionary for "yellable" words and applied to said words a boolean value.(True if Yellable, False if not)

Then I made the Function yell() to print a given text in uppercase and add an exclamation point at the end.

Finally, I yelled only the yellable words, And if the word was not yellable, I would get printed unaffected by yell().

This will print out:
    HELLO!
    Morning
    FRICK!
    This ain't even a word
    DAMN!!

But "DAMN" already has an exclamation point, so I added the Function has_exclamation to check if the word already has an exclamation or not and then changed yell() to make it "filter" the words.


"""

yellable_words = {
    "Hello" : True,
    "Morning" : False,
    "Frick" : True,
    "This ain't even a word" : False,
    "DAMN!" : True
}

def has_exclamation(text):
    if "!" in text:
        return True
    else:
        return False

def yell(text):
    if has_exclamation(text):
        print(text.upper())
    else:
        print(text.upper() + "!")

for word in yellable_words:
    if yellable_words[word]:
        yell(word)
    else:
        print(word)