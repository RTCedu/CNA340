# A Mad Lib is a fun, interactive word game where players fill in blanks with specific types of words
# (like nouns, verbs, adjectives, etc.) to create a humorous or surprising story.
# The structure of the story is pre-written, but key parts are left blank for the player to fill in
# without knowing the full context. Once all the blanks are filled, the story is revealed,
# often resulting in funny or unexpected outcomes.
from tabnanny import verbose

# How it works:
# 1. The Setup: A short story is written with blanks where key words should be
#    (e.g., the name of a person, a place, or an action).
# 2. Prompting for Words: The player is asked to provide words to fill in the blanks without knowing the full story.
#    For example:
#       - "Give me a noun."
#       - "Give me an adjective."
#       - "Give me a verb."
# 3. Creating the Story: Once all the words are filled in, they are inserted into the story's template,
#    creating a unique and often humorous final story.

# Example:
# Story Template: One day, a {adjective} {noun} decided to {verb} to the {place}.
# User Input:
#     - Adjective: "happy"
#     - Noun: "dog"
#     - Verb: "run"
#     - Place: "park"
# Final Story: One day, a happy dog decided to run to the park.

# Assignment:
# Create a Python program that asks the user for various inputs and generates a fun Mad Lib story using
# input(), print(), and f-strings.

# Deliverables:
# 1. Pick a Mad Lib from https://www.thewordfinder.com/wordlibs/.
# 2. Use the input() function to gather words from the user in the console and save them to variables.
# 3. Create a template using your chosen Mad Lib and generate a fun story using f-strings to print the final result.



#Madlib Assignment

number = input("Enter a grade year."),
adjective1 = input("Give me an Adjective!"),
adjective2 = input("Give me another adjective!"),
adjective3 = input("Give me an adjective!"),
name1 = input("What is your frend's name?"),
name2 = input("What is your other friend's name?"),
noun1 = input("Give me a noun?"),
plural_noun = input("Give me a plular_noun!")
noun2 = input("Give me a noun!"),
noun3 = input("Give me a noun!"),
noun4 = input("Give me a noun!"),
verb = input("Give me a verb!"),
adjective4 = input("Give me an adjective!"),

print(f"Today was my first day of input{number} grade."),
print(f"My teacher is ms.. She seems{adjective1} and {adjective2}."),
print(f"I think her class will be pretty {adjective3}."),
print(f"My friends {name1} and {name2} are also in my class."),
print(f"We messed around during class by hiding {noun1} in peoples'{plural_noun} and asking questions about {noun2}")
print(f"The teacher got really {noun3} at us and told us that we have to go to the {noun4}."),
print(f"This just made us {verb} more. It was a {adjective4} first day of school.!")
#final_story. I don't understand why the final story is not running.
#update. Its late but I finally have my program running. :)








