base_string = "cameron"

empty_list = []

#here i'm looping through each letter in the string and appending it
for letter in base_string:
    empty_list.append(letter)

#here i'm reversing it
empty_list.reverse()

#then i create an empty string
reversed_string = ""

#again loop throught the list and add each letter to the new string
for letter in empty_list:
    reversed_string += letter

print("Original String:", base_string)
print("reversed String:", reversed_string)