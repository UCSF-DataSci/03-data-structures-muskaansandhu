#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [
    "We suffer more in imagination than in reality. - Seneca", 
    "It never ceases to amaze me: we all love ourselves more than other people, but care more about their opinion than our own. - Marcus Aurelius",
    "First say to yourself what you would be; and then do what you have to do. - Epictetus",
    "Know, first, who you are, and then adorn yourself accordingly. - Epictetus",
    "Luck is what happens when preparation meets opportunity. - Seneca", 
    "Our life is what our thoughts make it. - Marcus Aurelius", 
    "Give yourself a gift: the present moment. - Marcus Aurelius", 
    "Spread love everywhere you go. Let no one ever come to you without leaving happier.  - Mother Teresa", 
    "It is during our darkest moments that we must focus to see the light. - Aristotle",
    "Education is bitter, but its fruit is sweet. - Aristotle"
    ]

def get_quote_of_the_day(quotes):
    today = date.today()
    random.seed(today)
    todays_quote=random.choice(quotes)
    
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 /path/to/quote_generator.py >> /path/to/daily_quote.txt