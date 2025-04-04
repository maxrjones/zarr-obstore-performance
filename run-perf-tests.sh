#!/usr/bin/env bash

echo "date,file,library,execution_time,concurrency" > timings.csv

CONCURRENCY_VALUES=(10 100 200)
REPETITIONS=8
for concurrency in "${CONCURRENCY_VALUES[@]}"
do
    # Run each script multiple times
    for (( rep=1; rep<=$REPETITIONS; rep++ ))
    do
    echo "Running benchmark with concurrency = $concurrency, repitition = $rep"
    python zarr-fsspec-s3store.py --concurrency $concurrency
    python zarr-obstore-s3store.py --concurrency $concurrency
    echo "----------------------------------------"
    done
done
