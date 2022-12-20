FROM python:3.11.1-alpine as builder

RUN python -m venv /opt/openapi-python-client

RUN /opt/openapi-python-client/bin/pip install -U \
    pip \
    openapi-python-client \
    autoflake \
    black \
    isort && \
    /opt/openapi-python-client/bin/pip check

FROM python:3.11.1-alpine as openapi-python-client

COPY --from=builder /opt/openapi-python-client /opt/openapi-python-client

RUN ln -snf /opt/openapi-python-client/bin/openapi-python-client /usr/local/bin/ && \
    ln -snf /opt/openapi-python-client/bin/autoflake /usr/local/bin/ && \
    ln -snf /opt/openapi-python-client/bin/black /usr/local/bin/ && \
    ln -snf /opt/openapi-python-client/bin/isort /usr/local/bin/

CMD ["sh"]
