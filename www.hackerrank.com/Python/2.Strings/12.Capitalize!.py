def capitalize(string):
    l = string.split(" ") # transform string in list
    a = [i.capitalize() for i in l] # capitalize each item of the list

    return " ".join(a) # transform the list of strings, in one string

    



string = input()
capitalized_string = capitalize(string)
print(capitalized_string)