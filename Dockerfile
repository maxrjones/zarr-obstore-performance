# Inherit from a JupyterHub compatible Docker image
FROM quay.io/developmentseed/veda-optimized-data-delivery-image:2025.04.02

# Install Zarr-Python version
RUN python -m pip install "zarr[optional,remote,test] @ git+https://github.com/zarr-developers/zarr-python@9e8b50ae19cc63ad573f58569c3ef5826a5c60fc"
