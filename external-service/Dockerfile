FROM python:3.7.4-alpine
RUN adduser -D flaskuser
ARG word_dir=/home/flaskuser/
ADD requirements.txt $word_dir
ADD main.py $word_dir
WORKDIR $word_dir
RUN pip install -r requirements.txt
USER flaskuser
ENTRYPOINT [ "python" ]

EXPOSE 8080/tcp

CMD  ["main.py"]