# Python code to remove duplicate elements
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


# Driver Code
fruit = str["apple", "banana", "cherry", "Avocado", "Corn", "Cucumber"]
veg = str["Avocado", "Corn", "Cucumber", "Zucchini", "Pumpkin", "Okra"]
duplicate = fruit.extend(veg)
print(Remove(duplicate))
