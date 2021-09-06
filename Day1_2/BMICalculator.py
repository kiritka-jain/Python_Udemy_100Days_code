print("welcome to BMI Calculator")
weight = float(input("Enter your weight in kgs"))
height = float(input("Enter your height in meters"))
bmi = weight//(height**2)

if bmi <= 18.5:
    print(f"Your Calculated BMI is:{bmi} and you are underweight.")
elif 18.5 < bmi <= 25:
    print(f"Your Calculated BMI is:{bmi} and you have normal weight.")
elif 25 < bmi <= 30:
    print(f"Your Calculated BMI is:{bmi} and you are overweight.")
elif 30 < bmi <= 35:
    print(f"Your Calculated BMI is:{bmi} and you are obese.")
else:
    print(f"Your Calculated BMI is:{bmi} and you are clinically obese.")