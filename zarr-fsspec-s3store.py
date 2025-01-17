import timeit
from utils import store_results, REP


setup = """
import zarr
import fsspec
from zarr.storage import FsspecStore

bucket = "nasa-veda-scratch"
path = "zarr-obstore-test/max/zarr-v3/test-era5-v3-919"

# Open store with fsspec
fs, path = fsspec.url_to_fs(f"s3://{bucket}/{path}", anon=False, asynchronous=True)
store = FsspecStore(fs, read_only=True, path=path)
"""
load_arr = """
arr = zarr.open_array(store, zarr_version=3, path="PV")
arr[:]
"""

if __name__ == "__main__":
    exec_time = timeit.timeit(stmt=load_arr, setup=setup, number=REP)
    store_results(__file__, exec_time, exec_time / REP)
