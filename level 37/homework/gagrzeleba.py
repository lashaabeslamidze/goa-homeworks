#1 დავალება
#1.Create a list named fruits that contains the following items: "apple", "banana", "cherry", "date", and "elderberry".
#2. Print the entire list.
#3. Access and print the first and last items in the list.
#4. Add a new fruit "fig" to the list.
#5. Remove "banana" from the list.
#6. Change the value of the second item to "blueberry".
#7. Print the length of the list.






fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)
#===================



print(max(fruits))
print(min(fruits))
#===========================


fruits += ["fig"]
print(fruits)
#=====================


fruits.remove("banana")
print(fruits)
#=============================

fruits.insert(2, "blueberry")
print(fruits)
#====================================

print(len(fruits))



#2 დავალება
#1. Create a list named numbers that contains the following integers: 10, 20, 30, 40, 50, 60, 70, 80, 90.
#2. Use the append() function to add the number 100 to the end of the list.
#3. Use the insert() function to add the number 5 at the beginning of the list.
#4. Use the remove() function to remove the number 30 from the list.
#5. Use the sort() function to sort the list in ascending order.
#6. Use the reverse() function to reverse the order of the list.
#7. Use the index() function to find the index of the number 50.
#8. Use the count() function to count how many times 20 appears in the list.


number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90,]
number_list.append(100)
print(number_list)
#=======================================

number_list.insert(0, 5)
print(number_list)
#==============================

number_list.remove(30)
print(number_list)
#=================================

number_list.sort()
print(number_list)
#================================

number_list.reverse()
print(number_list)
#===========================

print(number_list.index(50))
#====================================

print(number_list.count(20))





#3 დავალება
# Create a list named numbers that contains the integers from 1 to 10.
# Use list slicing to create a new list named first_half that contains the first five elements from numbers.
# Use list slicing to create another list named second_half that contains the last five elements from numbers.
# Use a list comprehension to create a new list named squares that contains the squares of each number in the numbers list.
# Print all three lists: first_half, second_half, and square

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_half = numbers[0:5]
print(first_half)
#===========================
seconde_half = second_half[5:10]
print(seconde_half)
#========================
new_list = [i**2 for i in numbers]
print(new_list)
#========================================















#4 დავალება
# Create a list named temperatures that contains the following values representing daily temperatures: [72, 68, 75, 70, 78, 74, 71].
# Calculate and print the highest temperature using the max() function.
# Calculate and print the lowest temperature using the min() function.
# Calculate and print the average temperature using the sum() function divided by the length of the list.
# Use a list comprehension to create a new list named above_70 that contains only the temperatures above 70 degrees.
# Print the above_70 list.



temperature = [72, 68, 75, 70, 78, 74, 71]
print(max(temperature))
print(min(temperature))
print(sum(temperature))
#===============================

above_70 = [71, 72, 74, 100, 90, 95,]
print(above_70)






