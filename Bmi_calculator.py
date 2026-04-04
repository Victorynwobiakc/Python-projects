print("BMI Calculator")

weight = float(input("What's your current weight (in kg)? "))
height = float(input("How tall are you (in meters)? "))


bmi = round(weight / (height ** 2),2)

#check weight class
print(f"Your current BMI is {bmi}")
if bmi >= 18.5 and bmi < 25:
    print("You're normal weight")
elif bmi >= 25:
    print("You're overweight fat_fuck")