# problem 1
# Given a string, write a function to reverse it. Do this using a loop.
def reverse_string(str):
    storage = []
    for i in range(len(str) - 1, -1, -1):
        storage.append(str[i])
    return ''.join(storage)


# problem 2
# Sal's classroom has a bag of alphabet magnets.
# She wants to know if she can spell her friend's name using the letters in the bag.
# Write a function that will take a list of letters and a name and
# print out yes if the name can be spelled and no otherwise.

def CanYouSpell(letters, name):
    for char in name:
        if char in letters:
            letters.remove(char)
        else:
            return 'NO'
    return 'YES'
