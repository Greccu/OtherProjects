import sys
from tkinter import *
from weather import *
from PIL import ImageTk, Image
from io import BytesIO
import requests as req


def show(action):
    city = CityInput.get()
    CityInput.delete(0, 'end')
    display(city)


def display(city="auto"):
    global WeatherFrame
    data = getinfo(city)
    WeatherFrame.grid_forget()
    WeatherFrame = LabelFrame(root, padx=10, pady=10, width=360, height=600)
    WeatherFrame.configure(background="#303d55", border=0)
    if data['cod'] == '404':
        Label(WeatherFrame, text="City not found", font=("Times new roman", 16, 'bold'), fg="red",
              background="#303d55").pack()
        WeatherFrame.grid(row=1)
    else:
        Label(WeatherFrame, text=data['name'] + "📍", font=("Times new roman", 16, 'bold'), fg="white",
              background="#303d55").pack()
        WeatherFrame.grid(row=1)
        ###################
        tempFrame = Frame(WeatherFrame, padx=2, pady=2, width=400)
        tempFrame.configure(background="#303d55", border=0)
        tempFrame.pack()
        response = req.get(geticonurl(data))
        img = Image.open(BytesIO(response.content))
        imgtk = ImageTk.PhotoImage(img)
        imglbl = Label(tempFrame, image=imgtk, bg="#303d55",pady=0)
        imglbl.image = imgtk
        imglbl.grid(column=0,row=0)
        templbl = Label(tempFrame, text=(str(kelvin_to_celsius(data['main']['temp']))+"°C"),
                        font=("Times new roman", 24, 'bold'), fg="white", background="#303d55")
        templbl.grid(column = 1,row=0)
        rflbl = Label(WeatherFrame, text=("RealFeel "+str(kelvin_to_celsius(data['main']['feels_like']))+"°C"),
                        font=("Times new roman", 16, 'bold'), fg="white", background="#303d55",pady=5)
        rflbl.pack()
        ###################
        tempFrame2 = Frame(WeatherFrame, padx=2, pady=2, width=400)
        tempFrame2.configure(background="#3c4a64", border=0)
        tempFrame2.pack()
        mintemp =   Label(tempFrame2, text=("Min Temp"),
                        font=("Times new roman", 16, 'bold'), fg="white", background="#3c4a64", padx=5)
        mintemp.grid(row=0,column=0)
        mintempval = Label(tempFrame2, text=(str(kelvin_to_celsius(data['main']['temp_min'])) + "°C"),
                        font=("Times new roman", 16, 'bold'), fg="white", background="#3c4a64", padx=5)
        mintempval.grid(row=1,column=0)
        maxtemp = Label(tempFrame2, text=("Max Temp"),
                        font=("Times new roman", 16, 'bold'), fg="white", background="#3c4a64", padx=5)
        maxtemp.grid(row=0, column=1)
        maxtempval = Label(tempFrame2, text=(str(kelvin_to_celsius(data['main']['temp_max'])) + "°C"),
                           font=("Times new roman", 16, 'bold'), fg="white", background="#3c4a64", padx=5)
        maxtempval.grid(row=1, column=1)
        ###################
        tempFrame3 = Frame(WeatherFrame, padx=2, pady=2, width=400)
        tempFrame3.configure(background="#3c4a64", border=0)
        tempFrame3.pack(pady=2)
        pressure = Label(tempFrame3, text=("Pressure"),
                        font=("Times new roman", 16, 'bold'), fg="white", background="#3c4a64", padx=5)
        pressure.grid(row=0,column=0)
        pressureval = Label(tempFrame3, text=(str(data['main']['pressure']) + " mbar"),
                        font=("Times new roman", 16, 'bold'), fg="white", background="#3c4a64", padx=5)
        pressureval.grid(row=1,column=0)

        humidity = Label(tempFrame3, text=("Humidity"),
                         font=("Times new roman", 16, 'bold'), fg="white", background="#3c4a64", padx=5)
        humidity.grid(row=0,column=1)
        humidityval = Label(tempFrame3, text=(str(data['main']['humidity']) + "%"),
                            font=("Times new roman", 16, 'bold'), fg="white", background="#3c4a64", padx=5)
        humidityval.grid(row=1, column=1)

        wind = Label(tempFrame3, text=("Wind Speed"),
                         font=("Times new roman", 16, 'bold'), fg="white", background="#3c4a64", padx=5)
        wind.grid(row=0, column=2)
        windval = Label(tempFrame3, text=(str(data['wind']['speed']) + " m/s"),
                            font=("Times new roman", 16, 'bold'), fg="white", background="#3c4a64", padx=5)
        windval.grid(row=1, column=2)

# Window definition
root = Tk()
root.title("Weather")
root.geometry("400x600")
root.iconphoto(True, PhotoImage(file='icon.png'))
root.configure(background="#303d55")
# City Input div
CityInputFrame = Frame(root, padx=20, pady=10, width=360, height=100, bd=0, relief=SUNKEN)
CityInputFrame.grid_propagate(1)
CityInputFrame.configure(background="#3c4a64")
CityInputFrame.grid(row=0, rowspan=1, padx=10, pady=10)
CityInputLabel = Label(CityInputFrame, text="Enter city", font=("Times new roman", 16, 'bold'), fg="white",
                       background="#3c4a64")
CityInputLabel.grid(row=0, column=0, pady=10)
CityInput = Entry(CityInputFrame, width=35, font=16, bd=2, justify='center', bg="#303d55", fg="white")
CityInput.grid(row=1, column=0, pady=10, padx=10)
CityInput.bind("<Return>", show)

WeatherFrame = LabelFrame(root, padx=20, pady=10, width=360, height=600)
WeatherFrame.configure(background="#303d55", border=0)
WeatherFrame.grid(row=1)

display()

root.mainloop()
