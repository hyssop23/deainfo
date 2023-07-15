#this script will call an encode and decode method from the encoder.py and decoder.py files respectively

import encoder
import decoder

READ_FILE = False

if not READ_FILE:
    string_to_encode = "hello world!"
else:
    string_to_encode = open("input.txt", "r").read()

encoded_string_array = encoder.encode(string_to_encode)
print("Original string: ", string_to_encode)
print("Encoded string: ", encoded_string_array)

decoded_string = decoder.decode(encoded_string_array)
print("Decoded string: ", decoded_string)