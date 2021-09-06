name_1 = input("Enter your name.")
name_2 = input("Enter partner's name.")
combined_name = (name_1+name_2).lower()
true_count =0
love_count =0
letter_in_true ='true'
letter_in_love ='love'
for letter in combined_name:
    if letter in letter_in_true:
        true_count += 1
    if letter in letter_in_love:
        love_count += 1
score = str(true_count)+str(love_count)
love_score = int(score)
if love_score <10 or love_score>90:
    print("Your score is"+score+", you go together like coke amd mentos")
elif love_score >=40 and love_score <=50:
    print("Your score is" + score + ", you are alright together")
else:
    print("Your score is"+score)
