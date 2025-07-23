FROM python:3.13.5-slim
WORKDIR /app
COPY . /app
CMD ["python", "garden_advice.py"]
