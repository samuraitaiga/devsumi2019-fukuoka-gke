FROM python:3.7.4-alpine
RUN adduser -D flaskuser
ARG work_dir=/home/flaskuser/
ADD requirements.txt $work_dir
ADD templates $work_dir/templates/
ADD main.py $work_dir
WORKDIR $work_dir
RUN pip install -r requirements.txt
USER flaskuser
ENTRYPOINT [ "python" ]

EXPOSE 8080/tcp

CMD  ["main.py"]