import argparse
import timeit

from utils import store_xarray_query_results


def run_benchmarks(concurrency):
    setup = f"""
import zarr
import xarray as xr

zarr.config.set({{'async.concurrency': {concurrency}}})
uri = 'gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3'
"""

    open_dataset = """
ds = xr.open_dataset(
	uri,
	engine='zarr',
	consolidated=False,
	storage_options = {'token': 'anon'})
value = ds["100m_u_component_of_wind"].sel(time=slice(ds.attrs['valid_time_start'], ds.attrs['valid_time_stop'])).isel(time=20000, latitude=234, longitude=253).values
"""

    exec_time = timeit.timeit(stmt=open_dataset, setup=setup, number=1)
    store_xarray_query_results(__file__, "fsspec", exec_time, concurrency)


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
