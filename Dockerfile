FROM bannsec/w3af

# Set root user
USER root

# Copy files
COPY . . 

ENTRYPOINT ["python3", "main.py"]