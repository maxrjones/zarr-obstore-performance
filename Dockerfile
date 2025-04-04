# Inherit from a JupyterHub compatible Docker image
FROM quay.io/developmentseed/veda-optimized-data-delivery-image:2025.04.03

# Install Zarr-Python version
RUN python -m pip install --no-cache-dir "zarr[optional,remote,test] @ git+https://github.com/maxrjones/zarr-python@d5993777a774748810567d309259ffae06b998fb"
