import re

min_diff = 1
max_diff = 3

# return -1 if a safe report
# if not safe, return the index where the algorithm fails
def is_good_report(report:[]) -> int:

    is_increasing = False
    is_decreasing = False

    for i in range(1,len(report)):
        diff = report[i-1] - report[i]
        if abs(diff) < min_diff or abs(diff) > max_diff:
            return i
        if diff < 0:
            is_increasing = True
        else:
            is_decreasing = True
        
        if is_increasing and is_decreasing:
            return i
    
    return -1


reports = []
with open("dec02_data.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        report = []
        values = re.split(" ", line)
        for value in values:
            report.append(int(value.strip()))
        reports.append(report)
    
    input_file.close()

# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

num_safe_reports = 0
failure_index = []

for report in reports:
    value = is_good_report(report)
    failure_index.append(value)
    if value == -1:
        num_safe_reports += 1

print ("Number of safe reports is ", num_safe_reports)

# Update your analysis by handling situations where the Problem Dampener can remove 
# a single level from unsafe reports. How many reports are now safe?

handled_reports = 0
for i in range(len(reports)):
    if failure_index[i] == -1:
        continue
    else:
        for j in range(len(reports[i])):
            hold_value = reports[i].pop(j)
            value = is_good_report(reports[i])
            if value == -1:
                handled_reports += 1
                break
            else:
                reports[i].insert(j, hold_value)

print ("Number of safe reports after error correct is ", (num_safe_reports + handled_reports))

