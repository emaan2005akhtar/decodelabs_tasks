print("🤖 Welcome to Rule-Based AI Chatbot!")
print("Type 'help' to see available commands.")
print("Type 'bye' or 'exit' to stop.\n")

while True:
    user = input("You: ").lower().strip()

    # Greetings
    if user == "hi" or user == "hello":
        print("Bot: Hello! How can I help you? 😊")

    elif user == "good morning":
        print("Bot: Good Morning! Have a wonderful day. ☀️")

    elif user == "good night":
        print("Bot: Good Night! Sweet dreams. 🌙")

    # Basic Questions
    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is Rule-Based AI Chatbot.")

    elif user == "who are you":
        print("Bot: I am a simple chatbot created using Python and if-else conditions.")

    elif user == "what can you do":
        print("Bot: I can answer basic predefined questions.")

    elif user == "who made you":
        print("Bot: I was created by an AI Intern.")

    elif user == "thank you":
        print("Bot: You're welcome! 😊")

    # Help Command
    elif user == "help":
        print("\nBot: You can ask me:")
        print("1. hi")
        print("2. hello")
        print("3. how are you")
        print("4. what is your name")
        print("5. who are you")
        print("6. who made you")
        print("7. what can you do")
        print("8. good morning")
        print("9. good night")
        print("10. thank you")
        print("11. bye")
        print()

    # Exit
    elif user == "bye" or user == "exit":
        print("Bot: Goodbye! Have a nice day. 👋")
        break

    # Unknown Input
    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")