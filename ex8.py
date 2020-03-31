#Takes four arguments
formatter = "{} {} {} {}"
#Passes in four arguments into formatter using the .format command to insert
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
  "Try your",
  "Own text here",
  "Maybe a poem",
  "Or a song about fear"
))
print(formatter.format(True,
 '',
 "three",
 formatter))
