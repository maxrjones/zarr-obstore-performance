# Inherit from a JupyterHub compatible Docker image
FROM quay.io/developmentseed/veda-optimized-data-delivery-image:2025.04.03

# Install Zarr-Python version
RUN python -m pip install --no-cache-dir "zarr[optional,upstream,test] @ git+https://github.com/maxrjones/zarr-python@c6ad5ac45c289d70dc1d5e190988fed3adb682f6"
