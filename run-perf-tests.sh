#!/usr/bin/env bash

echo "date,file,total execution time, average time\n" > timings.csv
python zarr-fsspec-s3store.py
python zarr-obstore-s3store.py
