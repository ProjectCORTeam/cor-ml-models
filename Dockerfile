FROM python:3.7.5

ARG BUIILD_PACKAGES="emacs wget bzip2 unzip make gcc g++ git"

RUN apt-get update && \
  apt-get install -y $BUIILD_PACKAGES && \
  rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip


COPY . /code
WORKDIR /code


RUN pip install -e .

RUN python -m nltk.downloader stopwords



ENV PYTHONPATH /code

ENTRYPOINT ["/code/docker_entrypoint.sh"]
