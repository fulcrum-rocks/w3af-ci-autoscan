FROM bannsec/w3af

# Set root user
USER root

# Copy files
COPY . . 

ENTRYPOINT ["python", "scan_config_creator.py"]