# Inherit from a JupyterHub compatible Docker image
FROM quay.io/developmentseed/veda-optimized-data-delivery-image:2025.01.24

# Install Zarr-Python version
RUN python -m pip install "zarr[optional,remote,test] @ git+https://github.com/maxrjones/zarr-python@f81a0d0c2f3dfcbc643aa63579a98aa10f23bc5e"
