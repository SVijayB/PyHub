import html2text

h = html2text.HTML2Text()
html_string = "<p>Hello there, I am <a href='https://github.com/SVijayB'>Vijay</a>!</p>"
result = h.handle(html_string)
print(result)
