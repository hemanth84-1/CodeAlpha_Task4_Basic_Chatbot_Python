def chatbot():
    print("🤖 ChatBot: Hello! I am your Python ChatBot.")
    print("🤖 ChatBot: Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["hi", "hello", "hey"]:
            print("🤖 ChatBot: Hello! How can I help you?")

        elif user_input == "how are you":
            print("🤖 ChatBot: I'm fine. Thanks for asking!")

        elif user_input in ["what is your name", "your name", "name"]:
            print("🤖 ChatBot: My name is ChatBot.")

        elif user_input == "who are you":
            print("🤖 ChatBot: I'm a simple Python chatbot.")

        elif user_input == "who made you":
            print("🤖 ChatBot: I was created using Python.")

        elif user_input == "what can you do":
            print("🤖 ChatBot: I can answer simple questions and chat with you.")

        elif user_input in ["good morning", "morning"]:
            print("🤖 ChatBot: Good Morning! Have a great day.")

        elif user_input in ["good afternoon", "afternoon"]:
            print("🤖 ChatBot: Good Afternoon!")

        elif user_input in ["good evening", "evening"]:
            print("🤖 ChatBot: Good Evening!")

        elif user_input == "tell me a joke":
            print("🤖 ChatBot: Why do programmers love Python? Because it's easy to understand! 😂")

        elif user_input in ["thanks", "thank you"]:
            print("🤖 ChatBot: You're welcome!")

        elif user_input == "bye":
            print("🤖 ChatBot: Goodbye! Have a nice day.")
            break

        else:
            print("🤖 ChatBot: Sorry, I don't understand that.")

# Run chatbot
chatbot()