import requests
from configparser import ConfigParser
import datetime
from config.gtfs_class_parsers import FEED_MESSAGE
from util.os_func import PROJECT_DIR
from realtime_feed_urls import get_url


gtfs_parser = FEED_MESSAGE.get("class")
parser = ConfigParser()
parser.read(PROJECT_DIR + '/config/mta_config.ini')
API_KEY = parser.get('keys', 'API_KEY')
HEADERS = {'x-api-key': API_KEY}

class MTARealTimeFeed:
    '''
    class that pulls in real time data feeds from the Metropolitan Transportation Authority
    based in New York City. The feed that request.get() ingests is serialized
    (object converted into a binary stream for efficient data transmission across MTA network).
    Thus, Google's gtfs_realtime_pb2 in essential for conversion of this binary into readable format

    Refer to http://datamine.mta.info/list-of-feeds for MTA API changes
    '''

    def __init__(self, feed_id):
        self.__mta_trains,\
        self.__feed_timestamp,\
        self.__gtfs_realtime_version = self.connect(feed_id)

    def connect(self, route_id):
        real_time_feed_link = get_url(route_id)
        try:
            #post carries request parameters in message body as detailed
            bytes_response = requests.post(url=real_time_feed_link, headers=HEADERS)
            gtfs_parser.ParseFromString(bytes_response.content)

        except requests.RequestException as e:
            print("Cannot connect to URL: " + real_time_feed_link + "\n" + e.__str__())

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
    #TODO: Refer to gtfs_class_parsers.py
    # Given that multiple departure times for a given train is obtained,
    # how does one determine which one to always correctly choose from for a given stop??

    #TODO: better design to have class user just insert train number/letter
    mta_object = MTARealTimeFeed("2")

    #print("MTA Trains: " + str(mta_object.get_train_count()))
    print("Time Feed was Pulled from MTA Server: " + mta_object.get_feed_timestamp())
    #print("Feed Version: " + mta_object.get_realtime_version())

    feed_entity_object = mta_object.get_mta_trains()
    print(feed_entity_object)


if __name__ == '__main__':
    main()