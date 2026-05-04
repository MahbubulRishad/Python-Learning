# max return
from basics.Function.FunctionExample import sum_number


def max_number(nums):
    return  max(nums)

set_of_numbers = [10,21,23,14,84,26,45,86,82,122,45,35]
find_max = max_number(set_of_numbers)
print("Max value: ", find_max)
#or
print("Max value2: ", max(set_of_numbers))

# min return
def min_number(nums):
    return  min(nums)

set_of_numbers = [10,21,23,14,84,26,45,86,82,122,45,35]
find_min = min_number(set_of_numbers)
print("Min value: ", find_min)
#or
print("Min value2: ", min(set_of_numbers))

#Round
print("Round: ", round(3.1416251,3))

#sum
print("Sum: ", sum(set_of_numbers))

#length
print("Length: ", len("Rishad"))

#sort
print("Sorted - min to max: ", sorted(set_of_numbers)) #min to max

#sort
print ("Sorted - max-min: ", sorted(set_of_numbers, reverse= True)) #max-min

#average
average  = sum(set_of_numbers) / len(set_of_numbers)
print(f"Average: , {average:.2f}")
