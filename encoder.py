import numpy as np
import utility
#the encode will take string and return encoded voltages represented as numpy array
#it has additional parameters such as frequency of transmission, voltage range (HIGH, LOW), max time of transmission
#default rate is 250Hz, default voltage range is 0-15kV, default max time is 10 seconds, default package size is 2
def encode(string_to_encode, frequency=250, v_min = 0, v_max= 15, max_time=10, package_size=2):
    #each wave can represent 2 colors
    colors_per_second = frequency*2

    #check length of string and compute length of numpy array needed
    #each package will represent 1 character
    str_len = len(string_to_encode)
    num_packages = str_len*package_size
    encoded_array = np.zeros(num_packages)
    
    #for each character check its dictionary value of voltage tuple and unpack it into the encoded array
    for i in range(str_len):
        voltage_tuple = utility.character_to_voltage(string_to_encode[i])
        if voltage_tuple is None:
            continue
        encoded_array[i*2] = voltage_tuple[0]
        encoded_array[i*2+1] = voltage_tuple[1]
    #print total number of time in seconds
    print("Total time: ", len(encoded_array)/colors_per_second, " seconds")
    return encoded_array

#This method takes an encoded string and exports a csv file deliminated with commas, with the format:
#line 1 must say: Type (AC | DC): Time Start [sec], Time End [sec], Value [V]
#line 2 must say: AC: 0.000000	1	1
#all other lines use DC instead of AC and start time based on 250 Hz frequency and value is encoded voltage*1000
def export_voltage(encoded_string_array, frequency=250, v_min = 0, v_max= 15, max_time=10, package_size=2):
    colors_per_second = frequency*2
    
    #open file for writing
    f = open("output.csv", "w")
    f.write("Type (AC | DC): Time Start [sec], Time End [sec], Value [V]\n")
    f.write("AC: 0.000000,	1,	1\n")
    #write each line
    for i in range(len(encoded_string_array)):
        f.write("DC: " + str(i/colors_per_second) + ", " + str((i+1)/colors_per_second) + ", " + str(encoded_string_array[i]*1000) + "\n")
    f.close()