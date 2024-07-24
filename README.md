# ip_logging

Docker is a open source platform that packs our application and its dependencies, ensuring that is runs consistently on different environments.
Docker registry is storage system for Docker images. Docker hub is default public registry.
Dockerfile is a script containing instrunctions to build a Docker image, its specifies the base image, application code and dependencies.
each line in a dockerfile creates a docker laywers and cached it.
cmd and dockerfile are two dockerfile instrunctions that combined together and define the command that runs when your container start.
images can only have one entrypoint
ENTRYPOINT is the process that’s executed inside the container.
CMD is the default set of arguments that are supplied to the ENTRYPOINT process.
tag and push to docker registry command (docker -t myimage:latest mydockerusername/mayimage:latest).
port forwarding in docker alows us to expose and map the host port to the container port.
a service can be run by one or more containers. with docker you can handle conteriners and with docker compose you can handle services.
