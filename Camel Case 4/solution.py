def un(s):
    s1 = ""
    s2 = ""
    for ele in list(s):
        if ele.isupper():
            index = s.index(ele)
            s1 = s[0:index]
            letters = list(s[index:])
            letters[0] = letters[0].lower()
            s2 = un("".join(letters))
            return f"{s1} {s2}"
    return s


switch = True
while switch:
    try:
        s = input("").replace("\r", "").split(";")

        if s[0] == "C":
            words = s[2].split(" ")
            first_done = False
            for word in words:
                if first_done:
                    words[words.index(word)] = word.capitalize()
                else:
                    first_done = True
            if s[1] == "M":
                word = "".join(words)
                print(f"""{word}()""")
            elif s[1] == "V":
                print("".join(words))
            elif s[1] == "C":
                words[0] = words[0].capitalize()
                print("".join(words))

        if s[0] == "S":
            word = s[2]
            if s[1] == "M":
                word = word[0:-2]
            elif s[1] == "C":
                letters = list(word)
                letters[0] = letters[0].lower()
                word = "".join(letters)

            print(un(word))
    except:
        switch = False
