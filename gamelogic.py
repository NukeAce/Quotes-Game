from csv import DictReader
from random import choice


with open("quote_db.csv", encoding="utf-8") as file:
    csv_reader = DictReader(file)
    quiz = choice(list(csv_reader))
    # answer, question, hint_list = quiz["Author"], quiz["Quote"],quiz["bio"].replace
    ans = quiz["Author"]
    quote = quiz["Quote"]
    bio = quiz["Bio"]
    initials = ["J.K", "C.S", "Dr.", "J.D",
                "Ph.D.", "Inc.", "St.", "W.C", "U.S"]
    author_names = ans.replace(".", "").split(" ")
    for initial in initials:
        if f"{author_names[0][0]}.{author_names[0][1]}" == initial:
            bio = bio.replace(initial, author_names[0])
        elif f"{author_names[0]}." == initial:
            bio = bio.replace(initial, author_names[0])
        elif "Ph.D." == initial:
            bio = bio.replace(initial, "PhD")
        elif "U.S" == initial:
            bio = bio.replace(initial, "PhD")
        else:
            bio = bio.replace(
                initial, initial[:-1]).replace("Harry Potter", "").replace("CLIVE STAPLES LEWIS", "______")

    for author in author_names:
        bio = bio.replace(author, "_"*len(author))

    bio = bio.strip(" \n").split(".", 4)[:4]

    # print(quiz["Bio"].replace(ans, "_"*len(ans)).strip(" \n").split(".", 2e))
