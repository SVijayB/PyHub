import pyperclip

pyperclip.copy("Hello world!")
text = pyperclip.paste()
print(text)

pyperclip.copy('original text')
text = pyperclip.waitForNewPaste()
print(text)
