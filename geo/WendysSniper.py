import urllib.request
import json
import math
import time

print(r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠏⢀⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⠻⣿⣿⣿⣿⡆⠹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠏⠀⢸⣿⣿⣿⣿⣿⣿⡋⣡⡾⢟⣥⣤⡝⣿⣿⣿⣧⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠀⠀⢸⣿⡟⠏⠀⣶⣶⣄⠀⠀⣠⣴⣶⡄⠘⢿⣿⡿⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠸⣿⣷⡀⢠⣩⣦⠿⠀⠀⠸⢠⣬⡇⢀⣿⣿⠇⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⣿⢴⠟⡽⣼⣿⣿⠀⠉⣄⠀⠛⣛⠁⢀⡀⠀⣿⣿⣏⡞⣻⣶⣼⡇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣿⣿⣬⣷⣷⣿⣿⣿⣷⣄⠈⠻⣭⣭⡿⠋⣀⣾⣿⣿⡿⠿⣿⣥⣿⣿⣵⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⢷⡿⣿⡋⢩⣿⠷⣄⣀⣀⣠⡾⢻⣬⢙⣟⡷⡾⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣦⡣⠿⢋⣿⣿⢿⣤⣍⢉⣥⣴⣿⣿⡈⠚⢥⣷⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣶⣄⡘⠋⣾⠏⣿⣻⡟⢿⡜⢟⣀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣶⣶⣿⣿⣷⣶⠾⠟⠋⠁⠀⠀⠀⣴⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⣴⣶⣦⠀⠀⠀⠀⣀⡀⠀⠀⠀⢸⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡆⠀⠀⠀⠀⠀
⢹⣿⣿⣿⠀⠀⢠⣾⣿⣿⠀⠀⢀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣿⣿⣿⡀⢀⣤⣤⡄⠀⠀⣠⣤⡄⣿⣿⠇⣀⣤⣤⣀⠀
⢸⣿⣿⡿⠀⠀⣾⣿⣿⣿⠀⠀⣸⣿⣿⠇⠀⣠⣴⣾⣿⣷⡄⣰⣿⣿⣟⣴⣿⣿⣧⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⢇⣿⣿⣿⠃⠀⣼⣿⣿⡇⢠⣴⣿⣿⣿⣿⣿⡆
⢸⣿⣿⡇⠀⣸⣿⣿⣿⣿⠀⢀⣿⣿⡟⠀⣼⣿⣿⠛⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⡏⠀⣴⣿⣿⡿⠋⣽⣿⣿⠁⣸⣿⣿⡏⠀⢰⣿⣿⣿⢠⣿⣿⣿⡋⠙⠿⠿⠁
⢸⣿⣿⡇⢠⣿⣿⣿⣿⣿⡆⢸⣿⣿⠇⣼⣿⣿⣁⣾⣿⡟⢸⣿⣿⣿⠟⢹⣿⣿⡇⣼⣿⣿⠏⢀⣼⣿⣿⣿⠀⣿⣿⣿⠁⢠⣿⣿⣿⡟⠈⢿⣿⣿⣿⣷⣤⡀⠀
⣾⣿⣿⡇⣼⣿⡿⢹⣿⣿⡇⣾⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⣿⣿⣿⡿⠀⢸⣿⣿⣷⣿⣿⣿⣶⣿⣿⣿⣿⣿⠀⣿⣿⣿⣷⣿⣿⣿⣿⠇⣠⣤⣌⣙⣿⣿⣿⣿⠀
⣿⣿⣿⣷⣿⣿⡇⠸⣿⣿⣷⣿⣿⡟⢻⣿⣿⣿⣁⣴⣶⡆⣿⣿⣿⠃⠀⠀⢿⣿⣿⠿⣿⣿⠿⠛⠁⢿⣿⣿⣧⠘⣿⣿⣿⠟⣿⣿⣿⠀⢿⣿⣿⣿⣿⣿⡿⢃⡀
⣿⣿⣿⣿⣿⡿⠀⠀⣿⣿⣿⣿⡿⠀⠈⢻⣿⣿⣿⣿⠟⠀⠘⠛⠋⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠁⠀⠀⠀⠀⢠⣿⣿⣿⠀⠀⠉⠛⠛⠉⠁⠀⠘⠛
⢸⣿⣿⣿⣿⡇⠀⠀⢻⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣴⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⣿⣿⣿⡿⠀⠀⠀⠀⠉⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠉⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

latitude = float(input("Latitude: "))
longitude = float(input("Longitude: "))
number_of_wendys = int(input("How many Wendy's? "))

overpass_servers = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.private.coffee/api/interpreter"
]

search_radii = [10000, 25000, 50000, 100000, 200000]

def calculate_distance(lat1, lon1, lat2, lon2):
    earth_radius = 3958.7613

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)

    latitude_difference = lat2 - lat1
    longitude_difference = math.radians(lon2 - lon1)

    a = (
        math.sin(latitude_difference / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(longitude_difference / 2) ** 2
    )

    return 2 * earth_radius * math.asin(math.sqrt(a))


def get_coordinates(place):
    if "lat" in place and "lon" in place:
        return place["lat"], place["lon"]

    center = place.get("center")

    if center:
        return center.get("lat"), center.get("lon")

    return None, None


def get_address(tags):
    address_parts = [
        tags.get("addr:housenumber"),
        tags.get("addr:street"),
        tags.get("addr:city"),
        tags.get("addr:state"),
        tags.get("addr:postcode")
    ]

    address = " ".join(part for part in address_parts if part)

    return address if address else "Address not listed"


wendys_locations = []
seen_locations = set()

for radius in search_radii:
    query = f"""
    [out:json][timeout:60];
    (
        nwr(around:{radius},{latitude},{longitude})["name"="Wendy's"];
        nwr(around:{radius},{latitude},{longitude})["name"="Wendys"];
        nwr(around:{radius},{latitude},{longitude})["brand"="Wendy's"];
        nwr(around:{radius},{latitude},{longitude})["brand"="Wendys"];
    );
    out center tags;
    """

    found_data = False

    for server in overpass_servers:
        try:
            request = urllib.request.Request(
                server,
                data=query.encode("utf-8"),
                headers={
                    "User-Agent": "WendysLocator/1.0"
                }
            )

            with urllib.request.urlopen(request, timeout=70) as response:
                data = json.load(response)

            found_data = True
            break

        except Exception as error:
            print(f"Server failed: {server}")
            print(error)
            time.sleep(1)

    if not found_data:
        continue

    for place in data.get("elements", []):
        wendy_latitude, wendy_longitude = get_coordinates(place)

        if wendy_latitude is None or wendy_longitude is None:
            continue

        location_key = (
            round(wendy_latitude, 5),
            round(wendy_longitude, 5)
        )

        if location_key in seen_locations:
            continue

        seen_locations.add(location_key)

        tags = place.get("tags", {})

        distance = calculate_distance(
            latitude,
            longitude,
            wendy_latitude,
            wendy_longitude
        )

        address = get_address(tags)

        wendys_locations.append({
            "distance": distance,
            "address": address,
            "latitude": wendy_latitude,
            "longitude": wendy_longitude
        })

    if len(wendys_locations) >= number_of_wendys:
        break


wendys_locations.sort(key=lambda location: location["distance"])

print()

if not wendys_locations:
    print("No Wendy's locations were found.")
else:
    for index, location in enumerate(
        wendys_locations[:number_of_wendys],
        start=1
    ):
        print(
            f"{index}. {location['address']} "
            f"— {location['distance']:.2f} miles "
            f"({location['latitude']}, {location['longitude']})"
        )
