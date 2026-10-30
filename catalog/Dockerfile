FROM python:3.13-slim AS builder

WORKDIR /build

COPY requirements.txt .
RUN pip install --no-cache-dir \
    --prefix=/install \
    -r requirements.txt

FROM python:3.13-slim

WORKDIR /app

RUN groupadd --system appgroup && \
    useradd --system --gid appgroup appuser

COPY --from=builder /install /usr/local
COPY catalog/main.py ./main.py

USER appuser

EXPOSE 8002

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]