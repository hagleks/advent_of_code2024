import re

left_values = []
right_values = []

with open("dec01_data.txt", "r") as input_file:

    lines = input_file.readlines()

    for line in lines:
        values = re.split("   ", line)
        left_values.append( int(values[0].strip()) )
        right_values.append( int(values[1].strip()) )

    input_file.close()

if len(left_values) != len(right_values):
    raise ("WTF, the left and right lists are not the same length")

left_values.sort()
right_values.sort()
difference = 0
for i in range(len(left_values)):
    difference += abs(left_values[i] - right_values[i])

print ("Day 1, Question 1, answer is: ", difference)

right_values_dict = {}
for value in right_values:
    if value not in right_values_dict:
        right_values_dict[value] = 1
    else:
        right_values_dict[value] += 1

similarity = 0
for value in left_values:
    similarity += value * right_values_dict.get(value, 0)

print ("Day 1, Question 2, answer is: ", similarity)
