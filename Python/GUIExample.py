from time import sleep
from guizero import App, PushButton


def forwards():
    print ("Forward")

def backwards():
    print ("Backward")

app = App("Buggy controller")

drive = PushButton(app, forwards, text="Forwards")
reverse = PushButton(app, backwards, text="Reverse")

app.display()
