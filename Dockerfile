# This code belongs to anmol0700,  
# a passionate developer dedicated to  
# creating innovative solutions and tools.  

# For more updates and projects,  
# please visit: t.me/anmol0700.  

# Your support is greatly appreciated,  
# and it motivates continuous improvement.  

# Feel free to reach out with feedback,  
# or to collaborate on exciting ideas.  

# Together, we can build amazing things!  
# Thank you for being a part of this journey! 

FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /VJ-Post-Search-Bot
WORKDIR /VJ-Post-Search-Bot
COPY . /VJ-Post-Search-Bot
CMD gunicorn app:app & python3 main.py
