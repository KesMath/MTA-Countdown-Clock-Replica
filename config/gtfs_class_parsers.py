from google.transit import gtfs_realtime_pb2


"""
dictionary sets to serve as a lightweight class documentation without
having to look at internal gtfs_realtime_pb2 module
--------------------------------------------------------
Note: fields starting with capital letter indicates aggregation class relation
"""



"""
Arrows Denote class aggregation relation:
FEED_MESSAGE -> FEEDENTITY -> TRIPUPDATE -> StopTimeUpdate -> STOPTIMEEVENT
"""


FEED_MESSAGE = {
    "class": gtfs_realtime_pb2.FeedMessage(),
    "description": "",
    "fields": {
        "trip_updates_and_alerts": "entity",
        "FeedHeader": "header",
    }
}


FEEDENTITY = {
    "class": gtfs_realtime_pb2.FeedEntity(),
    "description": "",
    "fields": {
        "Trip_Update": "trip_update",
        "VehiclePosition": "vehicle",
        "Alert": "alert",
    }
}


TRIPUPDATE = {
    "class": gtfs_realtime_pb2.TripUpdate(),
    "description": "",
    "fields": {
        "timestamp": "timestamp",
        "delay": "delay",
        "stop_time_update": "stop_time_update",
    }
}