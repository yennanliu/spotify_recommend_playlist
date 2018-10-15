# Build local DS env on mac OS X 
# start with  anaconda3 python 3


#############  install anaconda3 ################

FROM continuumio/anaconda3
MAINTAINER "yen"

#############  install library ################

RUN rm -rf /var/lib/apt/lists/* && \
    /opt/conda/bin/conda install numpy pandas scikit-learn flask && \
    pip install imutils spotipy && \ 
    /opt/conda/bin/conda upgrade dask 


RUN apt-get install -y git


#############  run commands  ################



#############  clone repo  ################

# Clone the conf files into the docker container
RUN git clone https://github.com/yennanliu/spotify_recommend_playlist.git

#############  run the flask app  ################

# app ports
EXPOSE 7777 

# export env variable 
#ENV SPOTIPY_CLIENT_ID=<your_CLIENT_ID> 
#ENV SPOTIPY_CLIENT_ID=<your_CLIENT_SECRET>


#ENTRYPOINT ["python"]
#CMD ["server.py"]











