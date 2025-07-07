# Create a BMI calculator that takes a person’s weight (in lb) and height (in in)
# then categorizes them as underweight, normal, overweight, or obese.
# bmi = weight(lb) * 703/(height(in)**2)
# Underweight: BMI < 18.5
# Normal weight: 18.5 – 24.9
# Overweight: 25 – 29.9
# Obese: 30 or more
weight = float(input("How much do you weigh?:"))
height = float(input("How tall are you?:"))
bmi = weight * 703/(height**2)
print(bmi)
if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi < 25:
    print("you are normal weight")
elif 25 <= bmi < 30:
    print("you are overweight")
else:
    print("you are obese")

