scores_of_students = list(map(int, input("Enter the scores of the students").split(", ")))
'''Method_1:'''
# highest_score = max(scores_of_students)
'''Method_2:'''
highest_score = 0
for score in scores_of_students:
    if score > highest_score:
        highest_score = score
print(highest_score)