import pyttsx3 as p
import os
import time
import subprocess as sp
def fun(a):
    import pyttsx3 as p
    time.sleep(2)
    p.speak(a+"Opened")
    p.speak("Hope you are satisfied \n and \n Hope ! this python program helped you!")
    print("\nThank You!")

p.speak(" Welcome to Program for opening the Os ")
print("Welcome to Program for opening the Os ")
p.speak("This Python Program can open")
p.speak(" Chrome \n  Notepad \n  Paint\n  Excel\n  Dvd Player\n Documents\n ")
print("1. Chrome\n2. Notepad\n3. Paint\n4. Excel\n5. Dvd Player \n6. Documents\n ")
p.speak("Please Enter the name of operating system which you want to open")
p = input("Enter Input As Text : ")

if (("chrome" or "Chrome") in p) or ((("chrome" or "Chrome" or "Web Browser" or "web browser") in p) and (("run" or "Run" or "RUN" or "execute" or "open" or "Open") in p)):
    os.system("chrome")
    print("Chrome Opened")
    fun("Chrome")
elif (("notepad" or "Notepad") in p) or ((("Notepad" or "notepad" or "text editor" or "Text Editor") in p) and (("run" or "Run" or "RUN" or "execute" or "open" or "Open") in p)):
    os.system("notepad")
    print("Notepad Opened")
    fun("Notepad")
elif (("paint" or "ms paint" or "Microsoft paint" or "Microsoft Paint" or "microsoft paint") in p) or ((("paint" or "ms paint" or "Microsoft paint" or "microsoft paint" or "Microsoft Paint") in p ) and (("run" or "Run" or "RUN" or "execute" or "open" or "Open") in p)):
    os.system("mspaint")
    print("Mircosoft Paint Opened")
    fun("Microsoft Paint")
elif (("excel" or "ms excel" or "Microsoft Excel" or "microsoft excel" or "Microsoft excel") in p) or ((("excel" or "ms excel" or "Microsoft Excel" or "microsoft excel" or "Microsoft excel") in p) and (("run" or "Run" or "RUN" or "execute" or "open" or "Open")in p)):
    os.system("Excel")
    print("Microsoft Excel Opened")
    fun("excel")
elif (("video player" or "dvd player" or "DVD player" or "Dvd Player" or "Dvd player") in p) or ((("video player" or "dvd player" or "DVD player" or "Dvd Player" or "Dvd player") in p) and ("run" or "Run" or "RUN" or "execute" or "open" or "Open" in p)):
    os.system("dvdplay")
    print("DVD Player Opened")
    fun("DVD player Opened")
elif (("Documents" or "documents") in p) or ((("documents" or "Documents") in p) and ("run" or "Run" or "RUN" or "execute" or "open" or "Open" in p)):
    os.system("documents")
    print("Documents Opened")
    fun("Documents")

