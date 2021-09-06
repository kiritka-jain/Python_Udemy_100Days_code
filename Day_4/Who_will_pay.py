import random

persons_list = list(map(str, input().split(", ")))
total_person = len(persons_list)
person_number = random.randint(0,total_person-1)
person_name = persons_list[person_number]
print("Today's bill will be paid by:"+ person_name)

