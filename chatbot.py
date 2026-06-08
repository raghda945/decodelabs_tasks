name = input("Enter your name: ")

while True:
    user = input("You: ").lower()

    if user == "hi":
        print("Bot: Hello", name)

    elif user == "how are you":
        print("Bot: I am fine")

    elif user == "what is your name":
        print("Bot: I am AI Bot")

    elif user == "bye":
        print("Bot: Goodbye")
        break