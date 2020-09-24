import datetime

def convert_timestamp_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(
        int(timestamp)
    ).strftime('%m-%d-%Y %H:%M:%S')

def compute_relative_time(timestamp):
    """subtracts current timestamp from param timestamp and converts value into minutes"""

    #FIXME: casting is causing precision lost.. need to implement floor / ceil function for better time accuracy!
    return int((timestamp - datetime.datetime.now().timestamp())/60) \
                            if timestamp > datetime.datetime.now().timestamp() else -1

