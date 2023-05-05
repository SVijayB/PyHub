import smtplib
import time
import speech_recognition as sr
import webbrowser
import datetime

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        return voice_data


def send_email(to, subject, body):
    email = "your_email_address_here"
    password = "your_email_password_here"
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(email, to, message)
        server.quit()
        print(f"Email sent to {to}!")
    except:
        print("Sorry, something went wrong. Email was not sent.")


def respond(voice_data):
    if "hello" in voice_data:
        print("Hello, how can I help you?")
    if "what is the time" in voice_data:
        now = datetime.datetime.now()
        print("Current time is {}".format(now.strftime("%H:%M:%S")))
    if "open website" in voice_data:
        website = record_audio("What website do you want to open?")
        url = "https://www." + website + ".com/"
        webbrowser.get().open(url)
        print("Here is what I found for " + website)
    if "send email" in voice_data:
        to = record_audio("Who do you want to send an email to?")
        subject = record_audio("What is the subject of your email?")
        body = record_audio("What do you want to say?")
        send_email(to, subject, body)


time.sleep(1)
print("How can I assist you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)
