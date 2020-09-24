import datetime

def convert_timestamp_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(
        int(timestamp)
    ).strftime('%m-%d-%Y %H:%M:%S')

def compute_relative_time(timestamp):
    """subtracts current timestamp from param timestamp and converts value into minutes"""
    return int((timestamp - datetime.datetime.now().timestamp())/60) \
                            if timestamp > datetime.datetime.now().timestamp() else -1

