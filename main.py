name = input("What's your name? ")
age = int(input("How old are you? "))

hobbies = []
for i in range(3):
    hobbies.append(input(f"Hobby {i+1}: "))

info = {"name": name, "age": age, "hobbies": hobbies}

print(f"\nHi {info['name']}, age {info['age']}.")
print("Your hobbies:", ", ".join(info["hobbies"]))

def summary(data):
    return f"{data['name']} likes {', '.join(set(data['hobbies']))}."

print("\nSummary:", summary(info))

