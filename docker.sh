#!/bin/bash

# Step 1: Start the Docker container
container_id=$(docker run -d -p 7500:80 --restart unless-stopped dorowu/ubuntu-desktop-lxde-vnc)

# Step 2: Wait for the container to be healthy
echo "Waiting for the container to be healthy..."
while true; do
    # Check if the container is healthy
    health_status=$(docker inspect --format '{{.State.Health.Status}}' $container_id)
    if [ "$health_status" == "healthy" ]; then
        echo "Container is healthy and ready!"
        break
    else
        echo "Waiting for container to be healthy..."
        sleep 3  # Check every 3 seconds
    fi
done

# Step 3: Run the command inside the container to check for finish.txt
docker exec -it $container_id bash -c 'while true; do if [ -f /root/newgit/finish.txt ]; then echo "happy file is found now and all scripts are finished successfully without any issue"; break; else echo "start does not exist"; sleep 3; fi; done'
