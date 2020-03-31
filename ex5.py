name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
in_to_cm = 	2.54
lb_to_kg = 0.454

print("Let's talk about %s." % name)
print("He's %d inches tall or %d cm tall." % (height, height* in_to_cm))
print("He's %d pounds heavy or %d kg heavy" % (weight, weight * lb_to_kg))
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are usually %s depending on the coffee." %teeth)

#this line is tricky, try to get it exactly right
total = age + height + weight
print("If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)) 
