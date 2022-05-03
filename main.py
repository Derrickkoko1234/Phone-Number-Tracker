from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root = Tk()
root.title("Phone Number Tracker")
root.geometry("365x584+400+100")
root.resizable(False, False)

#logo
logo = PhotoImage(file="logo image.png")
Label(root, image=logo).place(x=35, y=70)

Heading = Label(root, text="TRACK NUMBER", font=("arial", 15, "bold"))
Heading.place(x=130, y=110)

#entry
Entry_back = PhotoImage(file="search png.png")
Label(root, image=Entry_back).place(x=20, y=190)

entry = StringVar()
enter_number = Entry(root, textvariable=entry, width=17, bd=0, font=('arial', 20), justify='center')
enter_number.place(x=50, y=220)

#button
Search_image = PhotoImage(file='search.png')



root.mainloop()