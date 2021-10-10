FROM python:alpine
WORKDIR /home/data
COPY . .
CMD ["pyth1.py"]
ENTRYPOINT ["python3"]
