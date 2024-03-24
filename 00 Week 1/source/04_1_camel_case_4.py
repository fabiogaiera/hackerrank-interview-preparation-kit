def process_line(text):
    lst_line = text.split(";")

    if lst_line[0] == 'S':  # Split

        if lst_line[1] == 'V':  # Variable

            variable = lst_line[2]
            for elem in variable:
                if elem.islower():
                    print(elem, end="")
                else:
                    print(" " + elem.lower(), end="")

        elif lst_line[1] == 'C':  # Class
            classe = lst_line[2]
            for i in range(len(classe)):
                if i != 0 and classe[i].isupper():
                    print(" " + classe[i].lower(), end="")
                elif classe[i].isupper():
                    print(classe[i].lower(), end="")
                else:
                    print(classe[i], end="")

        elif lst_line[1] == 'M':  # Method

            method = lst_line[2]
            for elem in method:
                if elem.islower():
                    print(elem, end="")
                elif elem.isupper():
                    print(" " + elem.lower(), end="")
                elif elem in ['(', ')']:
                    pass

    elif lst_line[0] == 'C':  # Combine

        lst = lst_line[2].split()

        if lst_line[1] == 'V':  # Variable
            print(lst[0], end="")
            for i in range(1, len(lst)):
                print(lst[i].capitalize(), end="")

        elif lst_line[1] == 'M':  # Method
            print(lst[0], end="")
            for i in range(1, len(lst)):
                print(lst[i].capitalize(), end="")
            print("()", end="")

        elif lst_line[1] == 'C':  # Class
            for i in range(0, len(lst)):
                print(lst[i].capitalize(), end="")

    print()


while True:
    try:
        txt = input()
        process_line(txt)

    except EOFError:
        break
