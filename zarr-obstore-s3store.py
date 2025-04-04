import timeit
from utils import store_results, REP


setup = """
import zarr
from obstore.store import S3Store
from zarr.storage import ObjectStore

zarr.config.set({'async.concurrency': 128})
bucket = "nasa-veda-scratch"
path = "zarr-obstore-test/max/zarr-v3/test-era5-v3-919"

# Open store with obstore
s3store = S3Store(bucket, prefix=path)
store = ObjectStore(s3store, read_only=True)
"""
load_arr = """
zarr.config.set({'async.concurrency': 128})
arr = zarr.open_array(store, zarr_version=3, path="PV")
arr[:]
"""

if __name__ == "__main__":
    exec_time = timeit.timeit(stmt=load_arr, setup=setup, number=REP)
    store_results(__file__, exec_time, exec_time / REP)
