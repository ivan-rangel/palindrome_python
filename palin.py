#!/usr/bin/python


def palindrome(word):
    word_len = len(word)
    word_half = ""
    word_sec_half = ""
    if (word_len % 2 == 0):
        word_half = word[:(word_len // 2)]
        # print ("first word half: " + word_half)
        word_sec_half = word[(word_len // 2):]
        # print("second word half: " + word_sec_half)
        word_sec_half = word_sec_half[::-1]
        # print("second word half reversed: " + word_sec_half)
        for x in range(len(word_half)):
            if (word_half[x] != word_sec_half[x]):
                return (word + " is not a palindrome")
        return (word + " is pal")
    else:
        word_half = word[:(word_len // 2)]
        # print ("first word half: " + word_half)
        word_sec_half = word[(word_len // 2) + 1:]
        # print("second word half " + word_sec_half)
        word_sec_half = word_sec_half[::-1]
        # print("second word half reversed: " + word_sec_half)
        for x in range(len(word_half)):
            if (word_half[x] != word_sec_half[x]):
                return (word + " is not a palindrome")
        return (word + " is pal")


new_palindrome = input("Enter a word and I'll tell you if it's a palindrome:")
print (palindrome(new_palindrome))
