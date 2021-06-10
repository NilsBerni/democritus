import sys

from Predictions.Execution.Experiments_NextEvent import run_nextevent_pred
from Predictions.Execution.Experiments_Suffix import run_suffix_pred
from Predictions.Execution.Experiments_Train import run_training
from Predictions.Execution.Experiments_Variables import CAMARGO, DIMAURO, EDBN, LIN, TAX
from Predictions.DataProcessing import BPIC12, BPIC12W, BPIC15_1, BPIC15_2, BPIC15_3, BPIC15_4, BPIC15_5, HELPDESK, WEEKEND, LABOUR

def main(argv):

    # Specify event logs that should be considered
    CONSIDERED_EVENTLOGS = [BPIC15_1, BPIC15_2, BPIC15_3, BPIC15_4, BPIC15_5, HELPDESK, BPIC12, BPIC12W, WEEKEND, LABOUR]

    # Specify implementations that should be considered
    CONSIDERED_IMPLEMENTATIONS = [TAX, LIN, DIMAURO, EDBN, CAMARGO]

    if len(argv) == 0:
        for imp in CONSIDERED_IMPLEMENTATIONS:
            for log in CONSIDERED_EVENTLOGS:
                argv = [imp, log]

                if imp is CAMARGO:
                    argv = [imp, log, 'shared_cat']

                if imp is EDBN:
                    argv = [imp, log, 3, 'NEXT']

                # run_training(argv)

                # run_nextevent_pred(argv)

                if imp is not DIMAURO:
                    if imp is EDBN:
                       argv = [imp, log, 3, 'SUFFIX']
                    run_suffix_pred(argv)

if __name__ == "__main__":
    main(sys.argv[1:])
