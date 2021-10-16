# Program for squaring numbers using list comprehension
number_list = [1, 2, 3, 4,5]
squared_list = [n*n for n in number_list]
print(squared_list)

# Program to double the number in the list
doubled_list = [n+n for n in range(1,6)]
print(doubled_list)

# program with string
name = 'Kirtika'
name_letters = [letter for letter in name]
print(name_letters)

# Program to shorten the names of the int the list
given_list = ['Tom','Harry','Jerry','Jumbo','Winne','Jetsons', 'Doremon','Schinchan']
shorten_name_list = [name for name in given_list if len(name) <=5]
print(shorten_name_list)

# program to filter even number
odd_number = [num for num in range(1,26) if num % 2 !=0]
print(odd_number)