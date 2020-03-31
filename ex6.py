#declaring types_of_people as integer 10
types_of_people = 10

#formats a string using types_of_people as an integer
x = "There are %d types of people." %types_of_people

# sets the following variables as strings
binary ="binary"
do_not = "don't"

#formats the string y with two format strings, binary and do_not
y = f"Those who know {binary} and those who {do_not}."

#prints outputs of x and y
print(x)
print(y)

#format strings using x and y
print(f"I said: {x}")
print(f"I also said: '{y}'")

#boolean variable
hilarious=False
#sets a string using blank {} format string
joke_evaluation = "Isn't that joke so funny?! {}"
# prints the joke_evaluation string takes hilarious as an argument, putting
# it into the format {} above.
print(joke_evaluation.format(hilarious))

w= "This is the left side of..."
e= "a string with a right side."

#concatenate w and e into one string
print(w + e)
