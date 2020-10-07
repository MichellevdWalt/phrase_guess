from .phrase import Phrase

phrases = ["break a leg", 
"when pigs fly", 
"best of both worlds", 
"see eye to eye", 
"piece of cake", 
"to cut corners", 
"call it a day", 
"bite the bullet", 
"the last straw", 
"the elephant in the room"]

def phrase_objects():
    phrase_objects = []
    for phrase in phrases:
        phrase_objects.append(Phrase(phrase))
    return phrase_objects