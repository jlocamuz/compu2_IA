# Same thing than the 'server' Dockerfile.
FROM python:3.10.9

# Same thing than the 'server' Dockerfile.
# We import 'client.py' in '/client/' folder.
ADD . /client/
ADD requirements.txt /client

RUN pip install -r ./client/requirements.txt

# I would like to introduce something new, the 'WORKDIR' command.
# This command changes the base directory of your image.
# Here we define '/client/' as base directory.
WORKDIR /client/
