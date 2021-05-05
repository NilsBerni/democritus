
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
        events = 21348
        traces = 4580
        activities = 14
        avg_events_per_trace = 4.66
        max_trace_length = 15
        avg_event_duration_seconds = 964224  # seconds
        max_event_duration_seconds = 5180544  # seconds
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
    # TODO: read from a csv
    def getMatrix(self):
        camargo = {self.events: 1, self.traces: 1, self.activities: 1, self.avg_events_per_trace: -1, self.max_trace_length: -2, self.avg_event_duration_seconds: 3, self.max_event_duration_seconds: 2}
        tax =     {self.events: 2, self.traces: 2, self.activities: 2, self.avg_events_per_trace: -1, self.max_trace_length: -1, self.avg_event_duration_seconds: 2, self.max_event_duration_seconds: 1}
        lin =     {self.events: 1, self.traces: 1, self.activities: 3, self.avg_events_per_trace: 1, self.max_trace_length: -1, self.avg_event_duration_seconds: 1, self.max_event_duration_seconds: 3}
        dimauro = {self.events: 3, self.traces: 2, self.activities: 1, self.avg_events_per_trace: -1, self.max_trace_length: 2, self.avg_event_duration_seconds: 2, self.max_event_duration_seconds: 2}
        pauwels = {self.events: -1, self.traces: 1, self.activities: 3, self.avg_events_per_trace: 1, self.max_trace_length: 2, self.avg_event_duration_seconds: 1, self.max_event_duration_seconds: 1}
        authors = {'Camargo': camargo,
                   'Tax': tax,
                   'Lin': lin,
                   'DiMauro': dimauro,
                   'Pauwels': pauwels}

        return authors

    def decide(self, xesanalyzer):

        input_log_dict = self.getDict(xesanalyzer)
        average_dict = self.getAverageDict()
        matrix = self.getMatrix()
        author_scoring = {}

        for author, dict in matrix.items():

            score = 0.0

            for key, instrument in dict.items():

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









