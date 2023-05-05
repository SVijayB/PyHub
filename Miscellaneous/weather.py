import tkinter as tk


class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x200")
        self.master.title("Weather App")
        self.create_widgets()

    def create_widgets(self):
        self.location_label = tk.Label(self.master, text="Location:")
        self.location_label.grid(row=0, column=0, padx=10, pady=10)

        self.location_entry = tk.Entry(self.master)
        self.location_entry.grid(row=0, column=1, padx=10, pady=10)

        self.fetch_button = tk.Button(
            self.master, text="Fetch Weather", command=self.fetch_weather
        )
        self.fetch_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.temperature_label = tk.Label(self.master, text="")
        self.temperature_label.grid(row=2, column=0, padx=10, pady=10)

        self.status_label = tk.Label(self.master, text="")
        self.status_label.grid(row=3, column=0, padx=10, pady=10)

    def fetch_weather(self):
        location = self.location_entry.get()
        observation = owm.weather_at_place(location)
        weather = observation.get_weather()
        temperature = weather.get_temperature("celsius")["temp"]
        status = weather.get_detailed_status()
        self.temperature_label.config(text="Temperature: " + str(temperature) + " °C")
        self.status_label.config(text="Status: " + status)


root = tk.Tk()
app = WeatherApp(root)
root.mainloop()
