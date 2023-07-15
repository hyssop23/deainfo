import numpy as np
import utility
#the encode will take string and return encoded voltages represented as numpy array
#it has additional parameters such as frequency of transmission, voltage range (HIGH, LOW), max time of transmission
#default rate is 250Hz, default voltage range is 0-15V, default max time is 10 seconds, default package size is 2
def encode(string_to_encode, frequency=250, v_min = 0, v_max= 15, max_time=10, package_size=2):
    
    #check length of string and compute length of numpy array needed
    #each package will represent 1 character
    str_len = len(string_to_encode)
    num_packages = str_len*package_size
    encoded_array = np.zeros(num_packages)
    print("Length of string: ", str_len)
    print("encoded array length: ", len(encoded_array))
    #for each character check its dictionary value of voltage tuple and unpack it into the encoded array
    for i in range(str_len):
        voltage_tuple = utility.character_to_voltage(string_to_encode[i])
        if voltage_tuple is None:
            continue
        encoded_array[i*2] = voltage_tuple[0]
        encoded_array[i*2+1] = voltage_tuple[1]
    return encoded_array