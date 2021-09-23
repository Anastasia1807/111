import time
current_time_millis = round(time.time()*1000)
print("Current time in milliseconds",current_time_millis)

h = 1000*60*60*24
m = 1000*60*60

days = current_time_millis//h
hour = (current_time_millis%h)//m
minutes = (current_time_millis%h)%m//(1000*60)
seconds = (current_time_millis%h)%m%(1000*60)//1000

print("Time ", days,":",hour,":",minutes,":",seconds)
