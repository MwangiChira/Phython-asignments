# Dictionary to store personal information
personal_info = {}
name = input("Enter your name: ")
age = input("enter your age: ")
favorite_color = input("enter your favorite color: ")
personal_info["name"] = name
personal_info["age"] = age
personal_info["favorite color"] = favorite_color
print("personal information:")
for key, value in personal_info.items():
    print(f"{key}:{value}")