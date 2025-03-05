# Inherit from a JupyterHub compatible Docker image
FROM quay.io/developmentseed/veda-optimized-data-delivery-image:2025.02.28

# Install Zarr-Python version
RUN python -m pip install "zarr[optional,remote,test] @ git+https://github.com/maxrjones/zarr-python@97935e44c0e89f71e268b1e97e38f1d05ebf6680"
