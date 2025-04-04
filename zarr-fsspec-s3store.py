import timeit
import argparse
from utils import store_results


def run_benchmarks(concurrency):
    setup = f"""
import zarr
import fsspec
from zarr.storage import FsspecStore

zarr.config.set({{'async.concurrency': {concurrency}}})
bucket = "nasa-veda-scratch"
path = "zarr-obstore-test/max/zarr-v3/test-era5-v3-919"

# Open store with fsspec
fs, path = fsspec.url_to_fs(f"s3://{{bucket}}/{{path}}", anon=False, asynchronous=True)
store = FsspecStore(fs, read_only=True, path=path)

arr = zarr.open_array(store, zarr_version=3, path="PV")
"""

    load_arr = """
arr[:]
"""

    exec_time = timeit.timeit(stmt=load_arr, setup=setup, number=1)
    store_results(__file__, "fsspec", exec_time, concurrency)


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
