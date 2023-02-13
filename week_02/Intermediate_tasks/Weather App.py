''' The goal of this project is to create a weather app that shows the current weather conditions and forecast for a specific location.

Here are the steps you can take to create this project:

    Use the requests library to make an API call to a weather service (e.g. OpenWeatherMap) to retrieve the weather data for a specific location.

    Use the json library to parse the JSON data returned by the API call.

    Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons and text boxes.

    Use the Pillow library to display the weather icons.

    Use the datetime library to display the current time and date. '''
# importing required modules
from tkinter import *
from tkcalendar import Calendar,DateEntry
from datetime import date,time
import requests
import json, os

# requests module
def weather_details():
    city = location.get()
    # store api key in my system environment variables
    # api_key = os.environ.get('weather_api')

    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=##########&units=metric&lang=en")
     
    data = json.loads(response.text)
    if data['cod'] == 404:
        print("enter correct city name")
            
    else:
        place = data['name']
        temperature = round(data['main']['temp'])
        weather = data['weather'][0]['description']

        real_feel = round(data['main']['feels_like'])
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        visibility = data['visibility']
        wind_speed = round(data['wind']['speed']*3.6)

        main_details = "Place: "+place + '\n' + "Temperature: "+str(temperature) +" oC"+ '\n' + "weather: "+weather 

        other_details = "feels like: "+str(real_feel)+ "oC"+ '\n' + "Pressure: "+str(pressure) + '\n' + "Humidity: "+str(humidity) + '\n' + "Visibility: "+str(visibility) + '\n' + "wind_speed: "+str(wind_speed)
        # print(main_details)
        # print(other_details)

        # added to labels
        main_label.config(text=main_details)
        details_label.config(text=other_details)
        
 


# tkinter
""" display window properties """
weather_app = Tk()
weather_app.title("Weather Forecast")
weather_app.geometry('500x500')
weather_app.config(bg="skyblue")

""" widgets """
# creates a frame for inputs
search_frame = Frame(weather_app)
search_frame.pack(side=TOP,padx=10,pady=10)


""" Location related Widgets """
# create a label to enter location
location_label = Label(search_frame,text="Enter Location",fg="black")
location_label.pack(side=LEFT,padx=3)

# create an entry point variable to enter the location
location = StringVar()
location_entry = Entry(search_frame,textvariable=location,width="40")
location_entry.pack(side=LEFT,padx=3)

""" Date related Widgets """

"""
# created a calander
date = Calendar(search_frame, selectmode="day", date_pattern="dd-mm-y")
date.pack(side=LEFT,padx=3)
"""
"""
# to show new date in label
def new_date(*args):
    date_label.config(text=date_var.get())


# create variable to store the date
date_var = StringVar()

# created a DateEntry
date_entry = DateEntry(search_frame, selectmode="day", date_pattern="dd-mm-y", textvariable=date_var)
date_entry.pack(side=LEFT,padx=3)

# trace any changes in date
date_var.trace("w",new_date)

# create label to dispaly date
date_label = Label(search_frame,bg="grey")
date_label.pack(side=LEFT,padx=3)
"""

""" Search Button Widget """
# create a button for search
search_button = Button(search_frame,text="Search",fg="green",bg="grey",font="12",width="10",height="1",relief=RAISED,command=weather_details)
search_button.pack(side=LEFT,padx=10)

# create label to weather details
main_label = Label(weather_app,bg="skyblue")
main_label.pack(padx=2,pady=15)

details_label = Label(weather_app,bg="skyblue")
details_label.pack(padx=2,pady=15)


weather_app.mainloop()
