from flask import render_template, app

from App.run_advise.decider import Decider
from App.run_advise.xes_analyzer import XESAnalyzer


class Advisor:

    xesAalyzer = None

    # String getters
    def get_suggestion(self):
        return self.suggestion

    # Learn
    def learn(self, xes_file):
        self.xesAalyzer = XESAnalyzer()
        self.xesAalyzer.analyze(xes_file)

    # Render html
    def render(self, suggestion):

        events = self.xesAalyzer.get_events()
        traces = self.xesAalyzer.get_traces()
        activities = self.xesAalyzer.get_activities()
        avg_events_per_trace = self.xesAalyzer.get_avg_events_per_trace()
        max_trace_length = self.xesAalyzer.get_max_trace_length()
        avg_event_duration = self.xesAalyzer.get_avg_event_duration()
        max_event_duration = self.xesAalyzer.get_max_event_duration()

        return render_template('advisor_result.html',
                               events=events,
                               traces=traces,
                               activities=activities,
                               avg_events_per_trace=avg_events_per_trace,
                               max_trace_length=max_trace_length,
                               avg_event_duration=avg_event_duration,
                               max_event_duration=max_event_duration,
                               suggestion=suggestion)

    # Think about suggestion
    def think(self, prediction):


        decider = Decider()
        suggestion = decider.decide(self.xesAalyzer, prediction=prediction)

        return suggestion
