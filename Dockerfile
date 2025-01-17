# Inherit from a JupyterHub compatible Docker image
FROM quay.io/developmentseed/veda-optimized-data-delivery-image:2025.01.10

# Install obstore development packages (based on discussion in https://github.com/zarr-developers/zarr-python/pull/1661)
RUN python -m pip install obstore==0.3.0

# Install Zarr-Python version
RUN python -m pip install "zarr[optional,remote,test] @ git+https://github.com/maxrjones/zarr-python@0f8820d00d5c9a99c045493c68c8368c701a6a9c
