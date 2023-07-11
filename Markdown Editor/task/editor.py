
formatters = ["plain", "bold", "italic", "header",
              "link", "inline-code", "ordered-list", "unordered-list", "new-line"]
special_commands = ["!help", "!done"]
user_in = ""

def header():
    level_ok = False
    while not level_ok:
        level = input("Level:")
        try:
            level_int = int(level)
            if (level_int <= 6) & (level_int > 0):
                level_ok = True
            else:
                print("The level should be within the range of 1 to 6")
        except [TypeError, ValueError]:
            print("The level should be within the range of 1 to 6")
    temp = input("Text:")
    return level_int * "#" + " " + temp + "\n"

def bold():
    txt = input("Text:")
    return "**" + txt + "**"

def italic():
    txt = input("Text:")
    return "*" + txt + "*"

def plain():
    txt = input("Text:")
    return txt

def inline_code():
    txt = input("Text:")
    return "`" + txt + "`"

def link():
    label = input("Label:")
    url = input("URL:")
    return "[" + label + "](" + url + ")"

def new_line():
    return "\n"


def make_list(ordered):
    rows_ok = False
    txt = ""
    while not rows_ok:
        nrows = input("Number of rows:")
        try:
            nrows_int = int(nrows)
            if nrows_int > 0:
                rows_ok = True
            else:
                print("The number of rows should be greater than zero")
        except [TypeError, ValueError]:
            print("The number of rows should be greater than zero")
    for i in range(nrows_int):
        elem = input(f'Row #{i+1}')
        if ordered:
            elem = str(i+1) + ". " + elem + "\n"
        else:
            elem = "* " + elem + "\n"
        txt = txt + elem
    return txt


def ordered_list():
    return make_list(ordered=True)


def unordered_list():
    return make_list(ordered=False)


final_txt = ""
while user_in != "!done":

    user_in = input("Choose a formatter:")
    if (user_in in formatters) | (user_in in special_commands):
        if user_in == "!help":
            print("Available formatters:", ' '.join(formatters))
            print("Special commands:", ' '.join(special_commands))
        elif user_in in formatters:
            func_name = user_in.replace("-", "_")
            func = globals()[func_name]
            final_txt = final_txt + func()
            print(final_txt)
    else:
            print("unknown formatting type or command")
file = open("output.md", "w")
file.write(final_txt)
file.close()