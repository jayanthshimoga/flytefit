FROM python:3.9-slim-buster
LABEL org.opencontainers.image.source https://github.com/flyteorg/flytesnacks

WORKDIR /root
ENV VENV /opt/venv
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONPATH /root

RUN apt-get update && apt-get install -y build-essential curl

# Virtual environment
ENV VENV /opt/venv
RUN python3 -m venv ${VENV}
ENV PATH="${VENV}/bin:$PATH"


RUN pip install flytekit==1.10.2 && \
    pip install flytekitplugins-envd==1.10.2 

COPY . .

# RUN pip install flytekit==1.10.0 flytekitplugins-envd
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry export -f requirements.txt --output requirements.txt && \
    pip install -r requirements.txt 

# # Copy the actual code
COPY . /root

# This tag is supplied by the build script and will be used to determine the version
# when registering tasks, workflows, and launch plans
ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag
