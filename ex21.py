def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(25, 5)
height = subtract (75, 4)
weight = multiply(20, 10)
iq = divide (1000, 10)

print "Age: %d, Height %d, Weight %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra creadit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand."
