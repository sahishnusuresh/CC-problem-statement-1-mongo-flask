FROM python:3.7-alpine
COPY /app/requirements.txt ./requirements.txt
EXPOSE 27017
COPY /app .
RUN pip install -r ./requirements.txt
ENTRYPOINT [ "python" ]
CMD ["app.py" ]

