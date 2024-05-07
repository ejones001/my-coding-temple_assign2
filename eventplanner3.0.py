# Prompting user for number of attendees
attendees = int(input("Enter number of attendees: "))

# Determining venue based on number of attendees
if attendees > 100:
    venue = "large hall"
else:
    venue = "conference room"

# Prompting user for preference for vegetarian food
vegetarian_choice = input("Do you want vegetarian food? (yes/no): ")

# Recommending caterer based on vegetarian food preference
if vegetarian_choice.lower() == "yes":
    caterer = "Veggie Delight Caterers"
else:
    caterer = "Gourmet Meals Caterers"

# Displaying venue, caterer, and additional facilities recommendation
print("Venue:", venue)
print("Caterer:", caterer)
