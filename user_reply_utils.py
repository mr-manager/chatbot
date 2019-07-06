import json
import random

happy_animation =["dancing", "giggling", "laughing", "inLove"]
sad_animation = ["crying", "heartbroke", "no", "confused"]
neutral_animation = ["ok", "bored", "waiting"]

swear_jar = ['fuck', 'motherfucker', 'shit', 'shithead', 'cunt', 'ass', 'dick', 'whore', 'cock', 'pussy',
             'bitch', 'butt', 'butthole', 'poop', 'poopy', 'kaka']
swear_replies = ["Place a nickle in the swear jar, young man", "Do you kiss your mother with that mouth?",
                 "I don't respond to that kind of language",
                 "Try asking again, but with nicer words", "I don't negotiate with terrorists"]
money_keywords = ["cost", "price", "money", "bitcoin", "dollars", "shekel", "benjamins"]
question_keywords = ["who", "what", "where", "when", "why", "how",
                     "who's", "what's", "where's", "when's", "why's", "how's"]
question_replies = ["I wish I could be more helpful, sorry", "Who do you think I am, Google?",
                    "Try asking another time"]
dog_replies = ["I love puppies. Especially fluffy ones", "My favorite dog is Snoop Dogg, ya feel me?", "Woof Woof"]
joke_keywords = ["funny", "joke", "jokes"]
joke_replies = ["Tonight I dreamt of a beautiful walk on a sandy beach. " +
                "At least that explains the footprints I found in the cat litter box this morning",
                "Why did the donut visit the dentist? To get a new filling",
                "Did you know Iceland is just one sea away from Ireland?"]
sad_keywords = ["blood", "murder", "sad", "cry", "tears", "bomb", "rape", "kill", "gun", "shoot", "stab", "steal", "trump"]

def check_for_swears(input):
    if any(word in input for word in swear_jar):
        return True

def check_for_question(input):
    if any(word in input for word in question_keywords):
        return True

def check_for_money_question(input):
    if any(word in input for word in money_keywords):
        return True

def check_for_sad_words(input):
    if any(word in input for word in sad_keywords):
        return True

def tell_a_joke(input):
    if any(word in input for word in joke_keywords):
        return True

def handel_user_input(user_message):
    split_user_message = user_message.lower().split()
    if check_for_swears(split_user_message):
        return json.dumps({"animation": "afraid", "msg": swear_replies[random.randint(0, 4)]})
    elif tell_a_joke(split_user_message):
        return json.dumps({"animation": happy_animation[random.randint(0, 2)],
                           "msg": joke_replies[random.randint(0, 2)]})
    elif check_for_sad_words(split_user_message):
        return json.dumps({"animation": sad_animation[random.randint(0, 2)],
                           "msg": "Let's not talk about such sad things. Why don't you ask me for a joke?"})
    elif check_for_money_question(split_user_message):
        return json.dumps({"animation": "money", "msg": "If you have to ask, you can't afford it"})
    elif user_message.lower().find("what is love") is not -1:
        return json.dumps({"animation": sad_animation[random.randint(0, 3)],
                           "msg": "Baby, don't hurt me. Don't hurt me. No more"})
    elif user_message.lower().find("dog") is not -1:
        return json.dumps({"animation": "dog", "msg": dog_replies[random.randint(0, 2)]})
    elif check_for_question(split_user_message):
        return json.dumps({"animation": "takeoff", "msg": question_replies[random.randint(0, 2)]})
    else:
        return json.dumps({"animation": neutral_animation[random.randint(0, 2)],
                           "msg": "Not sure what you mean by than. Can you try asking again with different words"})
