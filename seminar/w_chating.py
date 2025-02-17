import random

def chatbot_response(user_input):
    # Define responses to specific questions or patterns
    if "weather" in user_input:
        return "The weather today is sunny with a temperature of 25°C. 🌞"
    
    elif "joke" in user_input:
        jokes = [
            "Why don't skeletons fight each other? They don't have the guts! 😄",
            "What did the ocean say to the beach? Nothing, it just waved! 🌊",
            "Why did the math book look sad? Because it had too many problems! 📚"
        ]
        return random.choice(jokes)

    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! 😊"
    
    elif "name" in user_input:
        return "I'm Dipen, your friendly assistant! 💬"
    
    elif "bye" in user_input:
        return "Goodbye! Have a nice day! 👋"

    # Default unknown response if no matches found
    return "Sorry, I don't understand that. Can you ask something else? 🤔"

def start_chat():
    print("ChatBot: Hi! Type 'bye' to exit the chat.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye! 👋")
            break
        
        response = chatbot_response(user_input.lower())
        print(f"ChatBot: {response}")

# Start the chatbot
start_chat()
