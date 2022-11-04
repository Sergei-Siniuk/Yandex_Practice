amount_stations, work_stations, home_stations = map(int, input().split(" "))
clockwise = abs(work_stations - home_stations) - 1
counter_clockwise = amount_stations - clockwise - 2
print(min(counter_clockwise, clockwise))
