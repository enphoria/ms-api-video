FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
RUN prb_api_video create-db
RUN prb_api_video populate-db
RUN prb_api_video add-user -u admin -p admin
EXPOSE 5000
CMD ["prb_api_video", "run"]
