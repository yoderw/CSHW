name = str(input("What is your name? "))
action = str(input("Ok. Now enter an action: "))

print()
print("I'm sorry, {}. I'm afraid I can't do that.".format(name))
print("(The action \"{}\" was not performed.)".format(action))