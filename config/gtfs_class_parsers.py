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


#TODO: finish class relation -> dictionary mapping

# _TRIPUPDATE_STOPTIMEEVENT.containing_type = _TRIPUPDATE
# _TRIPUPDATE_STOPTIMEUPDATE.fields_by_name['arrival'].message_type = _TRIPUPDATE_STOPTIMEEVENT
# _TRIPUPDATE_STOPTIMEUPDATE.fields_by_name['departure'].message_type = _TRIPUPDATE_STOPTIMEEVENT
# _TRIPUPDATE_STOPTIMEUPDATE.fields_by_name['schedule_relationship'].enum_type = _TRIPUPDATE_STOPTIMEUPDATE_SCHEDULERELATIONSHIP
# _TRIPUPDATE_STOPTIMEUPDATE.containing_type = _TRIPUPDATE
# _TRIPUPDATE_STOPTIMEUPDATE_SCHEDULERELATIONSHIP.containing_type = _TRIPUPDATE_STOPTIMEUPDATE
# _TRIPUPDATE.fields_by_name['trip'].message_type = _TRIPDESCRIPTOR
# _TRIPUPDATE.fields_by_name['vehicle'].message_type = _VEHICLEDESCRIPTOR
# _TRIPUPDATE.fields_by_name['stop_time_update'].message_type = _TRIPUPDATE_STOPTIMEUPDATE
# _VEHICLEPOSITION.fields_by_name['trip'].message_type = _TRIPDESCRIPTOR
# _VEHICLEPOSITION.fields_by_name['vehicle'].message_type = _VEHICLEDESCRIPTOR
# _VEHICLEPOSITION.fields_by_name['position'].message_type = _POSITION
# _VEHICLEPOSITION.fields_by_name['current_status'].enum_type = _VEHICLEPOSITION_VEHICLESTOPSTATUS
# _VEHICLEPOSITION.fields_by_name['congestion_level'].enum_type = _VEHICLEPOSITION_CONGESTIONLEVEL
# _VEHICLEPOSITION.fields_by_name['occupancy_status'].enum_type = _VEHICLEPOSITION_OCCUPANCYSTATUS
# _VEHICLEPOSITION_VEHICLESTOPSTATUS.containing_type = _VEHICLEPOSITION
# _VEHICLEPOSITION_CONGESTIONLEVEL.containing_type = _VEHICLEPOSITION
# _VEHICLEPOSITION_OCCUPANCYSTATUS.containing_type = _VEHICLEPOSITION
# _ALERT.fields_by_name['active_period'].message_type = _TIMERANGE
# _ALERT.fields_by_name['informed_entity'].message_type = _ENTITYSELECTOR
# _ALERT.fields_by_name['cause'].enum_type = _ALERT_CAUSE
# _ALERT.fields_by_name['effect'].enum_type = _ALERT_EFFECT
# _ALERT.fields_by_name['url'].message_type = _TRANSLATEDSTRING
# _ALERT.fields_by_name['header_text'].message_type = _TRANSLATEDSTRING
# _ALERT.fields_by_name['description_text'].message_type = _TRANSLATEDSTRING
# _ALERT.fields_by_name['tts_header_text'].message_type = _TRANSLATEDSTRING
# _ALERT.fields_by_name['tts_description_text'].message_type = _TRANSLATEDSTRING
# _ALERT.fields_by_name['severity_level'].enum_type = _ALERT_SEVERITYLEVEL
# _ALERT_CAUSE.containing_type = _ALERT
# _ALERT_EFFECT.containing_type = _ALERT
# _ALERT_SEVERITYLEVEL.containing_type = _ALERT
# _TRIPDESCRIPTOR.fields_by_name['schedule_relationship'].enum_type = _TRIPDESCRIPTOR_SCHEDULERELATIONSHIP
# _TRIPDESCRIPTOR_SCHEDULERELATIONSHIP.containing_type = _TRIPDESCRIPTOR
# _ENTITYSELECTOR.fields_by_name['trip'].message_type = _TRIPDESCRIPTOR
# _TRANSLATEDSTRING_TRANSLATION.containing_type = _TRANSLATEDSTRING
# _TRANSLATEDSTRING.fields_by_name['translation'].message_type = _TRANSLATEDSTRING_TRANSLATION