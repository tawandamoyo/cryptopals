import string


input_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
letters = list(string.ascii_lowercase)

print(letters)

def xor_decrpyt(input):
    input_as_bytes = bytes.fromhex(input)
    
    for letter in letters:
        letter_in_bytes = str.encode(letter)
        xored = bytes(x ^ y for x, y in zip(input_as_bytes, letter_in_bytes)).hex()
        
    
xor_decrpyt(input_string)