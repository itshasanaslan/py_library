genders = ["male", "female"]
ages = {range(0, 31): "young", range(31, 51): "middle aged",range(52,99999):"old"}
heights = {range(0,160):"short",range(160,180):"middle-height",range(180,1000):"tall"}
while True:
    try:
        user_age,user_height = int(input("Enter your age: ")),int(input("Enter your height: "))
        user_gender = input("Enter your gender: ").lower()
        if user_gender not in genders:
            print("Please enter a valid gender!")
            continue
        for key in ages:
            if user_age in key:
                user_age = key

        for key in heights:
            if user_height in key:
                user_height = key

        print(f"You are a {ages[user_age]} {heights[user_height]} {user_gender}.")

    except:
        print("Invalid type")
        continue
