# Module for taking arguments
import argparse

# Define arguments
parser = argparse.ArgumentParser("Encipher and decipher shift cipher")

parser.add_argument('-e', '--encipher', help='encipher plaintext', type=str)
parser.add_argument('-d', '--decipher', help='decipher ciphertext', type=str)
parser.add_argument('-s', '--shift', help='number of shifts to make', type=int)
parser.add_argument('-n', '--nordic', help='uses nordic alphabet', required=False, action='store_true')
parser.add_argument('-b', '--bruteforce', help='runs through every combination', required=False, type=str)

args = parser.parse_args()

# Check for selected alphabet
if args.nordic:
    alphabet = 'abcdefghijklmnopqrstuvwxyzæøå'
else:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Method for enciphering
if args.encipher:

    plainstring = args.encipher.lower()
    ciphertext = ''
    nshift = args.shift

    for i in range(len(plainstring)):

        if plainstring[i] == ' ':
            ciphertext += ' '
        else:
            offset = alphabet.find(plainstring[i]) + nshift

            if args.nordic:
                ciphertext += alphabet[offset % 29]
            else:
                ciphertext += alphabet[offset % 26]
    
    print('\n Enciphered string: ' + ciphertext)

# Method for decipehring
if args.decipher:

    cipherstring = args.decipher.lower()
    plaintext = ''
    nshift = args.shift

    for i in range(len(cipherstring)):
        if cipherstring[i] == ' ':
            plaintext += ' '
        else:
            offset = alphabet.find(cipherstring[i]) - nshift
            if args.nordic:
                plaintext += alphabet[offset % 29]
            else:
                plaintext += alphabet[offset % 26]
    
    print('\n Deciphered message: ' + plaintext)

# Method for bruteforce
if args.bruteforce:

    cipherstring = args.bruteforce.lower()
    plaintext = ''

    for i in range(1,26):
        for j in range(len(cipherstring)):
            if cipherstring[j] == ' ':  
                plaintext += ' '
            else:
                offset = alphabet.find(cipherstring[j]) - i
                if args.nordic:
                    plaintext += alphabet[offset % 29]
                else:
                    plaintext += alphabet[offset % 26]
        
        print('\n shifting ' + str(i) + ' places: ' + plaintext)
        
        plaintext = ''