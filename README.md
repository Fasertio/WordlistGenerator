# WordlistGenerator
Wordlist generator starting from a single string for targeted bruteforce.

Creates permutations from a single string to generate a wordlist of words similar to the starting one. Useful in bruteforce starting from a known password not randomly generated.

An example of a decomposition:
banana123! -> [“banana”, “123”,“!”]
[“banana”] -> [“banana”, “banana”, “bAnAnA”,...]
[“123”] -> [“123”, “000”, “999”,...]
[“!”] -> [“@”, “#”,“<”,...]
It then composes the strings while maintaining the original structure:
[“banana123!”,“Banana000@”,“bAnAnA999#”,...]

Usage:    

    py wordlist_generator.py -h
      _  _  _                _ _       _           ______
     | || || |              | | |     (_)     _   / _____)
     | || || | ___   ____ _ | | |      _  ___| |_| /  ___  ____ ____
     | ||_|| |/ _ \ / ___) || | |     | |/___)  _) | (___)/ _  )  _ \
     | |___| | |_| | |  ( (_| | |_____| |___ | |_| \____/( (/ /| | | |
      \______|\___/|_|   \____|_______)_(___/ \___)_____/ \____)_| |_|   by Fasertio
      usage: wordlist_generator.py [-h] [-o OUTPUT] [-l LIMIT] string
      Generate wordlist starting since a single string
      positional arguments:
      string                Input string, more than one for more wordlists
      options:
      -h, --help            show this help message and exit
      -o OUTPUT, --output OUTPUT
                        Wordlist output filename (default: wordlist.txt)
      -l LIMIT, --limit LIMIT
                        Write in wordlist only the first words number
