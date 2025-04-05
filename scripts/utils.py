from datetime import datetime


def store_results(file, store, exec_time, concurrency):
    with open("results/timings.csv", "a") as f:
        f.write(f"{datetime.now()},{file},{store},{exec_time},{concurrency}\n")


def store_xarray_open_results(file, store, exec_time, concurrency):
    with open("results/xarray-open-timings.csv", "a") as f:
        f.write(f"{datetime.now()},{file},{store},{exec_time},{concurrency}\n")


def store_xarray_query_results(file, store, exec_time, concurrency):
    with open("results/xarray-query-timings.csv", "a") as f:
        f.write(f"{datetime.now()},{file},{store},{exec_time},{concurrency}\n")
