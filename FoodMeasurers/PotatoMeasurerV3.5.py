potato_length_in = 4.5
potato_length_cm = 11.43
potato_length_ft = 0.374
potato_length_yd = 0.125
potato_length_mi = 0.0000712
potato_length_km = 0.0001143
potato_length_m  = 0.1143

potato_watts = 0.00027
potato_radiation_Bq = 17

potato_weight_grams = 150
potato_weight_pounds = 0.33
potato_weight_kilos = 0.15

potato_rupture_force_newtons = 387

potato_volume_cm = 140
potato_volume_m = 0.00014 

potato_water_ml = 130

while True:
    try:
        watts_or_length = input("What would you like to measure? [watts/length/radioactivity/mass/break force/volume/water content] ").lower()

        if watts_or_length == "watts":

            watts = int(input("How many watts? "))
            print("To get",watts,"watts, you need this many potatoes:")
            print((round)(watts / potato_watts))

        elif watts_or_length == "water content":
            water = int(input("Target water? (ml) "))
            print("To get",water,"ml of water, you would need to extract the water from this many potatoes: ")
            print(round(water / potato_water_ml))

        elif watts_or_length == "radioactivity":

            radiation = int(input("How much radiation? (Bq) "))
            print((round)(radiation / potato_radiation_Bq))

        elif watts_or_length == "volume":

            volumeunit = input("What unit for you volume? [cm/m] ")
            volume = int(input("How much volume?"))

            if volumeunit == "cm":
                print(round(volume / potato_volume_cm))

            elif volumeunit == "m":
                print(round(volume / potato_volume_m))

        elif watts_or_length == "weight" or watts_or_length == "mass":

            weight_unit = input("What unit? [lb/kg/g] ").lower()
            mass = int(input("How much weight? (in your selected unit) "))

            if weight_unit == "lb":
                print(round(mass / potato_weight_kilos))

            elif weight_unit == "kg":
                print(round(mass / potato_weight_kilos))

            elif weight_unit == "grams" or weight_unit == "g":
                print(round(mass / potato_weight_grams))

        elif watts_or_length == "break force":
            newtons = int(input("How many newtons of force? "))
            print("With",newtons,"newtons, you would be able to destroy this many potatoes:")
            print(round(newtons / potato_rupture_force_newtons))

        elif watts_or_length == "length":
            measurement = input("What measurement would you like to use? [in/cm/ft/yd/mi/km/m] ").lower()

            distance = int(input("How long of a distance would you like to use? (In your selected measurement) "))

            if measurement == "in" or measurement == "inch" or measurement == "inches":
                print(distance,measurement,":")
                print(round(distance / potato_length_in))

            elif measurement == "cm" or measurement == "centimetres" or measurement == "centimeter":
                print(distance,measurement,":")
                print(round(distance /potato_length_cm))

            elif measurement == "ft" or measurement == "feet":
                print(distance,measurement,":")
                print(round(distance /potato_length_ft))

            elif measurement == "yd" or measurement == "yards" or measurement == "yard":
                print(distance,measurement,":")
                print(round(distance /potato_length_yd))

            elif measurement == "mi" or measurement == "miles" or measurement == "mile":
                print(distance,measurement,":")
                print(round(distance /potato_length_mi))

            elif measurement == "km" or measurement == "kilometres" or measurement == "kilometer":
                print(distance,measurement,":")
                print(round(distance /potato_length_km))

            elif measurement == "m" or measurement == "metres" or measurement == "metre":
                print(distance,measurement,":")
                print(round(distance / potato_length_m))

    except ValueError:
        print("Invalid input")
