"""Files"""
#1.
name = input("What is your name? ")
out_file = open("name.txt", 'r')
print(name, file=out_file)
out_file.close()

#2
in_file = open("name.txt", 'r')
name = in_file.read()
name = name.strip()
in_file.close()
print("Your name is", name)

#3
in_file = open("number.txt",  'r')
first_number = in_file.readline()
first_number = int(first_number)

second_number = int(in_file.readline())
total = first_number + second_number
print(total)

#3 extended
in_file = open("number.txt",'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)



