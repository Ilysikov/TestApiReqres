FROM jenkins/jenkins:lts AS builder
LABEL "docker"

ENV POETRY_VERSION=1.8.3
ENV POETRY_VENV=/opt/poetry-venv

ENV POETRY_CACHE_DIR=/opt/.cache

FROM builder AS builder2

RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

FROM builder2 AS example-app
COPY --from=builder2 ${POETRY_VENV} ${POETRY_VENV}

ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app




COPY poetry.lock pyproject.toml ./


RUN poetry install --no-interaction --no-cache

COPY . /app

EXPOSE 8080
EXPOSE 50000

CMD [ "python3", "./app.py"]
VOLUME ["/run/docker.sock:/run/docker.sock"]