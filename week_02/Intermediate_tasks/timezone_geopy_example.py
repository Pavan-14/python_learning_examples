import requests
import json
# pip install timezonefinder
from timezonefinder import TimezoneFinder
# pip install geopy
from geopy.geocoders import Nominatim
# import tkinter
from tkinter import *



# tkinter display details
app_window = Tk()
app_window.title("weather App")
app_window.geometry("800x400+200+100")
app_window.config(bg="skyblue")
app_window.resizable(False,False)

# application icon
app_icon = PhotoImage(file = r"C:\Users\Adapala\OneDrive\Pictures\Saved Pictures\weathericon.png")
app_window.iconphoto(False,app_icon)

# enter a city
# city = input("enter a city name: ")
# get city information
def location_info():
    city = city_name.get()
    latitude,longitude = get_LatLong(city)
    call_weather_api(latitude,longitude)
    # deleting the location after execution and try anthoer time
    city_entry.delete(0,END)

# initialize Nominatim API
# user_agent is user application name. in my case i am using "openweathermap.org" to get weather details.
geolocator = Nominatim(user_agent="openweathermap")

# finding the Latitude and Longitude using the geopy
def get_LatLong(city):
    try:
        location_details = geolocator.geocode(city)
        # print location details
        address = location_details.address
        print(address)
        latitude = location_details.latitude
        longitude = location_details.longitude

        # get the time_zone using the latitude and longitude
        # create timezonefinder instance
        object = TimezoneFinder()

        result = object.timezone_at(lat=latitude,lng=longitude)
        print("TimeZone: ",result) 
        return latitude,longitude      
    except:
        print("enter city not existed")

# create an API request object for openweathermap
def call_weather_api(latitude,longitude):
    API_key = "f51a91fe4d20b204ba8619fe4b1415f3"
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_key}&units=metric&lang=en")
        data = json.loads(response.text)
        print(data)

        # append the weather deatils to paticular label
        place_label.config(text="Location: "+data['name'])
        temperature_label.config(text="Temp: "+str(round(data['main']['temp']))+" oC")
        weather_label.config(text="Description: "+data['weather'][0]['description'])

        real_feel_label.config(text="Feels Like: "+str(round(data['main']['feels_like']))+" oC")
        pressure_label.config(text="Pressure: "+str(data['main']['pressure'])+" mbar")
        humidity_label.config(text="Humidity: "+str(data['main']['humidity'])+" %")
        visibility_label.config(text="Visibility: "+str(data['visibility']))
        wind_speed_label.config(text="Wind Speed: "+str(round(data['wind']['speed']*3.6))+"Km/h")
    except:
        print("api not avaialable")

# create a frame
input_frame = Frame(app_window,bg="skyblue")
input_frame.pack(side=TOP,padx=10,pady=10)

# create a label
city_label = Label(input_frame,text="Enter Location",bg="skyblue")
city_label.pack(side=LEFT,padx=5)

# create a variable and entry widget
# variable
city_name = StringVar()
# enter widget
city_entry = Entry(input_frame,textvariable=city_name,width="30")
city_entry.pack(side=LEFT,padx=5)


# create a search button
search_button = Button(input_frame ,text="Search",fg="green",bg="grey",font="12",width="10",height="1",relief=RAISED,command=location_info)
search_button.pack(side=LEFT,padx=5)

# create result Frame
result_frame = Frame(app_window,width=800,height=200,bg='Black')
result_frame.pack()

# create labels to show weather details
place_label = Label(result_frame ,text="Place",bg="black",fg="white")
place_label.pack(pady=2)

temperature_label = Label(result_frame ,text="Temperature",bg="black",fg="white")
temperature_label.pack(pady=2)

weather_label = Label(result_frame ,text="Description",bg="black",fg="white")
weather_label.pack(pady=2)

real_feel_label = Label(result_frame ,text="Feels Like",bg="black",fg="white")
real_feel_label.pack(pady=2)

pressure_label = Label(result_frame ,text="Pressure",bg="black",fg="white")
pressure_label.pack(pady=2)

humidity_label = Label(result_frame ,text="Humidity",bg="black",fg="white")
humidity_label.pack(pady=2)

visibility_label = Label(result_frame,text="Visiblity",bg="black",fg="white")
visibility_label.pack(pady=2)

wind_speed_label = Label(result_frame ,text="Wind Speed",bg="black",fg="white")
wind_speed_label.pack(pady=2)

app_window.mainloop()