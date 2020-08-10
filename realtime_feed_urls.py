BASELINE_URL = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs"


FEED_URLS = {

    ('1', '2', '3', '4', '5', '6'): BASELINE_URL,
    ('A', 'C', 'E'): BASELINE_URL + "-ace",
    ('G',): BASELINE_URL + "-g",
    ('N', 'Q', 'R', 'W'): BASELINE_URL + "-nqrw",
    ('B', 'D', 'F', 'M'): BASELINE_URL + "-bdfm",
    ('J', 'Z'): BASELINE_URL + "-jz",
    ('L',): BASELINE_URL + "-l",
    ('7',): BASELINE_URL + "-7"

}

def get_url(route_id):
    for key, value in FEED_URLS.items():
        for route in key:
            if route_id is route:
                return FEED_URLS.get(key)


if __name__ == '__main__':
    print(get_url('N'))