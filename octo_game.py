import random

print("🐙 Welcome to Octo Meme Challenge 🐙")
choices = ["meme", "joke", "fact"]
user_choice = input("Pick one: meme, joke, or fact: ")

memes = ["Stay legendary!", "Coding is life.", "Octo mode activated!"]
jokes = ["Why did the octopus cross the road? Tentacles!", "Git commit, then git out."]
facts = ["Octopuses have three hearts!", "They can change color and texture to blend in."]

if user_choice == "meme":
    print(random.choice(memes))
elif user_choice == "joke":
    print(random.choice(jokes))
elif user_choice == "fact":
    print(random.choice(facts))
else:
    print("Invalid choice—but hey, you're still awesome!")
