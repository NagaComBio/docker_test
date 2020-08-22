# docker_test
A repo to create a docker image for training ML applications.<br>

#### Inspiration
Based on the video from Abhishek Thakur.
The video [link]( https://www.youtube.com/watch?v=0qG_0CPQhpg&t=1947s).

#### Docker Image
Have pushed the resulting image to the [Docker hub](https://hub.docker.com/r/nagarajanp/ml_training).

#### To Train
Download the imdb 50k data locally as train.csv and mount the input directories (volumes) to the containers.
```
sudo docker run -v $(pwd):/home/app/src -v /home/user10/project/imdb/input:/home/app/data -it ml_training:test /bin/bash -c "source activate ml_env && cd /home/app/src && python imbd_naiveBayes.py"
```
