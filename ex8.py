# defining the variable formatter to equal 4 brackets
formatter = "{} {} {} {}"

# call formatter and print the integers 1,2,3,4,
print(formatter.format(1, 2, 3, 4))

# print the 4 strings
print(formatter.format("one", "two", "three", "four"))

# print the 4 booleans
print(formatter.format(True, False, False, True))

# print the variable formatter 4 times
print(formatter.format(formatter, formatter, formatter, formatter))

# print this text and the commas make spaces between the lines
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
