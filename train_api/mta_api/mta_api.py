from google.transit import gtfs_realtime_pb2
import urllib.request
import datetime
from configparser import ConfigParser

#TODO: Add properties file where api_key becomes encripted and change abs path format below
#TODO: properties file will also stores (id -> subway line number) values
#TODO: properties file will also store (train set -> feed id)
REAL_TIME_FEED_LINK = "http://datamine.mta.info/mta_esi.php?key={0}&feed_id={1}"

'''
MTA trains are grouped into these feed numbers.
Grouping details available on: http://datamine.mta.info/list-of-feeds
'''

'''
From a design perspective, Do not want class to perform all of this variable definitions
so it's loaded first when program starts
'''

LIST_OF_FEEDS = [1, 2, 11, 16, 21, 26, 31, 36, 51]
FEED_MESSAGE = gtfs_realtime_pb2.FeedMessage()
parser = ConfigParser()
#TODO: get relative path inserted instead of absolute path
parser.read('/Users/keslermathieu/Kes_Python_Repo/rest_api/train_api/mta_api/mta_config/mta_config.ini')
API_KEY = parser.get('keys', 'API_KEY')

class MTARealTimeFeed:
    '''
    class that pulls in real time data feeds from the Metropolitan Transportation Authority
    based in New York City. The feed that request.get() ingests is serialized
    (object converted into a binary stream for efficient data transmission across MTA network).
    Thus, Google's gtfs_realtime_pb2 in essential for conversion of this binary into readable format

    Refer to http://datamine.mta.info/list-of-feeds for MTA API changes
    '''

    '''
    #Data that serves as good elements to do predictive analysis on:
    #TODO: enum OccupancyStatus
    #TODO: enum Cause
    #TODO: enum CongestionLevel
    #TODO: enum Effect
    '''

    '''
    #Goal: Analyze Weekday 2/5 North Bound Lines and discover trends based on emergency alerts. By discovering
    emergency trends, the findings can be published so that commuters can know: the probability of a 
    type of emergency happening, where it typically occurs on the transit line, which day and what time during
    the day it occurs. Commuters can avoid getting caught in major delay points by using this predictive model and 
    find alternate routes or external transit means thus increasing customer satisfaction.  
    '''

    def __init__(self, feed_id):
        self.connect(feed_id)

    def connect(self, feed_id):
        if feed_id not in LIST_OF_FEEDS:
            raise ValueError(str(feed_id) +
                             " is NOT a part of MTA train partitions: " +
                             str(LIST_OF_FEEDS))

        real_time_feed_link = REAL_TIME_FEED_LINK.format(API_KEY, feed_id)

        try:
            binary_data = urllib.request.urlopen(real_time_feed_link)
            FEED_MESSAGE.ParseFromString(binary_data.read())

        except urllib.error.URLError as e:
            print("Cannot connect to URL: " + real_time_feed_link + "\n" + str(e.reason))


        #TODO return a 3 element tupple and assign instance vars in constructor
        #TODO: add logging
        self.__mta_trains = [entity for entity in FEED_MESSAGE.entity]
        self.__feed_timestamp = FEED_MESSAGE.header.timestamp
        self.__gtfs_realtime_version = FEED_MESSAGE.header.gtfs_realtime_version


    def get_mta_trains(self):
        return self.__mta_trains


    def get_mta_train(self, train_id):
        train_length = len(self.__mta_trains)
        if train_id >= 0:
            if train_id <= train_length-1:
                return self.__mta_trains[train_id-1]
        else:
            raise IndexError("Select a train ID less than or equal to " + str(train_length))


    def get_feed_timestamp(self):
        return self.__convert_timestamp_to_datetime(self.__feed_timestamp)

    def __convert_timestamp_to_datetime(self, timestamp):
        return datetime.datetime.fromtimestamp(
                int(timestamp)
                ).strftime('%m-%d-%Y %H:%M:%S')


    def get_realtime_version(self):
        return self.__gtfs_realtime_version


    #def get_train_departure_delays(self):
        #return self.__mta_trains

    '''
    iterate through list of feedEntity objects and find which train id corresponds to subway line number
    there's a static mta webpage that has the conversions... Assuming that this page does not change, the 
    (id -> subway line number) can be hardcoded 
    '''

    #def get_subway_line(self, subway_line_number):


def main():
    #TODO: arg parser and include feed number as one switch
    mta_object = MTARealTimeFeed(1)
    train_count = len(mta_object.get_mta_trains())

    print("MTA Trains: " + str(train_count))
    #print("Time Feed was Pulled from MTA Server: " + mta_object.get_feed_timestamp())
    #print("Feed Version: " + mta_object.get_realtime_version())

    feed_entity_object = mta_object.get_mta_train(100)
    print(feed_entity_object)


if __name__ == '__main__':
    main()