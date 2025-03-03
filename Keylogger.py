from pynput.keyboard import Key, Listener

def show(key):

    cleaned_key = str(key).strip("'")
    if cleaned_key == "Key.space":
        cleaned_key = " "
    elif cleaned_key == "Key.enter":
        cleaned_key = "\n"
    elif cleaned_key == "Key.tab":
        cleaned_key = "\t"
    elif cleaned_key == "Key.backspace":
        cleaned_key = ''


    print(cleaned_key, end='')

with Listener(on_press = show) as listener:
    listener.join()

