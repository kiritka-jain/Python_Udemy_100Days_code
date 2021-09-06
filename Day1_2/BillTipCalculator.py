print("Welcome to tip claculator.")
bill = float(input("What was the total Bill?"))
total_people = int(input("How many people to split the bill?"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
tip = (100+tip_percentage)/100
calculated_tip = round((bill*tip)/total_people,2)
print(f"Each person should pay: Rs.{calculated_tip}")
