#1Create a string named template with the following content: "Hello, {name}. Welcome to {place}."
# Use the format() function to replace {name} with "Alice" and {place} with "Wonderland". Store the result in a variable named formatted_string and print it.

name = "Lasha"
place = "Batumi"

format = f"hello {name}, welcome to {place}"
formattted_strings = "My name is {name}, I'm from {place}".format(name="Alice",place="Wonderland")
print(formattted_strings)
#===============================================





#2Create a list named words that contains the following strings: "apple", "banana", "cherry".
# Use the join() function to combine these words into a single string, separated by a comma and a space ", ". Store the result in a variable named fruit_string and print it.




words =", " .join(["apple", "banana", "cherry"])
print(words)
#====================================================







#3Create a string named sentence with the following content: "The quick brown fox jumps over the lazy dog."
# Use the split() function to split the sentence into a list of words. Store the result in a variable named words_list and print it.



words_list = "The quick brown fox jumps over the lazy dog.".split(" ")
print(words_list)
#===============================================







#4 Create a string named quote with the following content: "To be or not to be, that is the question."
# Use the replace() function to replace the word "be" with "code". Store the result in a variable named modified_quote and print it.



modified_quote = "To be or not to be, that is the question.".replace("be","code")
print(modified_quote)



#===============================================

#5 Create a string named mixed_case with the following content: "PyThOn Is AwEsOmE!"
# Use the lower() function to convert the entire string to lowercase. Store the result in a variable named lowercase_string and print it.

mixed_case = "PyThOn Is AwEsOmE!"
print(mixed_case.lower()) 

#==============================================


#6 Create a string named greeting with the following content: "good morning"
# Use the upper() function to convert the entire string to uppercase. Store the result in a variable named uppercase_greeting and print it.

greeting = "good morning"
print(greeting.upper())





