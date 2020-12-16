from os import system
from math import sin, pi, tau
from json import load
from time import sleep

config = {}

with open("config.json", "r") as json_file:
	config = load(json_file)

gun = []

with open(config["gunfile"], "r") as gun_file:
	gun = gun_file.read().split("\n")

offset = config["offset"]
speed = config["speed"]
amplitude = config["amplitude"]
delay = config["delay"]

current = 0
multiplier = 1

while True:
	# works only on windows
	system("cls")
	spaces = " " * (offset + current)

	for row in gun:
		print(spaces + row)

	current += speed * multiplier

	if abs(current) >= amplitude:
		multiplier *= -1

	sleep(delay / 1000)