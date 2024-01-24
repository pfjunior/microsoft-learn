# ask the candidate a question
activity = input( "How would you like to spend your evening?\n(A) Reading a book\n(B) Attending a party\n" )

# print out which activity they chose
print( f"You chose {activity}.")

if activity == "A":
    print( "Nice choice!" )
elif activity == "B":
    print( "Sounds fun!" )
else:
    print("You must type A or B, let's just say you like to read.")