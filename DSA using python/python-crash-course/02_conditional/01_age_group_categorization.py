# classify a person's age group: child(<13), teenager(13-19), adult(20-59), senior(60+)

user_age = int(input("Provide me an age: "))

if user_age < 13:
    print(f"child")
elif user_age >= 13 and user_age <= 19:
    print(f"teenager")
elif user_age >= 20 and user_age <= 59:
    print("adult")
else:
    print("senior")
