
def senten_maker(phrase):
    investigatives = ("who", "why", "where", "when", "how")
    new_sentence = phrase.capitalize()
    if phrase.startswith(investigatives):
        return "{}?".format(new_sentence)
    else:
        return "{}.".format(new_sentence)


final_sentence = []


while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        final_sentence.append(senten_maker(user_input))

print(" ".join(final_sentence))

