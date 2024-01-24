print("Hello, Contosoville!")
# This is a comment that won't be interpreted as a command.

# ---- variables ----
# Associate variable town with the value "Contosoville"
town = "Contosoville"

# Print a message about the secret location
print( "The town I am looking for is " + town )

# use a variable named year to "remember" the value 1990
year = 1990

# print a message to see what year it is
print( f"The year is {year}..." )

year = year + 36

# print a message to see what year it is now
print( f"The year is now {year}..." )


# ---- functions ----
# Define a power (function) to chant a phrase
def chant( phrase ):
    # Glue three copies together and print it as a message
    print( phrase + phrase + phrase )

# Invoke the power to chant on the phrase "Contosoville!"
chant( "Contosoville!" )


# ---- conditionals ----
# if we're in 1990
if year == 1990:
    print( "I left you a message on your answering machine!" )
# if we're in 2026
if year == 2026:
    print( "I sent you a text message!" )