import re

def simple_chatbot(user_input):
    user_input = user_input.lower()

    greetings = ['hello', 'hi', 'hey', 'greetings']
    farewells = ['bye', 'goodbye', 'see you', 'farewell']
    questions = ['how are you', 'what is your name', 'who are you', 'what do you do', 'what is your favorite color']
    default_response = "I'm a simple chatbot. You can greet me or ask me something."

    if any(greeting in user_input for greeting in greetings):
        return "Hello! How can I help you today?"

    elif any(farewell in user_input for farewell in farewells):
        return "Bye! Have a great day."

    elif any(question in user_input for question in questions):
        if 'how are you' in user_input:
            return "I'm chatbot, but thanks for asking! How can I assist you?"
        elif 'what is your name' in user_input or 'who are you' in user_input:
            return "I'm a chatbot. You can call me chatbot."
        elif 'what do you do' in user_input:
            return "I'm here to chat with you and answer your questions. How Can I Help You today?"
        elif 'what is your favorite color' in user_input:
            return "As a chatbot, I don't have a favorite color!"
        else:
            return "I'm just a chatbot."

    else:
        return default_response


print("I'm chatbot! how can i help you? ")
print("___________________________________")
while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)