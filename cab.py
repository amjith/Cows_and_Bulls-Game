#!/usr/bin/env python

from random import randint;

def check_chars(inp, actual):
    bull =0 
    cow  =0
    
    if not inp.isalpha():
        print "Only alphabets are allowed\n"
        return (cow,bull)
    
    if len(inp) != len(actual):
        print "Input string must be %d chars\nTry again" %len(actual)
        return (cow,bull)

    inp_list = []
    inp_list.extend(inp)
    actual_list = []
    actual_list.extend(actual)

    for i in range( len(actual_list) ): # Find bulls and replace them with '-'
        if inp_list[i] == actual_list[i]:
            bull += 1
            inp_list[i] = actual_list[i] = '-'
    
    for i in range (len(actual_list)):
        if inp_list[i] != '-':
            try:
                actual_list[actual_list.index(inp_list[i])] = '-'
                cow += 1
            except ValueError:
                continue
    
    print "cow,bull", cow,bull
    return (cow,bull)


def has_dups(word):
    """
    >>> has_dups("")
    0
    >>> has_dups("abcdef")
    0
    >>> has_dups("aba")
    1
    >>> has_dups("abcdefc")
    1
    >>> has_dups("abcdeff")
    1
    """
    if word == "":
        return 0

    for letter in word:
        if word.count(letter) > 1:
            return 1
    return 0

def pick_word():
    """
    Function to pick a word from the file
    """
    f = open('words_4_uniq.txt','r') # This file already has only unique words with no repeated characters
    words = f.read()
    f.close()
    words = words.splitlines()
    uniq_words = [ word for word in words if has_dups(word) == 0 ]
    return uniq_words[randint(0,len(uniq_words)-1)].lower()

def main():
    actual_word = pick_word()
    found = False
    attempts = 1
    print attempts, 
    inp_word = raw_input("Input a Word: ")
    inp_word = inp_word.lower()
    found = ((0,len(actual_word)) == check_chars(inp_word, actual_word))
    while ( (not found) and  (attempts < len(actual_word) * 3)):
        attempts += 1
        print attempts, 
        inp_word = raw_input("Input a Word: ")
        found = ((0,len(actual_word)) == check_chars(inp_word, actual_word))

    if found:
        print "Victory!!\nWow! that only took like %d attempts." %attempts
    else:
        print "Fail!\nThe word was %s\nGo read a dictionary." %actual_word.upper()


if __name__=="__main__":
    import doctest
    doctest.testmod()
    main()

