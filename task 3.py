import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    # Greetings
    [r"hi|hello|hey", ["Hello there!", "Hi, how can I help you today?", "Hey!"]],
    
    # Name
    [r"what is your name\??", ["I am ChatBot, your assistant!", "You can call me Chatty."]],
    [r"(.*) your name\??", ["I'm ChatBot. Nice to meet you!"]],
    
    # How are you
    [r"how are you\??", ["I'm good, thank you!", "Feeling great! How about you?"]],
    [r"I am fine|I am good", ["That's great to hear!", "Awesome!"]],
    
    # Help
    [r"(.*) help (.*)", ["Sure, I'm here to help. Tell me your problem.", "Yes, I'm happy to help."]],
    
    # Weather (dummy response)
    [r"(.*) weather(.*)", ["I can't check real weather, but I hope it's sunny!"]],
    
    # Education
    [r"what is Python\??", ["Python is a high-level programming language used for general-purpose programming."]],
    [r"what is AI\??", ["AI stands for Artificial Intelligence – it's when machines mimic human intelligence."]],
    
    # Hobbies
    [r"what are your hobbies\??", ["I like chatting with people and learning new things!"]],
    [r"do you like music\??", ["Yes, especially binary beats! 😉"]],
    
    # Time/Day
    [r"what day is it\??", ["I don't have a clock yet, but you can check your device's calendar."]],
    
    # Age
    [r"how old are you\??", ["I was born the moment you ran this program."]],
    
    # Small Talk
    [r"(.*) (love|like) (.*)", ["Love is a beautiful thing. ❤️", "Yes, I like that too!"]],
    [r"(.*) joke", ["Why did the computer get cold? Because it left its Windows open!"]],
    [r"(.*) bored", ["You can talk to me! I’ll try to make your day better."]],
    
    # Exit
    [r"quit|exit|bye", ["Goodbye!", "See you later!", "It was nice talking to you. Bye!"]],
    
    # Default fallback
    [r"(.*)", ["Sorry, I didn’t understand that. Try asking something else.", "Interesting! Can you ask differently?"]]
]

def chatbot():
    print("🤖 ChatBot: Hello! I'm ChatBot. Ask me anything. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

chatbot()
