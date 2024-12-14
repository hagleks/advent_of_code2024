import re

data_equations = []

with open("dec07_data.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        values = re.split("\:", line)
        operands = re.split(" ", values[1].strip())
        data_equations.append( ( int(values[0]), operands ) )
    input_file.close()

calibration_results = 0
for entry in data_equations:
    key = entry[0]
    operands = entry[1]

    current_level = [int(operands[0])]
    for i in range(1, len(operands)):
        new_level = []
        for j in range(len(current_level)):
            new_level.append( int(operands[i]) + current_level[j] )
            new_level.append( int(operands[i]) * current_level[j] )
            new_level.append( int( str(current_level[j]) + operands[i] ) )
        current_level = new_level

    for i in range(len(current_level)):
        if key == current_level[i]:
            calibration_results += key
            break

print ("Day 7 answer is ", calibration_results)
            
