# Prompting user for number of attendees
attendees = int(input("Enter number of attendees: "))

# Determining venue based on number of attendees
if attendees > 100:
    venue = "large hall"
else:
    venue = "conference room"

# Recommending additional facilities based on number of attendees
additional_facilities = []
if attendees > 50:
    additional_facilities.append("audio system")
if attendees > 80:
    additional_facilities.append("projector")

# Displaying venue and additional facilities recommendation
print("Venue:", venue)
if additional_facilities:
    print("Additional facilities recommended:", ', '.join(additional_facilities))
else:
    print("No additional facilities recommended.")
