contact_info = {
    "address": "497 Linden Boulevard",
    "city": "Brooklyn",
    "state": "New York",
    "ZIP": 11203
}

print(f'{contact_info["address"]} \n{contact_info["city"]} \n\
{contact_info["state"]} {contact_info["ZIP"]}'
      )

full_name = {
    "first name": "Gbolahan",
    "last name": "Abidemi"
}
# Adds Mr. to the full_name dictionary
full_name.update({"honorific": "Mr."})

# Adds full name to the dictionary
contact_info.update(full_name)

# Displays updated contact info
print('-' * 20)
print("Updated Address")
print('-' * 20)

print(f'{contact_info["honorific"]}{contact_info["first name"]} \
{contact_info["last name"]} \n{contact_info["address"]}\n\
{contact_info["city"]}, {contact_info["state"]} {contact_info["ZIP"]}'
      )