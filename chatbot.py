import numpy
import random
import re
import time

#created a list to select one of the answers given 
responses = {
    "your name?": [
        "my name is TutkuBot",
        "they call me TutkuBot",
        "the name's Bot, Tutku Bot"
    ], 
    "hello": [
        "Hello!",
        "Good to see you again!",
        "Hi there, how can I help? :)"
    ],
    "goodbye": [
        "Goodbye! ^.^",
        "Take care! :)",
        "Have a good day! :)",
        "I will miss you :(",
        "You will be missed here :("
    ],
    "delete": [
        "I cannot do that but you can do this from this link: www.xxx-deleteaccount.com"
    ],
    "create": [
        "To create new account you can go to this link: www.createAccount.com"
    ],
    "blocking": [
        "You can write the username of the account that you want to block."
    ],
    "No answer": [
        "I did not understand what you said!"
    ]
}

#patterns_key, patterns_pattern
patterns = {
    "your name?" : re.compile(r"what's your name|[nN]+[aA]+[mM]+[Ee]+"),
    "hello" : re.compile(r"[hH]+[Ee]+[lL]+[Oo]+|[hH]+[iI]+|[hH]+[eE]+[yY]"),
    "goodbye": re.compile(r"[gG]+[Oo]+[dD]+[bB]+[yY]+[Ee]+|[cC]+[yY]+[Aa]"),
    "delete" : re.compile(r"[dD]+[Ee]+[lL]+[Ee]+[tT]+[Ee]+|[rR]+[Ee]+[mM]+[Oo]+[vV]+[eE]"),
    "create" : re.compile(r"[cC]+|[rR]+[Ee]+[aA]+[tT]+[Ee]|[nN]+[Ee]+[Ww]"),
    "blocking" : re.compile(r"[bB]+[lL]+[Oo]+[cC]+[Kk]+[iI]+[nN]+[gG]")

}

def match(answer):
    for patterns_key, patterns_pattern in patterns.items():
        if patterns_pattern.search(answer):
            return patterns_key
    return "No answer"


def respond(answer):
    key = match(answer)
    if key in responses:
        #if key == "create" for ex
        return random.choice(responses[key])
    

# word_tokenized = word_tokenize(nameUserNamePassword)
print("Hello :)")

count=0
# program will be iterated
while 1:
    answer = input()
    #Make the chatbot more like a human I added 1second of delay like it is thinking about the answer
    time.sleep(1)
    #1st step, getting answer
    print(respond(answer))
    time.sleep(1)

    if count==0:
        print("What do you need ? :)")
        count +=1
    else:
        print("What else do you need? :)")