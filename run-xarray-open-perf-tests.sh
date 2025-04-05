#!/usr/bin/env bash

echo "date,file,library,execution_time,concurrency" > results/xarray-open-timings.csv

CONCURRENCY_VALUES=(10 100 200)
REPETITIONS=8
for concurrency in "${CONCURRENCY_VALUES[@]}"
do
    # Run each script multiple times
    for (( rep=1; rep<=$REPETITIONS; rep++ ))
    do
    echo "Running benchmark with concurrency = $concurrency, repetition = $rep"
    python scripts/xarray-open-fsspec-gcs.py --concurrency $concurrency
    python scripts/xarray-open-obstore-gcs.py --concurrency $concurrency
    echo "----------------------------------------"
    done
done
