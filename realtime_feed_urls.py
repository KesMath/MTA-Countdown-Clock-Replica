BASELINE_URL = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs"

FEED_URLS = {

    "123456": BASELINE_URL,
    "ACE": BASELINE_URL + "-ace",
    "G": BASELINE_URL + "-g",
    "NQRW": BASELINE_URL + "-nqrw",
    "SIR": BASELINE_URL + "-si",
    "BDFM": BASELINE_URL + "-bdfm",
    "JZ": BASELINE_URL + "-jz",
    "L": BASELINE_URL + "-l",
    "7": BASELINE_URL + "-7"

}

#TODO: write function that given char of train, returns the corresponding url