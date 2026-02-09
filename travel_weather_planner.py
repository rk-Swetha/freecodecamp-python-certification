# Build a Travel Weather Planner - Lab

distance_mi = 19
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)

elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)

elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

else:
    if has_ride_share_app or has_car:
        print(True)
    else:
        print(False)
