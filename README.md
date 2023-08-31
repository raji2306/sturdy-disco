# Advanced User Profile README Generator

# Collect user inputs
name = input("Enter your name: ")
username = input("Enter your GitHub username: ")
bio = input("Enter a short bio: ")
email = input("Enter your email address: ")

# Choose languages known
languages_known = input("Enter languages known (comma-separated): ").split(',')

# Choose profession
professions = ["Developer", "Designer", "Data Scientist", "Product Manager", "Other"]
print("Choose your profession:")
for index, profession in enumerate(professions, start=1):
    print(f"{index}. {profession}")

profession_choice = int(input("Enter the number corresponding to your profession: "))
chosen_profession = professions[profession_choice - 1]

# Generate the README content
readme_content = f"""
# Hi there! 👋 I'm {name}

{bio}

## Languages Known

- {', '.join(languages_known)}

## Profession

{chosen_profession}

## Get in Touch

📧 Email: {email}

🌐 GitHub: [github.com/{username}](https://github.com/{username})
"""

# Write the generated content to a README file
with open("PROFILE.md", "w") as readme_file:
    readme_file.write(readme_content)

print("PROFILE.md generated successfully!")
