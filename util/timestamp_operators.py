import datetime
import math

def convert_timestamp_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(
        int(timestamp)
    ).strftime('%m-%d-%Y %H:%M:%S')

def compute_relative_time(timestamp):
    """subtracts current timestamp from param timestamp and converts value into minutes.
    performs necessary minute rounding (i.e. rounds up if remainder >= 0.5 else rounds down)"""

    #NOTE: uncomment code to perform minute analysis to assure rounding accuracy
    #if timestamp > datetime.datetime.now().timestamp():
        #print((timestamp - datetime.datetime.now().timestamp())/60)

    if timestamp > datetime.datetime.now().timestamp():
        if ((timestamp - datetime.datetime.now().timestamp())/60) % \
                int(((timestamp - datetime.datetime.now().timestamp())/60)) < 0.5:
            return math.floor(((timestamp - datetime.datetime.now().timestamp())/60))
        else:
            return math.ceil(((timestamp - datetime.datetime.now().timestamp())/60))
    else:
        return -1