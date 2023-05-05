import nltk

nltk.download("punkt")
from nltk.corpus import nps_chat
from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = nps_chat.ic_pairs()
chatbot = Chat(pairs, reflections)

# Chat with the bot
while True:
    try:
        user_input = input("You: ")
        response = chatbot.converse(user_input)
        print(response)
    except KeyboardInterrupt:
        print("Goodbye!")
        break
