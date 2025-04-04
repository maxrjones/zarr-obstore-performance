# Inherit from a JupyterHub compatible Docker image
FROM quay.io/developmentseed/veda-optimized-data-delivery-image:2025.04.03

# Install Zarr-Python version
RUN python -m pip install --no-cache-dir "zarr[optional,upstream,test] @ git+https://github.com/maxrjones/zarr-python@98cff171c464d67b555b0384555d3fac37ac1724"
