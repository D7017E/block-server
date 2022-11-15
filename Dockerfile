FROM python:2.7.18

# Download naoqi sdk
RUN wget -P ~/Downloads https://community-static.aldebaran.com/resources/2.5.10/Python%20SDK/pynaoqi-python2.7-2.5.7.1-linux64.tar.gz
# creates folder for naoqi sdk
RUN mkdir -p /etc/python2.7
# extract naoqi sdk
RUN tar -xf ~/Downloads/pynaoqi-python2.7-2.5.7.1-linux64.tar.gz -C /etc/python2.7/
# change name
RUN mv /etc/python2.7/pynaoqi-python2.7-2.5.7.1-linux64 /etc/python2.7/python-naoqi-sdk
# remove naoqi sdk tar
RUN rm ~/Downloads/pynaoqi-python2.7-2.5.7.1-linux64.tar.gz
# add python naoqi sdk to environment path
ENV PYTHONPATH=${PYTHONPATH}:/etc/python2.7/python-naoqi-sdk/lib/python2.7/site-packages
WORKDIR /usr/src/app
# RUN python -m site

COPY requirements.txt ./
RUN pip2 install -r requirements.txt

COPY . .

# TODO: Not copy .env file, make the password come from the docker environment
# Run code test
# RUN pylint *.py

CMD [ "python2", "-u", "./main.py" ]