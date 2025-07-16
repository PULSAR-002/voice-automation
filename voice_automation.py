import tkinter as tk
import pyautogui as pg
import speech_recognition as sr
import keyboard as k

class speech:
    def recognize(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:

            recognizer.adjust_for_ambient_noise(source)

            while True:
                # Check for 'q' key press before listening
                if k.is_pressed('q'):
                    print("Recording stopped.")
                    break

                try:

                    audio = recognizer.listen(source, timeout=5)
                    text = recognizer.recognize_google(audio)
                    return text

                except sr.UnknownValueError:
                    print("Sorry, I couldn't understand that.")
                except sr.RequestError:
                    print("Sorry, I'm unable to connect to the speech recognition service.")

    def action(self, a):
        print("As you wish sir")
        pg.press('win')
        pg.sleep(1)
        pg.write('chrome')
        pg.sleep(1)
        pg.press('enter')
        pg.sleep(1)
        pg.write(a)
        pg.sleep(1)
        pg.press('enter')

    def __init__(self):
        r = self.recognize()
        l2.config(text=f'You said: {r}')
        self.action(r)


def clicked():
    automation=speech()



root=tk.Tk()
root.geometry("600x300")
root.title("Search the Web")
root.config(bg="cyan")
l1=tk.Label(root, text="Press the Button below and speak and press 'q' to exit the listener", bg="cyan")
l1.pack()
btn1=tk.Button(root, text="Listen", command=clicked)
btn1.pack()
l2=tk.Label(root, text="you said : ", bg="cyan")
l2.pack()






root.mainloop()