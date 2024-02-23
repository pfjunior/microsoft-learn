# Truth table for AND
# true AND true = true
# true AND false = false
# false AND true = false
# false AND false = false

# Truth table for OR
# true OR true = true
# true OR false = true
# false OR true = true
# false OR false = false

# Example using if, elif and else
object_size = 10

if object_size > 5:
    print("We need to keep an eye on this object")
else:
    print("Object poses no threat")


# Example using "and" and "or" operators
object_size = 10
proximity = 9000

if object_size > 5 and proximity < 10000:
    print("Evasive maneuvers required")
else:
    print("Object poses no threat")
