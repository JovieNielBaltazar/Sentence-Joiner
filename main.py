

def sentence_prepper(phrase):
    interogatives = ("how", "where", "when", "where", "who")
    capitalized = phrase.capitalize()
    if phrase.startswith(interogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

sentence = []
final_sentence = ""

while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        sentence.append(sentence_prepper(user_input))

print(" ".join(sentence))