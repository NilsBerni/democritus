import csv
import os

import numpy

from App.run_advise.xes_analyzer import XESAnalyzer


class Decider:

    # KEYS
    # these keys are measuring instruments to identify the right framework
    events = 'events'
    traces = 'traces'
    activities = 'activities'
    avg_events_per_trace = 'avg_events_per_trace'
    max_trace_length = 'max_trace_length'
    avg_event_duration_seconds = 'avg_event_duration_seconds'
    max_event_duration_seconds = 'max_event_duration_seconds'

    # BENCHMARKS
    # these determine the average values of popular event logs
    def getAverageDict(self):

        events = XESAnalyzer.avg_events
        traces = XESAnalyzer.avg_traces
        activities = XESAnalyzer.avg_activities
        avg_events_per_trace = XESAnalyzer.avg_avg_events_per_trace
        max_trace_length = XESAnalyzer.avg_max_trace_length
        avg_event_duration_seconds = XESAnalyzer.avg_avg_event_duration_seconds   # seconds
        max_event_duration_seconds = XESAnalyzer.avg_max_event_duration_seconds   # seconds
        average = {self.events: events, self.traces: traces, self.activities: activities, self.avg_events_per_trace: avg_events_per_trace,
                   self.max_trace_length: max_trace_length, self.avg_event_duration_seconds: avg_event_duration_seconds, self.max_event_duration_seconds: max_event_duration_seconds}
        return average

    # Input log transformation
    def getDict(self, xes_analyzer):
        events = xes_analyzer.events
        traces = xes_analyzer.traces
        activities = xes_analyzer.activities
        avg_events_per_trace = xes_analyzer.avg_events_per_trace
        max_trace_length = xes_analyzer.max_trace_length
        avg_event_duration_seconds = xes_analyzer.avg_event_duration_seconds
        max_event_duration_seconds = xes_analyzer.max_event_duration_seconds
        log_dict = {self.events: events, self.traces: traces, self.activities: activities,
                   self.avg_events_per_trace: avg_events_per_trace,
                   self.max_trace_length: max_trace_length, self.avg_event_duration_seconds: avg_event_duration_seconds,
                   self.max_event_duration_seconds: max_event_duration_seconds}
        return log_dict

    # AUTHORS
    # authors are measured by measuring instruments with one integer
    # value > 0 means suited for a large integer
    # value < 0 means not suited for a large integer
    def getMatrix(self, prediction):

        my_path = os.path.abspath(os.path.dirname(__file__))
        matrix_path = os.path.join(my_path, f"value_matrix_gen/output/{prediction}_matrix.csv")
        with open(matrix_path, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            array2d = list(reader)
            tArray2d = numpy.transpose(array2d)
            authors = {}
            for idx, row in enumerate(tArray2d):

                if idx == 0:
                    continue

                values = list(row.copy())
                values.pop(0)
                authors[row[0]] = {self.events: values[0], self.traces: values[1], self.activities: values[2], self.avg_events_per_trace: values[3], self.max_trace_length: values[4]}

        return authors

    def find_strongest(self, datafile_path, name):
        with open(datafile_path) as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            headers = next(reader, None)
            for row in reader:
                if row[0].capitalize() == name.capitalize():
                    list = row.copy()
                    list.pop(0)
                    max_value = max(list)
                    max_index = list.index(max_value)
                    suggestion = headers[max_index + 1]

        return suggestion

    def decide(self, xesanalyzer, prediction):

        my_path = os.path.abspath(os.path.dirname(__file__))
        suffix_pred_path = os.path.join(my_path, "decision_helper/data/suffix_pred.csv")
        event_pred_path = os.path.join(my_path, "decision_helper/data/event_pred.csv")

        if prediction == "next":
            suggestion = self.find_strongest(event_pred_path, xesanalyzer.name)


        if prediction == "suffix":
            suggestion = self.find_strongest(suffix_pred_path, xesanalyzer.name)

        return suggestion.upper()


    def decide_strong_weak(self, xesanalyzer, prediction):

        input_log_dict = self.getDict(xesanalyzer)
        average_dict = self.getAverageDict()
        matrix = self.getMatrix(prediction)
        author_scoring = {}

        for author, dict in matrix.items():

            score = 0.0

            for key, instrument in dict.items():
                instrument = float(instrument)

                if average_dict[key] is not None and input_log_dict[key] is not None:
                    average_value = average_dict[key]
                    input_log_value = input_log_dict[key]
                    ratio = input_log_value / average_value

                    score += ratio * instrument

            author_scoring[author] = score

        max_score = 0
        suggested_author = ''
        for author, score in author_scoring.items():
            if score > max_score:
                max_score = score
                suggested_author = author


        return suggested_author









