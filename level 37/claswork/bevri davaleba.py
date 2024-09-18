#1
nums = [1, 4, 8, 9, 5]

nums.insert(1,3)
nums.remove(9)
nums.insert(0, nums.count(8))
print(nums[3])

#2
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


#3
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









