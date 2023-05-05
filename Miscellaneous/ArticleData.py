import re
import keyboard  # install keyboard module using pip

# Example string
example_string = """
"""


# Define a function to paste the extracted text when a key is pressed
def paste_text(extracted_text):
    for value in extracted_text:
        keyboard.write(value)
        keyboard.press_and_release("enter")


def title_extraction():
    # Extract text between ")" and ":"
    extracted_text = re.findall(r"\)(.*?)\:", example_string)
    keyboard.add_hotkey("p", paste_text(extracted_text))


def word_extraction():
    pattern = r":\s*(.*?)\s*words"
    result = re.findall(pattern, example_string)
    return result


def paste_words(extracted_text):
    for value in extracted_text:
        keyboard.write(value + " words.")
        keyboard.press_and_release("enter")


paste_words(word_extraction())
