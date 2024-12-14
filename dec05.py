import re

page_order = {}
good_updates = []
bad_updates = []
num_updates = 0
with open("dec05_data.txt", "r") as input_file:

    lines = input_file.readlines()

    for line in lines:
        # store the page numbers that cannot come before a given page number
        #  that given page number will be the dictionary key
        has_bar = re.search("\|", line.strip())
        if has_bar is not None:
            values = re.split("\|", line.strip())
            key = int(values[1])
            if key not in page_order:
                page_order[key] = [int(values[0])]
            else:
                page_order[key].append(int(values[0]))
        else:
            num_updates += 1
            values = re.split(",", line.strip())
            good_update = True
            for i, value in enumerate(values):
                for j in range(i+1, len(values), 1):
                    # look at every page after page i; if the page you are on (page j)
                    #  is in the dictionary for page i (the key value) then it is a bad
                    #  update, as those dictionary entries are the pages that cannot come
                    #  after the page you are on
                    if int(values[j]) in page_order[int(value)]:
                        good_update = False
                        break

            if good_update:
                good_updates.append(values)
            else:
                bad_updates.append(values)

middle_pages_answer = 0
for gu in good_updates:
    middle_pages_answer += int( gu[(len(gu) // 2)] )

print ("Day 5 answer is ", middle_pages_answer)

still_wrong = True
while (still_wrong):
    still_wrong = False
    for bu in bad_updates:
        for i, value in enumerate(bu):
            for j in range(i+1, len(bu), 1):
                # find the bad entry and move it to not be bad per at least that
                #  that one rule
                # if there are no bad entries, you've fixed it and will fall out of the 
                #  loop
                if int(bu[j]) in page_order[int(value)]:
                    pop_value = bu.pop(j)
                    bu.insert(i, pop_value)
                    still_wrong = True
                    break

middle_pages_answer = 0
for bu in bad_updates:
    middle_pages_answer += int( bu[(len(bu) // 2)] )

print ("Day 5 part 2 answer is ", middle_pages_answer)
