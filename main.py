#this script will call an encode and decode method from the encoder.py and decoder.py files respectively

import encoder
import decoder

READ_FILE = True

if not READ_FILE:
    string_to_encode = "hello world!"
else:
    string_to_encode = open("input.txt", "r").read()

#convert full string to lower case first
string_to_encode = string_to_encode.lower()

encoded_string_array = encoder.encode(string_to_encode)
print("Original string: ", string_to_encode)
print("Encoded string: ", encoded_string_array)

#export voltage to csv file
encoder.export_voltage(encoded_string_array)
print("Exported voltage to output.csv")

decoded_string = decoder.decode(encoded_string_array)
print("Decoded string: ", decoded_string)

#print accuracy as percentage of characters decoded correctly
num_correct = 0
for i in range(len(string_to_encode)):
    if string_to_encode[i] == decoded_string[i]:
        num_correct += 1
print("Accuracy: ", num_correct/len(string_to_encode)*100, "%")
