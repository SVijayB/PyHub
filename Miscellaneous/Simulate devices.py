from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller

mouse = Controller()
mouse.position = (50,60)
print('Current mouse position -> {0}'.format(mouse.position))
mouse.move(30,15)
mouse.press(Button.left)
mouse.release(Button.left)
mouse.press(Button.right)
mouse.release(Button.right)
mouse.click(Button.left, 2)
mouse.scroll(0,2)

keyboard = Controller()
keyboard.press('a')
keyboard.release('a')
keyboard.press(Key.space)
keyboard.release(Key.space)
keyboard.press(Key.ctrl)
keyboard.release(Key.ctrl)
keyboard.type('Hello World!!')
