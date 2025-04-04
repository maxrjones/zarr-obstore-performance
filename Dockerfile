# Inherit from a JupyterHub compatible Docker image
FROM quay.io/developmentseed/veda-optimized-data-delivery-image:2025.04.03

# Install Zarr-Python version
RUN python -m pip install --no-cache-dir "zarr[optional,upstream,test] @ git+https://github.com/maxrjones/zarr-python@e536011ce95e150ad2f00582fb5cfc3554dc1d3d"
