def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = ", weight)
    BMI = weight/(height*height)
    print("BMI = ", f"{BMI: .2f}")
    if BMI < 18.5:
        print("Under Weight")
        return -1
    elif BMI > 25.0:
        print("Over Weight")
        return 1
    else:
        print("Normal Weight")
        return 0


calculate_bmi(weight=57, height=1.73)
calculate_bmi(weight=55, height=1.80)
calculate_bmi(weight=77, height=1.70)