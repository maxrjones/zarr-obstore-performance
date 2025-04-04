from datetime import datetime


def store_results(file, store, exec_time, concurrency):
    with open("timings.csv", "a") as f:
        f.write(f"{datetime.now()},{file},{store},{exec_time},{concurrency}\n")


def store_xarray_results(file, store, exec_time, concurrency):
    with open("xarray-timings.csv", "a") as f:
        f.write(f"{datetime.now()},{file},{store},{exec_time},{concurrency}\n")
