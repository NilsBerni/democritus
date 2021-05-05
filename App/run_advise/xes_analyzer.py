import xml.etree.ElementTree as ET
from datetime import datetime
import pandas as pd
import numpy as np


class XESAnalyzer:

    events = None
    traces = None
    activities = None
    avg_events_per_trace = None
    max_trace_length = None
    avg_event_duration_seconds = None
    max_event_duration_seconds = None
    seconds_in_day = 60 * 60 * 24

    # String getters for showing final result
    def get_events(self):
        return str(self.events)

    def get_traces(self):
        return str(self.traces)

    def get_activities(self):
        return str(self.activities)

    def get_avg_events_per_trace(self):
        return str(round(self.avg_events_per_trace, 2))

    def get_max_trace_length(self):
        return str(self.max_trace_length)

    def get_avg_event_duration(self):
        return str(round(self.avg_event_duration_seconds / self.seconds_in_day, 2)) + ' days'

    def get_max_event_duration(self):
        return str(round(self.max_event_duration_seconds / self.seconds_in_day, 2)) + ' days'

    # Analyze xes file
    def analyze(self, xes_file):

        tree = ET.parse(xes_file)
        root = tree.getroot()

        # Key data
        tracesC = 0
        eventsC = 0
        maxEventsC = 0
        activities = {}
        durations = []

        for trace in root:

            tag = trace.tag.split("}", 2)[-1]
            if tag == 'trace':
                tracesC += 1

                events = list(trace)

                events_of_traceC = 0
                last_event_timestamp = None
                for event in events:
                    tag = event.tag.split("}", 2)[-1]

                    if tag == 'event':
                        events_of_traceC += 1

                        values = list(event)

                        for value in values:

                            if value.attrib['key'] == 'time:timestamp':
                                timestamp_str = value.attrib['value']
                                timestamp = pd.to_datetime(timestamp_str)

                                if last_event_timestamp is not None:
                                    datetime_delta = timestamp.tz_localize(None) - last_event_timestamp.tz_localize(
                                        None)
                                    durations.append(datetime_delta.total_seconds())

                                last_event_timestamp = timestamp

                            if value.attrib['key'] == 'Activity':
                                activity_name = value.attrib['value']

                                if activity_name in activities:
                                    activities[activity_name] = activities[activity_name] + 1
                                else:
                                    activities[activity_name] = 1

                eventsC += events_of_traceC

                if maxEventsC < events_of_traceC:
                    maxEventsC = events_of_traceC

        self.events = eventsC
        self.traces = tracesC
        self.activities = len(activities)
        self.avg_events_per_trace = eventsC / tracesC
        self.max_trace_length = maxEventsC
        self.avg_event_duration_seconds = np.average(durations)
        self.max_event_duration_seconds = np.max(durations)

