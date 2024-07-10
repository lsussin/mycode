#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Accessing Open APIs with Python"""

# standard library
import json

# 3rd party library
import requests

# Define URL as a global constant (this will not change)
MAJORTOM = 'https://anapiofficeandfire.com/api/books'

def main():
    """making API requests"""
    
    # Call the web service
    resp = requests.get(MAJORTOM)  # sends an HTTP GET
    
    # strip JSON data off response and convert
    # to python data types
    data = resp.json()
            
    # display our Pythonic data
    print("\n\nConverted Python data")
    print(data)
    
    print('\n\nThe Author is: ', data.get('authors'))
    
    names = data.get('name') # people is a list of dict
    print(names) # this is the list of dict

    # for-loop across astros
    # display names of those in space
    for name in names:
        print("Game of throne book {name['numberOfPages]} pages long:", names['name'])

if __name__ == '__main__':
    main()

