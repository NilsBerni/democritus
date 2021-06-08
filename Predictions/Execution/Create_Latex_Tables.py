

import os



training_times_latex_table = """\\begin{table}[]
\\centering
\\begin{tabular}{l|l||l|l|l|l|l}
& Dataset     & DiMauro&  Lin   &  Tax   & Pauwels& Cam. Sp & Cam. Sh      \\\ \hline \hline
\multirow{11}{*}{\\rotatebox{90}{Training time}}              
"""

pred_next_times_latex_table = """\\begin{table}[]
\\centering
\\begin{tabular}{l|l||l|l|l|l|l}
& Dataset     & DiMauro&  Lin   &  Tax   & Pauwels& Cam. Sp & Cam. Sh      \\\ \hline \hline
\multirow{11}{*}{\\rotatebox{90}{Training time}}              
"""

pred_next_accuracy_latex_table = """\\begin{table}[]
\\centering
\\begin{tabular}{l|l||l|l|l|l|l}
& Dataset     & DiMauro&  Lin   &  Tax   & Pauwels& Cam. Sp & Cam. Sh      \\\ \hline \hline
\multirow{11}{*}{\\rotatebox{90}{Training time}}              
"""

pred_suffix_times_latex_table = """\\begin{table}[]
\\centering
\\begin{tabular}{l|l||l|l|l|l|l}
& Dataset     &  Lin   &  Tax   & Pauwels& Cam. Sp & Cam. Sh      \\\ \hline \hline
\multirow{11}{*}{\\rotatebox{90}{Training time}}              
"""

pred_suffix_accuracy_latex_table = """\\begin{table}[]
\\centering
\\begin{tabular}{l|l||l|l|l|l}
& Dataset     &  Lin   &  Tax   & Pauwels& Cam. Sh & Cam. Sh      \\\ \hline \hline
\multirow{11}{*}{\\rotatebox{90}{Training time}}              
"""


current_log = ""
for subdir, dirs, files in os.walk('Output'):

    for file in files:

        log_name = os.path.normpath(subdir).split('/')[1]
        print(log_name)

        if log_name != current_log:
            print("New Line")
            current_log = log_name
            newLine = '{:14s}'.format(f"& {log_name}")
            training_times_latex_table += f"""\\\ \n{newLine}"""
            pred_next_times_latex_table += f"""\\\ \n{newLine}"""
            pred_next_accuracy_latex_table += f"""\\\ \n{newLine}"""
            pred_suffix_accuracy_latex_table += f"""\\\ \n{newLine}"""
            pred_suffix_times_latex_table += f"""\\\ \n{newLine}"""

        filepath = subdir + os.sep + file
        if filepath.endswith("timings_train.log"):
            f = open(filepath, "r")
            txt = f.read()
            result = txt.split("""\n\n""")
            if len(result[len(result) - 1]) < 1:
                result.pop()

            lines = result[len(result) - 1].split("\n")
            last_line = lines[len(lines) - 1]
            name, var = last_line.partition(":")[::2]
            duration = var.split(".")[0]
            durationF = '{:9s}'.format(f"& {duration}")

            if len(result) > 2:
                print(f.read())

            training_times_latex_table += durationF

        if filepath.endswith("timings_next_event.log"):
            f = open(filepath, "r")
            txt = f.read()
            result = txt.split("""\n\n""")
            if len(result[len(result) - 1]) < 1:
                result.pop()

            lines = result[len(result) - 1].split("\n")
            last_line = lines[len(lines) - 1]
            name, var = last_line.partition(":")[::2]
            duration = var.split(".")[0]
            durationF = '{:9s}'.format(f"& {duration}")

            if len(result) > 2:
                print(f.read())

            pred_next_times_latex_table += durationF


        if filepath.endswith("results_next_event.log"):
            f = open(filepath, "r")
            txt = f.read()
            result = txt.split("""\n""")
            if len(result[len(result) - 1]) < 1:
                result.pop()

            last_line = result[len(result) - 1]
            columns = last_line.split(" ")
            accuracy = float(columns[len(columns) - 1])
            formatted = "{:1.3f}".format(accuracy)
            durationF = '{:9s}'.format(f"& {formatted} ")

            if len(result) > 2:
                print(f.read())

            pred_next_accuracy_latex_table += durationF


        if filepath.endswith("timings_suffix.log"):
            f = open(filepath, "r")
            txt = f.read()
            result = txt.split("""\n\n""")
            if len(result[len(result) - 1]) < 1:
                result.pop()

            lines = result[len(result) - 1].split("\n")
            last_line = lines[len(lines) - 1]
            name, var = last_line.partition(":")[::2]
            duration = var.split(".")[0]
            durationF = '{:9s}'.format(f"& {duration}")

            if len(result) > 2:
                print(f.read())

            pred_suffix_times_latex_table += durationF

        if filepath.endswith("results_suffix.log"):
            f = open(filepath, "r")
            txt = f.read()
            result = txt.split("""\n""")
            if len(result[len(result) - 1]) < 1:
                result.pop()

            last_line = result[len(result) - 1]
            columns = last_line.split(" ")
            accuracy = float(columns[len(columns) - 1])
            formatted = "{:1.3f}".format(accuracy)
            durationF = '{:9s}'.format(f"& {formatted} ")

            if len(result) > 2:
                print(f.read())

            pred_suffix_accuracy_latex_table += durationF




training_times_latex_table += """
\hline \hline
                                                             \end{tabular}
\caption{\label{tab:robots} All time related values are given in seconds. The training times for Pauwels implementation are measured using the next event optimized training and the k-value is set to 3.}
\label{table:compareT}
\end{table}
"""

pred_next_times_latex_table += """
\hline \hline
                                                             \end{tabular}
\caption{\label{tab:robots} The prediction accuracy for Pauwels implementation is measured using the next event optimized training and the k-value is set to 3..}
\label{table:compareT}
\end{table}
"""

pred_next_accuracy_latex_table += """
\hline \hline
                                                             \end{tabular}
\caption{\label{tab:robots} The prediction accuracy for Pauwels implementation is measured using the next event optimized training and the k-value is set to 3..}
\label{table:compareT}
\end{table}
"""

pred_suffix_times_latex_table += """
\hline \hline
                                                             \end{tabular}
\caption{\label{tab:robots} The prediction accuracy for Pauwels implementation is measured using the next event optimized training and the k-value is set to 3..}
\label{table:compareT}
\end{table}
"""

pred_suffix_accuracy_latex_table += """
\hline \hline
                                                             \end{tabular}
\caption{\label{tab:robots} The prediction accuracy for Pauwels implementation is measured using the next event optimized training and the k-value is set to 3..}
\label{table:compareT}
\end{table}
"""

f = open("Latex/training_times_latex_table.txt", "a")
f.truncate(0)
f.write(training_times_latex_table)
f.close()

f = open("Latex/pred_next_times_latex_table.txt", "a")
f.truncate(0)
f.write(pred_next_times_latex_table)
f.close()

f = open("Latex/pred_next_accuracy_latex_table.txt", "a")
f.truncate(0)
f.write(pred_next_accuracy_latex_table)
f.close()

f = open("Latex/pred_suffix_accuracy_latex_table.txt", "a")
f.truncate(0)
f.write(pred_suffix_accuracy_latex_table)
f.close()

f = open("Latex/pred_suffix_times_latex_table.txt", "a")
f.truncate(0)
f.write(pred_suffix_times_latex_table)
f.close()