FROM bannsec/w3af

# Set root user
USER root

# Copy files
COPY . . 

ENTRYPOINT ["python3", "scan_config_creator.py"]