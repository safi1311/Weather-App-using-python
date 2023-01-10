from tkinter import*
from tkinter import ttk  #for combobox

import requests  #module for use API
def data_get():
    city = city_name.get()  #geting the selcted city name
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=5ec3304b3ee7e4b92acfaa668a3c0ca8").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))  #kelvin to celcius
    p_label1.config(text=data["main"]["pressure"])

#making window
win=Tk()
win.title("Weather APP")
win.config(bg= "orange")
win.geometry("500x550")
name_label =Label(win, text="Weather App",
                  font=("Time New Roman",35,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
#making combobox
list_name=["Dhaka","Chittagong","Rajshahi","Barisal","Khulna","Rangpur","Sylhet"]
com = ttk.Combobox(win, text="Weather App",values=list_name,
                  font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

#label for climate
w_label =Label(win, text="Weather Climate",
                  font=("Time New Roman",18,))
w_label.place(x=25,y=260,height=50,width=220)
w_label1 =Label(win, text="",
                  font=("Time New Roman",18,))
w_label1.place(x=250,y=260,height=50,width=220)

#label for weather description
wd_label =Label(win, text="Weather Description",
                  font=("Time New Roman",18,))
wd_label.place(x=25,y=330,height=50,width=220)
wd_label1 =Label(win, text="",
                  font=("Time New Roman",18,))
wd_label1.place(x=250,y=330,height=50,width=220)

#label for temperature
temp_label =Label(win, text="Temperature",
                  font=("Time New Roman",18,))
temp_label.place(x=25,y=400,height=50,width=220)
temp_label1 =Label(win, text="",
                  font=("Time New Roman",18,))
temp_label1.place(x=250,y=400,height=50,width=220)

#label for pressure
p_label =Label(win, text="pressure",
                  font=("Time New Roman",18,))
p_label.place(x=25,y=470,height=50,width=220)
p_label1 =Label(win, text="",
                  font=("Time New Roman",18,))
p_label1.place(x=250,y=470,height=50,width=220)

#making button
done_button= Button(win, text="Done",
                  font=("Time New Roman",20,"bold"),command=data_get)  #function calling
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop()