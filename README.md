**Repository for developement of the Weather App.**

Main language: Python 3.6

GUI created using: tkinter v. 8.6.

Internet communication library: requests v. 2.13.0.

`Goal: To create a visual representation of a weather report obtained via Open Weather API. `

The APIs used for this project:
 
https://openweathermap.org/api - weather data

Please obtain your unique API key at:
https://home.openweathermap.org/users/sign_up

http://api.geonames.org/timezone - time zone from geolocation service

Please register your unique user name at:
www.geonames.org/login


I created this simple application to apply in practice knowledge gained in the past months of learning Python 3 and give myself a challenge and coding exercise which does not end after writing one algorithm.

The aim of refactoring the original "all in one file" approach is to learn to isolate main parts of the application from each other to allow for developing more complicated structures in the future without tying up the components to each other unnecessarily.

During the development I have found out that due to the construction of the tkinter library it is necessary to provide the root Tk() object not only for the View which will use it for drawing of its widgets but also for the Controller which requires it to create tkinter special variables like StringVar etc.

Since there can be only one active Tk() object at any time we launch our View class first which inherits from this object and then create Controller object inside the view class.

Still the View is not aware in any way of the Model and vice versa.

Architecture which I will try to implement: Model-View-Adapter (Mediating-Controller).

Due to that some naming conventions have to be established and kept at all times to allow us to quickly, at a glance be able to get the meaning of the call without digging deep into the code.


Naming convention for actions which will be passed between the View - Controller and Model:
    
    View:
        begin_action()
        
    Controller:
        action()
        
    Model:
        finish_action()

For example to obtain a weather report after user presses the search button:

    View:
        begin_get_report()
        
    Controller:
        get_report()
    
    Model:
        finish_get_report()

Data structure obtained from the API and stored in memory in
finish_get_report: 

    status (tuple): (error_status, [weather_dicts])

    weather_dicts: {
                    "metric": [{w_d_cur}, {w_d_short}, {w_d_long}]
                    "imperial": [{w_d_cur}, {w_d_short}, {w_d_long}]
                   } 
      
If you wish you can use the debug option by enabling it in the controller
attributes (switch self.debug to 1). This will load data saved in Debug
folder instead of contacting the API for it. Still you have to make at least
one call to have the data in the first place.

To help placing objects on the canvas one can enable drawing alignment lines
on the canvas. Switch self.draw_lines to 1 in the controller attributes.
The vertical / horizontal lines have to be turned on / off by commenting
code in gui (look for self.controller.draw_lines ==).