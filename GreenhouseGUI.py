from customtkinter import *
from PIL import Image

import tkinter as tk
import webbrowser

def open_earth_engine():
    link = "https://code.earthengine.google.com/3d965797ad8b13ed80c23f66bc2f7504"
    webbrowser.open(link)

app = CTk()
app.geometry("600x480")
app.resizable(0,0)
app.title("Greenhouse Gas Emission Monitoring System")

sideimgdata = Image.open("side-img.jpg")
greenhousedata = Image.open("email-icon.png")
datedata = Image.open("date.png")
google_icon_data = Image.open("google-icon.png")

side_img = CTkImage(dark_image=sideimgdata, light_image=sideimgdata, size=(300, 480))
gicon = CTkImage(dark_image=greenhousedata, light_image=greenhousedata, size=(20,20))
dateicon = CTkImage(dark_image=datedata, light_image=datedata, size=(17,17))
google_icon = CTkImage(dark_image=google_icon_data, light_image=google_icon_data, size=(17,17))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Greenhouse Gas", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 0), padx=(25, 0))
CTkLabel(master=frame, text="Monitoring System", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", padx=(25, 0))
CTkLabel(master=frame, text="Using Google Earth Engine", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Greenhouse Gas", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=gicon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000").pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Year", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=gicon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000").pack(anchor="w", padx=(25, 0))


CTkButton(master=frame, text="Open Google Earth Engine", fg_color="#601E88", hover_color="#E44982", command=open_earth_engine, font=("Arial Bold", 12), text_color="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 0))


app.mainloop()