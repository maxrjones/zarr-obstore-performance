# Inherit from a JupyterHub compatible Docker image
FROM quay.io/developmentseed/veda-optimized-data-delivery-image:2025.01.24

# Install Zarr-Python version
RUN python -m pip install "zarr[upstream] @ git+https://github.com/maxrjones/zarr-python@9c259d2ab12718f7d3796ad91a2129c034c1b0a1"
