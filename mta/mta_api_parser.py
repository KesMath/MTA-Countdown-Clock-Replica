import sys
import requests
import datetime
from mta.tokenauth import TokenAuth
from util.os_func import PROJECT_DIR
from configparser import ConfigParser
from realtime_feed_urls import get_url
from util.cryptographic_func import decrypt
from config.gtfs_class_parsers import FEED_MESSAGE


gtfs_parser = FEED_MESSAGE.get("class")
parser = ConfigParser()
parser.read(PROJECT_DIR + '/config/mta_config.ini')
cipher_key = parser.get('keys', 'API_KEY')
API_KEY = decrypt(cipher_key)
API_KEY = API_KEY.decode("utf-8")

class MTARealTimeFeedParser:
    '''
    class that pulls in real time data feeds from the Metropolitan Transportation Authority
    based in New York City. The feed that request.get() returns is serialized
    (object converted into a binary stream for efficient data transmission across MTA network).
    Thus, Google's gtfs_realtime_pb2 in essential for conversion of this binary into readable format
    '''

    def __init__(self, route_id):
        self.__mta_trains,\
        self.__feed_timestamp,\
        self.__gtfs_realtime_version = self.connect(route_id)

    def connect(self, route_id):
        real_time_feed_link = get_url(route_id)
        try:
            bytes_response = requests.get(url=real_time_feed_link, auth=TokenAuth(API_KEY))
        except requests.RequestException as e:
            print("Cannot connect to URL: " + real_time_feed_link + "\n" + e.__str__())
            sys.exit(1)

        if bytes_response.status_code != 200:
            raise requests.exceptions.HTTPError("HTTP Error Occurred: " + str(bytes_response.status_code))

        gtfs_parser.ParseFromString(bytes_response.content)

        return ([entity for entity in gtfs_parser.entity],
                gtfs_parser.header.timestamp,
                gtfs_parser.header.gtfs_realtime_version)

    def get_mta_trains(self):
        return self.__mta_trains

    def get_train_count(self):
        return len(self.__mta_trains)

    def get_mta_train(self, train_id):
        train_length = len(self.__mta_trains)
        if train_id >= 0:
            if train_id <= train_length-1:
                return self.__mta_trains[train_id-1]
        else:
            raise IndexError("Select a train ID less than or equal to " + str(train_length))

    def get_feed_timestamp(self):
        return "No Feed Timestamp" if self.__feed_timestamp == 0 \
            else self.__convert_timestamp_to_datetime(self.__feed_timestamp)

    def __convert_timestamp_to_datetime(self, timestamp):
        return datetime.datetime.fromtimestamp(
                int(timestamp)
                ).strftime('%m-%d-%Y %H:%M:%S')

    def get_realtime_version(self):
        return self.__gtfs_realtime_version

    '''
    iterate through list of feedEntity objects and find which train id corresponds to subway line number
    there's a static mta webpage that has the conversions... Assuming that this page does not change, the 
    (id -> subway line number) can be hardcoded 
    '''

    #def get_subway_line(self, subway_line_number):


def main():
    #TODO: api feed can return multiple route_id's (meaning a series of subsequent trains)
    # first step in parsing should be to fetch all trains (by route_id) and store them in a queue structure

    mta_object = MTARealTimeFeedParser("2")

    print("MTA Trains: " + str(mta_object.get_train_count()))
    print("Time Feed was Pulled from MTA Server: " + mta_object.get_feed_timestamp())
    print("Feed Version: " + mta_object.get_realtime_version())

    feed_entity_object = mta_object.get_mta_trains()
    print(feed_entity_object)


if __name__ == '__main__':
    main()