import datetime
import math

SEC_TO_MINUTE = 60

'''NOTE: may need to adjust rounding threshold for departure/ arrival times!
   'common rounding technique' may be too optimistic and it's best to err on side of pessimism!  
   
   EXAMPLE: If you are rushing to make the train and time is 2.5 til departure,
   would you rather api round down to 2 minutes so you can rush and make it versus rounding up to 
   3 minutes so you can think you have more time then you have in actuality?
   In this case we have a bias for the lowest integer.
   
   EXAMPLE: If you are waiting for a train arrival and time is 2.5 til arrival,
   would you rather the api round down to 2 minutes so you can be over-optimistic
   and have a false sense of hope versus rounding up to 3 minutes to avoid disappointment and
   provide more room for possible delays. In this case we have a bias for the highest integer.
   
   FYI: this is not critical in the grand scheme of timing as (+ or -) 1 minute is not a major difference.
   The rounding threshold just adjusts INTEGER BIAS when rounding up or rounding down
   
'''
ROUNDING_THRESHOLD = 0.5

def convert_timestamp_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(
        int(timestamp)
    ).strftime('%m-%d-%Y %H:%M:%S')

def compute_relative_time(timestamp):
    """subtracts current timestamp from param timestamp and converts value into minutes.
    performs necessary minute rounding (i.e. rounds up if remainder >= 0.5 else rounds down)"""

    #NOTE: uncomment code to perform minute analysis to assure rounding accuracy
    if timestamp > datetime.datetime.now().timestamp():
        print((timestamp - datetime.datetime.now().timestamp())/SEC_TO_MINUTE)

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