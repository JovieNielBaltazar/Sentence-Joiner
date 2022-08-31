wh_questions = ["who", "where", "when", "how"]
sentence = "who are you"

for x in wh_questions:
    print(x)
    if x in sentence():
        print("yes")