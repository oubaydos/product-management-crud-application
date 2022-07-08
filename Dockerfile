FROM python
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt # Write Flask in this file
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]