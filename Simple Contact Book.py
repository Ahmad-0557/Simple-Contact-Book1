name = input("Enter your name: ")
phone = int(input("Enter your phone number: "))
email = input("Enter your email address: ")
contactinfo = {
    "name": name,
    "phone": phone,
    "email": email
}
if len(str(phone)) == 10:
    print("Welcome, " + contactinfo["name"] + "! Your phone number is valid.")
else:
    print("Invalid phone number.")
if "@" in email and "." in email:
    print("Your email address is valid.")
else:
    print("Invalid email address.")