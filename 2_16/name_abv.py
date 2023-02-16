first_name, last_name = input("Enter first name and last name separated by a space: ").lower().split()
abv_name = first_name[0] + last_name[:7]
print(abv_name)
