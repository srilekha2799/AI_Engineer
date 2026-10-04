def profile(name, batch, goal):
    print("Name: " + name)
    print("Batch: " + batch)
    print("Goal: " + goal + "\n")


name = input("Name: ")
batch = input("Batch: ")
goal = input("Goal: ")


skills = []

skills.append(input("Enter Skill1: "))
skills.append(input("Enter Skill2: "))
skills.append(input("Enter Skill3: "))

recommendation = input("\nEnter Recommendation: ")

print("========== AI ENGINEER PROFILE ==========\n")
profile(name, batch, goal)
print("\nSkills:")
for skill in skills:
    print(skill)
print("\nRecommendation:", recommendation)