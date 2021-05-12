FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

ARG USER_ID
ARG GROUP_ID

RUN addgroup --gid ${GROUP_ID} py3user
RUN adduser --disabled-password --gecos '' --uid ${USER_ID} --gid ${GROUP_ID} py3user
USER py3user
