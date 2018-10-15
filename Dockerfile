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



#############  set up PATH  ################


ENV PYTHONPATH="$PYTHONPATH:/spotify_recommend_playlist"

#############  clone repo  ################

# Clone the conf files into the docker container
RUN git clone https://github.com/yennanliu/spotify_recommend_playlist.git || echo "The repo has been installed in Docker!"
# to the repo 
#RUN cd spotify_recommend_playlist

#############  run the flask app  ################

# app ports
EXPOSE 7777 

# export env variable 
#ENV SPOTIPY_CLIENT_ID=<your_CLIENT_ID> 
#ENV SPOTIPY_CLIENT_ID=<your_CLIENT_SECRET>


# run the APP
ENTRYPOINT ["python"]
CMD ["spotify_recommend_playlist/server.py"]











