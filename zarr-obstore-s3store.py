import timeit
from utils import store_results, REP


setup = """
import zarr
from obstore.store import S3Store, PrefixStore
from zarr.storage.object_store import ObjectStore

bucket = "nasa-veda-scratch"
path = "zarr-obstore-test/max/zarr-v3/test-era5-v3-919"

# Open store with obstore
s3store = S3Store.from_url(f"s3://{bucket}")
prefixstore = PrefixStore(s3store, path)
store = ObjectStore(prefixstore, read_only=True)
"""
load_arr = """
arr = zarr.open_array(store, zarr_version=3, path="PV")
arr[:]
"""

if __name__ == "__main__":
    exec_time = timeit.timeit(stmt=load_arr, setup=setup, number=REP)
    store_results(__file__, exec_time, exec_time / REP)
