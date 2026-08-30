potato_length_in = 4.5
potato_length_cm = 11.43
potato_length_ft = 0.374
potato_length_yd = 0.125
potato_length_mi = 0.0000712
potato_length_km = 0.0001143
potato_length_m  = 0.1143

potato_watts = 0.00027
potato_radiation_Bq = 17

while True:
    try:
        watts_or_length = input("What would you like to measure? [watts/length/radioactivity] ").lower()

        if watts_or_length == "watts":
            watts = int(input("How many watts? "))
            print((round)(watts / potato_watts))

        elif watts_or_length == "radioactivity":
            radiation = int(input("How much radiation? (Bq) "))
            print((round)(radiation / potato_radiation_Bq))


        elif watts_or_length == "length":
            measurement = input("What measurement would you like to use? [in/cm/ft/yd/mi/km/m] ").lower()

            distance = int(input("How long of a distance would you like to use? (In your selected measurement) "))

            if measurement == "in" or measurement == "inch" or measurement == "inches":
                print(round(distance / potato_length_in))

            elif measurement == "cm" or measurement == "centimetres" or measurement == "centimeter":
                print(round(distance /potato_length_cm))

            elif measurement == "ft" or measurement == "feet":
                print(round(distance /potato_length_ft))

            elif measurement == "yd" or measurement == "yards" or measurement == "yard":
                print(round(distance /potato_length_yd))

            elif measurement == "mi" or measurement == "miles" or measurement == "mile":
                print(round(distance /potato_length_mi))

            elif measurement == "km" or measurement == "kilometres" or measurement == "kilometer":
                print(round(distance /potato_length_km))

            elif measurement == "m" or measurement == "metres" or measurement == "metre":
                print(round(distance / potato_length_m))

    except ValueError:
        print("Invalid input")
