# curing
Used to power curing fridge with raspberry pi + 4-channel 5V relay 

Heavily inspired by PorkPi on github : https://github.com/hjbct44/PorkPi
 
This repo uses a sqlite database on disk to handle the readings from the sensors and to hold all of the settings and statistics that will be mined. The purpose is to be able to not be connected to a nnetwork and still function so there is the reason for a local db. There are a few helping scripts in the repository to facilitate the creation of the database and the management of it as well. 

Scripts in .sh-files will run via crontab 

Fridge used is a Whirlpool, half size with freezer on top.

Sensor is DHT-22 

Humidifier TBA

Fan TBA
