import argparse
import timeit

from utils import store_xarray_query_results


def run_benchmarks(concurrency):
    setup = f"""
import zarr
import xarray as xr
from obstore.store import GCSStore
from zarr.storage import ObjectStore

zarr.config.set({{'async.concurrency': {concurrency}}})
bucket = "gcp-public-data-arco-era5"
path = "ar/full_37-1h-0p25deg-chunk-1.zarr-v3"

# Open store with obstore
gcsstore = GCSStore(bucket, prefix=path, skip_signature=True)
store = ObjectStore(gcsstore, read_only=True)
"""

    open_dataset = """
ds = xr.open_dataset(store, consolidated=False, engine="zarr")
value = ds["100m_u_component_of_wind"].sel(time=slice(ds.attrs['valid_time_start'], ds.attrs['valid_time_stop'])).isel(time=20000, latitude=234, longitude=253).values
"""

    exec_time = timeit.timeit(stmt=open_dataset, setup=setup, number=1)
    store_xarray_query_results(__file__, "obstore", exec_time, concurrency=concurrency)


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
