name = "Martin P. Ochwat"
age = 22 # not a lie
height = 73 #inches
height_cm = round(height / 0.393701)
weight = 140 #lbs
weight_kg = round(weight / 2.20462)
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %r cm tall." % height_cm
print "He's %d kg heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height_cm, weight_kg, age + height_cm + weight_kg)
