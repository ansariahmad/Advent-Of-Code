# Solution of Problem - 01

# read data from file
with open("inputs.txt", "r") as file:
    inputs = file.read().strip()

# extract the both columns and put them in separate lists
left_list = []
right_list = []

for single_row in inputs.split("\n"):
    left_list.append(int(single_row.split(" ")[0]))
    right_list.append(int(single_row.split(" ")[-1]))

# sort both columns
left_list.sort()
right_list.sort()

# 
res_1 = 0
for i,j in zip(left_list, right_list):
    res_1 += abs(i-j)

# Solution of Problem - 02

# add all numbers in a dictionary and set values to 0
right_list_dict = dict().fromkeys(right_list, 0)

# (key,val) -> (val, frequency)
for num in right_list:
    right_list_dict[num] += 1

# multiply the number in left list with its frequency in right list and add to the previous result
res_2 = 0
for num in left_list:
    if num in right_list:
        res_2 += right_list_dict[num]*num

print(f"Result of Problem 01: {res_1}\nResult of Problem 02: {res_2}")