FROM python:3.12-alpine

RUN pip install uv

COPY . /app

WORKDIR /app

RUN uv sync

EXPOSE 3001

CMD  ["uv", "run", "flask", "--app", "app", "run", "--host", "0.0.0.0", "--port", "3000"]