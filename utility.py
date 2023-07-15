
#For 7 colors map it to voltage values: 
#red = 0, orange = 7.8, yellow=8.4, green=10.2, teal=12.4, blue=13.2, violet=13.8
color_voltage_dict = {'red':0, 'orange':7.8, 'yellow':8.4, 'green':10.2, 'teal':12.4, 'blue':13.2, 'violet':13.8}

#For each pair of colors seperated by dash map it to a single character (a-z, 0-9, ' ', '.', ',', '?', '!', and some common characters)
#Duplicate colors can be used to represent a single character
colorpair_character_dict = {'red-red':'a', 'red-orange':'b', 'red-yellow':'c', 'red-green':'d', 
                            'red-teal':'e', 'red-blue':'f', 'red-violet':'g', 'orange-red':'h', 
                            'orange-orange':'i', 'orange-yellow':'j', 'orange-green':'k', 'orange-teal':'l', 
                            'orange-blue':'m', 'orange-violet':'n', 'yellow-red':'o', 'yellow-orange':'p', 
                            'yellow-yellow':'q', 'yellow-green':'r', 'yellow-teal':'s', 'yellow-blue':'t', 
                            'yellow-violet':'u', 'green-red':'v', 'green-orange':'w', 'green-yellow':'x', 
                            'green-green':'y', 'green-teal':'z', 'green-blue':'0', 'green-violet':'1', 
                            'teal-red':'2', 'teal-orange':'3', 'teal-yellow':'4', 'teal-green':'5', 
                            'teal-teal':'6', 'teal-blue':'7', 'teal-violet':'8', 'blue-red':'9', 
                            'blue-orange':' ', 'blue-yellow':'.', 'blue-green':',', 'blue-teal':'?', 
                            'blue-blue':'!', 'blue-violet':'@', 'violet-red':'#', 'violet-orange':'$',
                            'violet-yellow':'%', 'violet-green':'^', 'violet-teal':'&', 'violet-blue':'(',
                            'violet-violet':')'}

character_colorpair_dict = {'a':'red-red', 'b':'red-orange', 'c':'red-yellow', 'd':'red-green',
                            'e':'red-teal', 'f':'red-blue', 'g':'red-violet', 'h':'orange-red',
                            'i':'orange-orange', 'j':'orange-yellow', 'k':'orange-green', 'l':'orange-teal',
                            'm':'orange-blue', 'n':'orange-violet', 'o':'yellow-red', 'p':'yellow-orange',
                            'q':'yellow-yellow', 'r':'yellow-green', 's':'yellow-teal', 't':'yellow-blue',
                            'u':'yellow-violet', 'v':'green-red', 'w':'green-orange', 'x':'green-yellow',
                            'y':'green-green', 'z':'green-teal', '0':'green-blue', '1':'green-violet',
                            '2':'teal-red', '3':'teal-orange', '4':'teal-yellow', '5':'teal-green',
                            '6':'teal-teal', '7':'teal-blue', '8':'teal-violet', '9':'blue-red',
                            ' ':'blue-orange', '.':'blue-yellow', ',':'blue-green', '?':'blue-teal',
                            '!':'blue-blue', '@':'blue-violet', '#':'violet-red', '$':'violet-orange',
                            '%':'violet-yellow', '^':'violet-green', '&':'violet-teal', '(':'violet-blue',
                            ')':'violet-violet'}

#takes single string character and returns tuple of voltages
def character_to_voltage(character):
    if not character in character_colorpair_dict.keys():
        return None
    else:
        colorpair = character_colorpair_dict[character]
        colorpair_split = colorpair.split('-')
        voltage1 = color_voltage_dict[colorpair_split[0]]
        voltage2 = color_voltage_dict[colorpair_split[1]]
        return (voltage1, voltage2)
    