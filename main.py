from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition 
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
import requests
import json
  


class StartScreen(Screen):
	def register(self):
		Name_of_city = self.ids.city_name.text
		close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
		api_key = "d17d6281bd1ecf9e531e851b7edbc43d"
		base_url = "http://api.openweathermap.org/data/2.5/weather?"
		city_name = Name_of_city
		complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
		response = requests.get(complete_url) 
		x = response.json() 
		if x["cod"] != "404": 
			y = x["main"] 
			current_temperature = round(int(y["temp"]) - 273.15,1)
			current_pressure = y["pressure"] 
			current_humidiy = y["humidity"] 
		  
			z = x["weather"] 
			Buttons = [close_button]
			weather_description = z[0]["description"] 
			titleA = f"Todays Weather in {city_name}"
			weather_display = f"Temperature  {current_temperature}°C\n\nHumidity  {current_humidiy}\n\n{weather_description}"
			self.dialog = MDDialog(title = f"{titleA}", text= f"{weather_display}", size_hint=(0.95,1),
			buttons = Buttons,
			)
			self.dialog.open()	
		else:
			Buttons = [close_button]
			close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
			self.dialog = MDDialog(title = f"Error", text= f"Please Recheck Your Entry", size_hint=(0.95,1),
			buttons = Buttons,
			)
			
	def close_dialog(self, obj):
		self.dialog.dismiss()	

		 
class MainApp(MDApp):

	def build(self):
		presentation = Builder.load_file("main.kv")
		return presentation
	
MainApp().run()