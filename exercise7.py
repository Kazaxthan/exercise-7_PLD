
#Exercise 7: Return the count of a given substring from a string
#Write a program to find how many times substring “Emma” appears in the given string.

main_word = input (str("type the words:"))
count_of_words = input (str("the the word you want to count:"))
     
    
cnt = main_word.count(count_of_words)

print ("The word was used:",cnt,"times")