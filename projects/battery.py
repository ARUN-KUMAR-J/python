import psutil
battery=psutil.sensors_battery()
print("Battery Percentage:",battery.percent)
print("Power plugged:",battery.power_plugged)
