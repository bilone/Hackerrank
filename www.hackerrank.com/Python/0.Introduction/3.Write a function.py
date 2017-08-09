def leap(year):
    isleap = False

    # Write your logic here
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                isleap = True
        else:
            isleap = True

    return isleap


year = int(input())
print(leap(year))
