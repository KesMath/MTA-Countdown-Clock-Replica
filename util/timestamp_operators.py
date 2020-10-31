import math
import datetime
from util.config_parser import get_config_value

SEC_TO_MINUTE = 60
ROUNDING_THRESHOLD = float(get_config_value("timing", "ROUNDING_THRESHOLD"))

def convert_timestamp_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(
        int(timestamp)
    ).strftime('%m-%d-%Y %H:%M:%S')

#TODO: assure timestamp is within the domain of EST!
def compute_relative_time(timestamp):
    """subtracts current timestamp from param timestamp and converts value into minutes.
    performs necessary minute rounding (i.e. rounds up if remainder >= 0.5 else rounds down)"""

    #NOTE: uncomment code to perform minute analysis to assure rounding accuracy
    #if timestamp > datetime.datetime.now().timestamp():
        #print((timestamp - datetime.datetime.now().timestamp())/SEC_TO_MINUTE)

    #TODO: cache datetime.now() reference for better runtime (at the cost of slightly less accurate time)
    # or just compute at each line (at the cost of slower runtime but accurate timing)

    if timestamp > datetime.datetime.now().timestamp():
        if ((timestamp - datetime.datetime.now().timestamp())/SEC_TO_MINUTE) - \
                int(((timestamp - datetime.datetime.now().timestamp())/SEC_TO_MINUTE)) < ROUNDING_THRESHOLD:
            return math.floor(((timestamp - datetime.datetime.now().timestamp())/SEC_TO_MINUTE))
        else:
            return math.ceil(((timestamp - datetime.datetime.now().timestamp())/SEC_TO_MINUTE))
    else:
        return -1