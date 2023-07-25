import nltk
from nltk.chat.util import Chat, reflections
import random

pairs = [
    ['my name is (.*)', ['Hi %1! How can I help you?']],
    ['(hi|hello|hey)', ['Hi there! How can I help you?', 'Hello! How can I help you?', 'Hey! How can I help you?']],
    ['what is your name?', ['I am chatbot']],
    ['how are you?', ['I am doing well, thank you. How about you?']],
    ['(.*) age?', ['I am a computer program and I do not have an age.']],
    ['(.*) created you?', ['I was created by a team of developers using Python and NLTK.']],
    ['(.*) help (.*)', ['Sure, I would be happy to help you. How can I assist you?']],
    ['(.*) your favorite color?', ['My favorite color is blue.']],
    ['(.*) thank you (.*)', ['My pleasure!', 'No problem.']],
    ['bye', ['Goodbye!', 'Have a nice day.']],
    ['can you suggest me a song?', ['Blank space by Taylor swift ', 'Money by Lisa', 'Lemonade by Diljit Dosanj']],

]

chatbot = Chat(pairs, reflections)
chatbot.converse()


# Define a function to generate a response to user input
def respond(user_input):
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    return "I'm sorry, I don't understand what you're saying."


# Start the chatbot
while True:
    user_input = input("You: ")
    print("YOU: ", respond(user_input))