while True:
    msg = input("You: ").lower()

    if msg == "hi":
        print("Bot: Hello!")
    elif msg == "how are you":
        print("Bot: I am fine.")
    elif msg == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
 