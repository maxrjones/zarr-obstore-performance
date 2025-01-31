# Inherit from a JupyterHub compatible Docker image
FROM quay.io/developmentseed/veda-optimized-data-delivery-image:2025.01.24

# Install obstore development packages (based on discussion in https://github.com/zarr-developers/zarr-python/pull/1661)
RUN python -m pip install git+https://github.com/developmentseed/obstore@18197676ae46720dbda9cfd85db02f94e8aba4cf#subdirectory=obstore

# Install Zarr-Python version
RUN python -m pip install "zarr[optional,remote,test] @ git+https://github.com/maxrjones/zarr-python@87a5143a39da4c7c5ae74995d1a788f62b3ce27b"
