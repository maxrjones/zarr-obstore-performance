import argparse
import timeit

from utils import store_results


def run_benchmarks(concurrency):
    setup = f"""
import zarr
from obstore.store import S3Store
from zarr.storage import ObjectStore

zarr.config.set({{'async.concurrency': {concurrency}}})
bucket = "nasa-veda-scratch"
path = "zarr-obstore-test/max/zarr-v3/test-era5-v3-919"

# Open store with obstore
s3store = S3Store(bucket, prefix=path)
store = ObjectStore(s3store, read_only=True)

arr = zarr.open_array(store, zarr_version=3, path="PV")
"""

    load_arr = """
arr[:]
"""

    exec_time = timeit.timeit(stmt=load_arr, setup=setup, number=1)
    store_results(__file__, "obstore", exec_time, concurrency=concurrency)


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Run zarr loading benchmark with configurable concurrency"
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        help="Set the async concurrency value for zarr",
    )
    args = parser.parse_args()

    # Use the concurrency value from command line arguments
    run_benchmarks(args.concurrency)
