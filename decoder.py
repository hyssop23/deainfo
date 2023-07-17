import numpy as np
import utility

#the decode will take a set of voltages in numpy array and return string
#it has additional parameters such as frequency of transmission, voltage range (HIGH, LOW), max time of transmission
#default rate is 250Hz, default voltage range is 0-15V, default max time is 10 seconds, default package size is 2
#def (.avi -> voltage pairings)

def decode(encoded_array, frequency=250, v_min = 0, v_max= 15, max_time=10, package_size=2):
    #check length of encoded array and compute length of string
    #each package will represent 1 character
    encoded_array_len = len(encoded_array)
    num_packages = int(encoded_array_len/package_size)
    decoded_string = ""

    #for each package, check its voltage value and convert it to character
    for i in range(num_packages):
        voltage_tuple = (encoded_array[i*2], encoded_array[i*2+1])
        character = utility.voltage_to_character(voltage_tuple)
        if character is None:
            continue
        decoded_string += character
    return decoded_string