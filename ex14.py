#prompting user input and passing
from sys import argv

script, user_name = argv

#user input as prompt
prompt ='>'

print (f"Hi {format(user_name).upper()}, I'm {script} script")
print ("I'd like to ask you a few questions.")
print (f"{format(user_name).upper()},Do you like how I am?")

likes = input(prompt)

print (f"Where do you live {user_name}?")
lives = input(prompt)

print ("Which  computer do you have?")
computer = input(prompt).upper()

print (f"""
{format(user_name).upper()} said you {likes} me.
You currently live in {lives}.
You have {computer} machine
""")


