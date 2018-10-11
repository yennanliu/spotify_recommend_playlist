# Build local DS env on mac OS X 
# start with  anaconda3 python 3


#############  install anaconda3 ################

FROM continuumio/anaconda3
MAINTAINER "yen"

#############  install library ################

RUN apt-get update && apt-get install -y libgtk2.0-dev && \
    rm -rf /var/lib/apt/lists/* && \
    /opt/conda/bin/conda install numpy pandas scikit-learn spotipy flask && \
    /opt/conda/bin/conda upgrade dask 


#############  run commands  ################

RUN ["mkdir", "notebooks"]

COPY jupyter_notebook_config.py /root/.jupyter/

# Jupyter ports
EXPOSE 8888 

# Store notebooks in this mounted directory
VOLUME /notebooks


#############  run the flask app  ################

#ENTRYPOINT ["python"]
#CMD ["server.py"]











