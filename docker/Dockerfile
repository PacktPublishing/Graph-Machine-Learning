FROM jupyter/scipy-notebook as base

ARG user=euler
ARG branch=main

USER root

RUN apt-get update && apt-get install git-all -y

RUN useradd -ms /bin/bash ${user}
RUN deluser --remove-home jovyan

USER ${user}

ENV HOME /home/${user}
ENV NB_USER=${user}
ENV XDG_CACHE_HOME=/home/${user}/.cache/
ENV DATA_FOLDER=/data

RUN git clone https://github.com/deusebio/Graph-Machine-Learning.git /home/${user}/Graph-Machine-Learning
WORKDIR /home/${user}/Graph-Machine-Learning
RUN git checkout ${branch}

RUN ln -s /data data
EXPOSE 8888

ENTRYPOINT jupyter notebook --no-browser --port 8888 --NotebookApp.token='' --NotebookApp.password=''

FROM base as chap1
RUN ls -d -1 */  | grep -v -e Chapter01 | xargs rm -rf
RUN conda create -n chap1 python=3.9
RUN conda run -n chap1 pip install -r Chapter01/requirements.txt
RUN conda run -n chap1 python -m ipykernel install --name chap1 --user

FROM base as chap2
RUN ls -d -1 */  | grep -v -e Chapter02 | xargs rm -rf
RUN conda create -n chap2 python=3.11
RUN conda run -n chap2 pip install -r Chapter02/requirements.txt
RUN conda run -n chap2 python -m ipykernel install --name chap2 --user

FROM base as chap3
RUN ls -d -1 */  | grep -v -e Chapter03 | xargs rm -rf
RUN conda create -n chap3 python=3.8
RUN conda run -n chap3 pip install -r Chapter03/requirements.txt
RUN conda run -n chap3 python -m ipykernel install --name chap3 --user

FROM base as chap4
RUN ls -d -1 */  | grep -v -e Chapter04 | xargs rm -rf
RUN conda create -n chap4 python=3.8
RUN conda run -n chap4 pip install -r Chapter04/requirements.txt
RUN conda run -n chap4 python -m ipykernel install --name chap4 --user

FROM base as chap5
RUN ls -d -1 */  | grep -v -e Chapter05 | xargs rm -rf
RUN conda create -n chap5 python=3.8
RUN conda run -n chap5 pip install -r Chapter05/requirements.txt
RUN conda run -n chap5 python -m ipykernel install --name chap5 --user

FROM base as chap6
RUN ls -d -1 */  | grep -v -e Chapter06 | xargs rm -rf
RUN conda create -n chap6 python=3.8
RUN conda run -n chap6 pip install -r Chapter06/requirements.txt
RUN conda run -n chap6 python -m ipykernel install --name chap6 --user

FROM base as chap7
RUN ls -d -1 */  | grep -v -e Chapter07 | xargs rm -rf
RUN conda create -n chap7 python=3.8
RUN conda run -n chap7 pip install -r Chapter07/requirements.txt
RUN conda run -n chap7 python -m ipykernel install --name chap7 --user

FROM base as chap8
RUN ls -d -1 */  | grep -v -e Chapter08 | xargs rm -rf
RUN conda create -n chap8 python=3.8
RUN conda run -n chap8 pip install -r Chapter08/requirements.txt
RUN conda run -n chap8 python -m ipykernel install --name chap8 --user

FROM base as chap9
RUN ls -d -1 */  | grep -v -e Chapter09 | xargs rm -rf
RUN conda create -n chap9 python=3.8
RUN conda run -n chap9 pip install -r Chapter09/requirements.txt
RUN conda run -n chap9 python -m ipykernel install --name chap9 --user

FROM base as chap10
RUN ls -d -1 */  | grep -v -e Chapter10 | xargs rm -rf
RUN conda create -n chap10 python=3.10
RUN conda run -n chap10 pip install -r Chapter10/requirements.txt
RUN conda run -n chap10 python -m ipykernel install --name chap10 --user

FROM base as chap12
RUN ls -d -1 */  | grep -v -e Chapter12 | xargs rm -rf
RUN conda create -n chap12 python=3.10
RUN conda run -n chap12 pip install -r Chapter12/requirements.txt
RUN conda run -n chap12 python -m ipykernel install --name chap12 --user
# RUN /bin/bash ./Chapter12/setup_ollama.sh
