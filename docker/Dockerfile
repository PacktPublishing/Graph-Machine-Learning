FROM jupyter/scipy-notebook

ARG user=euler

USER root

RUN apt-get update && apt-get install git-all -y

RUN useradd -ms /bin/bash ${user}
RUN deluser --remove-home jovyan

USER ${user}

ENV HOME /home/${user}
ENV NB_USER=${user}
ENV XDG_CACHE_HOME=/home/${user}/.cache/

RUN git clone https://github.com/deusebio/Graph-Machine-Learning.git /home/${user}/Graph-Machine-Learning

WORKDIR /home/${user}/Graph-Machine-Learning

RUN ln -s /data data

RUN git checkout chap6

RUN conda create -n chap1 python=3.9
RUN conda run -n chap1 pip install -r Chapter01/requirements.txt
RUN conda run -n chap1 python -m ipykernel install --name chap1 --user

RUN conda create -n chap2 python=3.11
RUN conda run -n chap2 pip install -r Chapter02/requirements.txt
RUN conda run -n chap2 python -m ipykernel install --name chap2 --user

RUN conda create -n chap3 python=3.8
RUN conda run -n chap3 pip install -r Chapter03/requirements.txt
RUN conda run -n chap3 python -m ipykernel install --name chap3 --user

RUN conda create -n chap6 python=3.8
RUN conda run -n chap6 pip install -r Chapter06/requirements.txt
RUN conda run -n chap6 python -m ipykernel install --name chap6 --user

EXPOSE 8888

ENTRYPOINT jupyter notebook --no-browser --port 8888 --NotebookApp.token='' --NotebookApp.password=''