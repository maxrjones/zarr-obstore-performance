# Inherit from a JupyterHub compatible Docker image
FROM quay.io/developmentseed/veda-optimized-data-delivery-image:2025.01.24

# Install Zarr-Python version
RUN python -m pip install "zarr[optional,remote,test] @ git+https://github.com/kylebarron/zarr-python@8c3a6f2b6c605e80851587b94d72104fcc4706ff"
