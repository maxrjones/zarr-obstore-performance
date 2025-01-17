from datetime import datetime

REP = 50


def store_results(file, exec_time, ave_time):
    with open("timings.csv", "a") as f:
        f.write(f"{datetime.now()},{file},{exec_time},{ave_time}\n")
