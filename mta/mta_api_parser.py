import sys
import requests
from mta.tokenauth import TokenAuth
from config.stops_dict import STOPS
from util.os_func import PROJECT_DIR
from configparser import ConfigParser
from util import timestamp_converter
from realtime_feed_urls import get_url
from util.cryptographic_func import decrypt
from config.gtfs_class_parsers import FEED_MESSAGE
from google.protobuf.json_format import MessageToDict

gtfs_parser = FEED_MESSAGE.get("class")
parser = ConfigParser()
parser.read(PROJECT_DIR + '/config/mta_config.ini')
cipher_key = parser.get('keys', 'API_KEY')
API_KEY = decrypt(cipher_key).decode("utf-8")


class MTARealTimeFeedParser:
    '''
    class that pulls in real time data feeds from the Metropolitan Transportation Authority
    based in New York City. The feed that request.get() returns is serialized
    (object converted into a binary stream for efficient data transmission across MTA network).
    Thus, Google's gtfs_realtime_pb2 in essential for conversion of this binary into readable format
    '''

    def __init__(self, route_id, stop_id):
        #TODO: add refresh_rate params
        if stop_id not in STOPS.keys():
            raise KeyError(stop_id + " is not a valid stop_id!")
        self.__mta_trains,\
        self.__feed_timestamp,\
        self.__gtfs_realtime_version = self.__connect(route_id=route_id, stop_id=stop_id)

    def __connect(self, route_id, stop_id):
        real_time_feed_link = get_url(route_id)
        try:
            bytes_response = requests.get(url=real_time_feed_link, auth=TokenAuth(API_KEY))
        except requests.RequestException as e:
            print("Cannot connect to URL: " + real_time_feed_link + "\n" + e.__str__())
            sys.exit(1)

        if bytes_response.status_code != 200:
            raise requests.exceptions.HTTPError("HTTP Error Occurred: " + str(bytes_response.status_code))

        gtfs_parser.ParseFromString(bytes_response.content)

        return (self.__filter_train(list_of_entities=gtfs_parser.entity, stop_id=stop_id),
                gtfs_parser.header.timestamp,
                gtfs_parser.header.gtfs_realtime_version)

    def __filter_train(self, list_of_entities, stop_id):
        queue = list()
        for entity in list_of_entities:
            stops_length = entity.trip_update.stop_time_update.__len__()
            while stops_length != 0:
                stop_time_update_object = entity.trip_update.stop_time_update.pop()
                if stop_time_update_object.stop_id == stop_id:
                    queue.append((entity.trip_update.trip.route_id, MessageToDict(stop_time_update_object)))
                stops_length -= 1
        return queue

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
            else timestamp_converter.convert_timestamp_to_datetime(self.__feed_timestamp)

    def get_realtime_version(self):
        return self.__gtfs_realtime_version

def main():
    mta_object = MTARealTimeFeedParser(route_id="2", stop_id="247N")

    print("MTA Trains: " + str(mta_object.get_train_count()))
    print("Time Feed was Pulled from MTA Server: " + mta_object.get_feed_timestamp())
    print("Feed Version: " + mta_object.get_realtime_version())
    print(mta_object.get_mta_trains())
    #NOTE: can create some dictionary mapping route_id -> image so it can be displayed on PI
    print(mta_object.get_mta_train(1)[1].get('departure').get('time'))



if __name__ == '__main__':
    main()