fruit = ["apple", "banana", "cherry", "Avocado", "Corn", "Cucumber"]
veg = ["Avocado", "Corn", "Cucumber", "Zucchini", "Pumpkin", "Okra"]

fruit.extend(veg)
print(fruit)


def remove_duplicate_from_list():
    fruits = ["apple", "banana", "cherry", "Avocado", "Corn", "Cucumber"]
    vegetables = ["Avocado", "Corn", "Cucumber", "Zucchini", "Pumpkin", "Okra"]
    for fruits in vegetables:
        fruits.append(fruits.remove())
    return fruits


print(remove_duplicate_from_list())
