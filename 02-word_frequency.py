#!/usr/bin/env python3
"""
Word Frequency Counter

This script reads a text file and counts the frequency of each word, ignoring case.

Usage: python word_frequency.py <input_file>


Your task:
- Complete the word_frequency() function to count word frequencies sorted alphabetically
- Test your script on 'alice_in_wonderland.txt'

Hints:
- Use a dictionary to store word frequencies
- Consider using the lower() method to ignore case
- The split() method can be useful for splitting text into words
"""

import sys
import string

def word_frequency(text):
    frequencies = {} # Dictionary to store word frequencies
    
    lower_case = text.lower() #using .lower() to turn everything into lowercase
    sep_words = lower_case.split() #using .split() to split text into words 

    for word in sep_words:
        word = word.strip(string.punctuation) #removes trailing and leading whitespace and punctuation 

        if word: 
            frequencies[word] = frequencies.get(word, 0) + 1 #couting words 
    return dict(sorted(frequencies.items())) #adding words to sorted dictionary 


# Scaffold for opening a file and running word_frequency() on the contents
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_frequency.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            text = file.read() # Read the entire file into a string
        
        frequencies = word_frequency(text)
        
        # Print results
        for word, count in frequencies.items():
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    
    print(f"Word frequencies for '{filename}':")
    print(frequencies)