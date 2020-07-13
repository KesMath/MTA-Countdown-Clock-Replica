"""
train payload collected from routes.txt and trips.txt
NOTE: add more train payloads to alter output of main class: mta_api.py
"""


TWO_TRAIN = {
    "route_id": 2,
    "agency_id": "MTA NYCT",
    "route_long_name": "7 Avenue Express",
    "route_desc": "Trains operate between Wakefield-241 St, Bronx, and Flatbush Av-Brooklyn College, Brooklyn, at all times.\
                  Trains operate local in Bronx and Brooklyn. "
                  "Trains operate express in Manhattan except late night when it operates local.",
    "route_type": 1,
    "route_url": "http://web.mta.info/nyct/service/pdf/t2cur.pdf",
    "route_color": "EE352E",
    "stop_id_north": "247N",
    "stop_id_south": "247S",
    "initial_stop": "Flatbush Av - Brooklyn College",
    "final_destination": "Wakefield-241 St",
    "stop_latitude": 40.632836,
    "stop_longitude": -73.947642,
    "parent_station": 247
}



FIVE_TRAIN = {
    "route_id": 5,
    "agency_id": "MTA NYCT",
    "route_long_name": "Lexington Avenue Express",
    "route_desc": "Weekdays daytime, most trains operate between either Dyre Av or 238 St-Nereid Av,\
                   Bronx, and Flatbush Av-Brooklyn College, Brooklyn. At all other times except during late nights,\
                   trains operate between Dyre Av, Bronx, and Bowling Green, Manhattan.\
                   During late nights trains operate only in the Bronx between Dyre Av and E 180 St/MorrisPark Av.\
                   Customers who ride during late night hours can transfer to 2 service at the E 180 St Station.\
                   At all times, trains operate express in Manhattan and Brooklyn. Weekdays, trains in the Bronx\
                   operate express from E 180 St to 149 St-3 Av during morning rush hours (from about 6 AM to 9 AM),\
                   and from 149 St-3 Av to E 180 St during the evening rush hours (from about 4 PM to 7 PM).",
    "route_type": 1,
    "route_url": "http://web.mta.info/nyct/service/pdf/t5cur.pdf",
    "route_color": "00933C"
    #TODO: need to collect missing key value pairs
}
