import sys
import requests
from queue import PriorityQueue
from mta.tokenauth import TokenAuth
from config.stops_dict import STOPS
from util.os_func import PROJECT_DIR
from configparser import ConfigParser
from util import timestamp_operators
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
        if stop_id not in STOPS.keys():
            raise KeyError(stop_id + " is not a valid stop_id!")
        else:
            self.__stop_name = STOPS.get(stop_id)
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
        queue = PriorityQueue()
        for entity in list_of_entities:
            stops_length = entity.trip_update.stop_time_update.__len__()
            while stops_length != 0:
                stop_time_update_object = entity.trip_update.stop_time_update.pop()
                if stop_time_update_object.stop_id == stop_id:

                    # NOTE: based on observation,
                    # final stop for a given route will NOT contain arrival time field populated
                    stop_time_update_object.arrival.time = \
                        timestamp_operators.compute_relative_time(stop_time_update_object.arrival.time)

                    stop_time_update_object.departure.time = \
                        timestamp_operators.compute_relative_time(stop_time_update_object.departure.time)

                    inbound_train_tup = ({'route_id': entity.trip_update.trip.route_id},
                                         MessageToDict(stop_time_update_object))
                    # NOTE: The choice of either 'Departure times' or 'arrival times'
                    # seems depends on what type of stations.
                    # For in-between stations (those that are not final stops),
                    # arrival & departure times are observed to be identical
                    # values for the most part so either metric is valid for sorting.
                    # From observation, final stop stations
                    # must be treated differently (depending if it's initial or final stop?)
                    try:
                        queue.put(item=(stop_time_update_object.departure.time, inbound_train_tup))
                    except TypeError as e:
                        print(e)
                        print(stop_time_update_object.departure.time)
                        print(inbound_train_tup)
                stops_length -= 1
        return queue

    def get_train_count(self):
        return self.__mta_trains.qsize()

    def get_stop_name(self):
        return self.__stop_name

    def display_trains(self):
        """
        :return: Pops all elements within priorityQueue and returns elements as a list
        Note: This can be used to show all inbound trains for a given stop
        (i.e. displaying all trains on a given )
        """
        queue = list()
        while not self.__mta_trains.empty():
            queue.append(self.__mta_trains.get())
        return queue

    def display_train(self):
        """
        :return:
        """
        return self.__mta_trains.get() if not self.__mta_trains.empty() else None

    def get_feed_timestamp(self):
        return "No Feed Timestamp" if self.__feed_timestamp == 0 \
            else timestamp_operators.convert_timestamp_to_datetime(self.__feed_timestamp)

    def get_realtime_version(self):
        return self.__gtfs_realtime_version

def main():
    #TODO: can create some dictionary mapping route_id -> image so it can be displayed on PI.
    # This will be implemented later when factory class comes into play
    mta_parser = MTARealTimeFeedParser(route_id="2", stop_id="247N")
    print("Feed Version: " + mta_parser.get_realtime_version())
    print("MTA Train Count for this Stop: " + str(mta_parser.get_train_count()))
    print("Stop Name: " + mta_parser.get_stop_name())
    print("Time Feed was Pulled from MTA Server: " + mta_parser.get_feed_timestamp())
    print('\n')
    queue = mta_parser.display_trains()
    for q in queue:
        print(q[1])


if __name__ == '__main__':
    main()