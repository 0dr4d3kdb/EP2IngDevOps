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
COPY orders/main.py ./main.py

ENV CATALOG_URL=http://catalog:8002

USER appuser

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]