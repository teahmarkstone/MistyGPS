import googlemaps
from datetime import datetime
import json
import html2text
import requests


def convert_directions(directions_output):
    directions_list = []
    for dict in directions_output['legs'][0]['steps']:
        direction = html2text.html2text(dict['html_instructions'])
        direction = direction.translate({ord('*'): None, ord('\n'): " "})
        distance = dict['distance']['text']
        directions_list.append((direction, distance))
    return directions_list


def print_directions(directions_result):
    output = convert_directions(directions_result)
    for line in output:
        print("In " + line[1] + ": " + line[0])


# def run(gmaps, current_loc):
#     running = True
#     print("Welcome to Teah's GPS!")
#     while running:
#         print("Enter your destination or 'exit' to quit:")
#         inp = input()
#         if inp == "exit":
#             running = False
#             continue
#         now = datetime.now()
#
#         inp_address = gmaps.geocode(inp)
#         if inp_address:
#             inp_latlng = (inp_address[0]['geometry']['location']['lat'], inp_address[0]['geometry']['location']['lng'])
#             directions_result = gmaps.directions(current_loc, inp_latlng, mode="walking", departure_time=now)[0]
#
#             with open(inp + '_directions.json', 'w') as f:
#                 json.dump(directions_result, f, ensure_ascii=False, indent=4)
#
#             print_directions(directions_result)
#
#         else:
#             print("Error: invalid location.")


def get_curr_location():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()['ip']
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

    # with open('currloc.json', 'w') as f:
    #     json.dump(response, f, ensure_ascii=False, indent=4)

    return (response['latitude'], response['longitude'])


def get_directions(string_location):
    KEY = 'AIzaSyCU1DnFQWrL7wnejd4OByB2z8HN17_ykrw'
    gmaps = googlemaps.Client(key=KEY)
    current_loc = gmaps.geocode("177 College Ave, Medford, MA 02155")
    current_loc = (current_loc[0]['geometry']['location']['lat'], current_loc[0]['geometry']['location']['lng'])

    now = datetime.now()

    inp_address = gmaps.geocode(string_location)
    if inp_address:
        inp_latlng = (inp_address[0]['geometry']['location']['lat'], inp_address[0]['geometry']['location']['lng'])
        directions_result = gmaps.directions(current_loc, inp_latlng, mode="walking", departure_time=now)[0]
        output = convert_directions(directions_result)
        result = []
        for line in output:
            new_line = "In " + line[1] + ": " + line[0]
            result.append(new_line)
        return result