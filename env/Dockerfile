from ubuntu
ENV work /work
WORKDIR ${work}
ADD . $work

RUN apt-get update 
RUN apt-get install -y python python-dev python-pip 
RUN pip install -r requirements.txt
RUN pip install -r requirements_new.txt
