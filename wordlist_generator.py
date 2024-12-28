#wordlist generator

import re
from itertools import product
import string
import argparse

def scompose_string(scomp_string):   
    pattern = r'[a-zA-Z]+|\d+|[^a-zA-Z\d]'
    matches = re.findall(pattern, scomp_string)
    return matches

def generatePermutation(array):
    results = []
    symbols = list(string.punctuation)

    for el in array:
        if el.isdigit():
            options = [(str(i) for i in range(10)) for _ in el]
            combinations = [''.join(comb) for comb in product(*options)]
        elif all(not char.isalnum() for char in el):
 
            options = [symbols for _ in el]
            combinations = [''.join(comb) for comb in product(*options)]
        else:
            options = [(car.lower(), car.upper()) for car in el]
            combinations = [''.join(comb) for comb in product(*options)]

        results.append(combinations)

    return results

def compose_string(comp_arr):
    return [''.join(comb) for comb in product(*comp_arr)]

def write_wordlist(output_arr,filename,limit):
    c = 0
    with open(filename, 'w') as file:
        for i, combination in enumerate(output_arr):
            if limit is not None and i >= limit:
                break
            file.write(combination + '\n')
            c=c+1
    return c

def main():

    ascii_art = """
 _  _  _                _ _       _           ______             
| || || |              | | |     (_)     _   / _____)            
| || || | ___   ____ _ | | |      _  ___| |_| /  ___  ____ ____  
| ||_|| |/ _ \ / ___) || | |     | |/___)  _) | (___)/ _  )  _ \ 
| |___| | |_| | |  ( (_| | |_____| |___ | |_| \____/( (/ /| | | |
 \______|\___/|_|   \____|_______)_(___/ \___)_____/ \____)_| |_|   by Fasertio
    """
    print(ascii_art)

    parser = argparse.ArgumentParser(description="Generate wordlist starting since a single string")
    parser.add_argument('string', help="Input string, more than one for more wordlists")
    parser.add_argument('-o', '--output', type=str, default="wordlist.txt", help="Wordlist output filename (default: wordlist.txt)")
    parser.add_argument('-l', '--limit', type=int, help="Write in wordlist only the first words number")

    args = parser.parse_args()

    num_string = write_wordlist(compose_string(generatePermutation(scompose_string(args.string))),args.output, args.limit)

    print(f"[+] Wordlist with {num_string} of words created: {args.output}")

if __name__== "__main__":
    main()
