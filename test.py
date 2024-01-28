message = input("Enter Text please: ")
message_filter = ""

for char in message:
    if(char.isalnum()):
        message_filter += char.lower()

if(message_filter == message_filter[::-1]):
    print(f"{message} is a Palindrome")
else:
    print(f"{message} is not a Palindrome")
