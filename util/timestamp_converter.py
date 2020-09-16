import datetime

def convert_timestamp_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(
        int(timestamp)
    ).strftime('%m-%d-%Y %H:%M:%S')


if __name__ == '__main__':
    timestamps = [
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        ''
    ]
    for time in timestamps: print(convert_timestamp_to_datetime(time))


