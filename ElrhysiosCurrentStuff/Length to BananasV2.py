BananaLengthMetres = 0.178 
BananaLengthFeet = 0.58
BananaLengthCM = 18
BananaLengthInch = 7
BananaLengthMiles = 0.000110

while True:
    try:
        distance_unit = input("What unit? [cm/inch/feet/metres/mile] ").lower()
        Distance = int(input("How long of a distance? "))
        if distance_unit == "metres":
            print(round(Distance / BananaLengthMetres))

        elif distance_unit == "feet":
            print(round(Distance / BananaLengthFeet,"(Rounded)"))

        elif distance_unit == "inch":
            print(round(Distance / BananaLengthInch))

        elif distance_unit == "cm":
            print(round(Distance / BananaLengthCM))

        elif distance_unit == "mile":
            print(round(Distance / BananaLengthMiles))

    except ValueError:
        print("Input a distance plz")
