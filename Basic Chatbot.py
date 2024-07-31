import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thanks for asking!', 'Doing well, thank you!', 'I am fine, how about you?']),
    (r'what is your name?', ['I am a chatbot created by a Aman kumar Pandey.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Take care!']),
    (r'(.*)', ['Sorry, I do not understand that.'])
]

chatbot = Chat(pairs, reflections)

def chatbot_response(user_input):
    return chatbot.respond(user_input)

print("Chatbot: Hi! How can I help you? (Type 'bye' to exit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
