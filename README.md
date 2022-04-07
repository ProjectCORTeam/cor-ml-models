# cor-ml-models
A custom package to handle ML models


## Requirements
 - Python >= 3.7.0
 - Any flavour of Conda. We recommend [Miniconda](https://docs.conda.io/en/latest/miniconda.html). 
 - A version Docker on your OS.
 
## Local Set up

Generate the Conda environment and install all the dependencies.
```
conda create -n <environment name> python=3.7
```

```
conda activate <environment name>
```

```
pip install -e .
```

Additionally, you have to download NTLK corpus by using the command:

```
python -m nltk.downloader stopwords
```


## Build Docker image

```
./tools/build.sh
```

By default, the build script will create a image called **`cor-categorization:dev`**.


Use the optional flags **`--image`** and **`--tag`** for further options.
**`--help`** will print the command explanation.

For Example
```
./tools/build.sh --image cor-categorization --tag dev
```

Alternatively you can set the environment variable **`DOCKER_IMAGE_TAG`** to set the image tag.

```
export DOCKER_IMAGE_TAG=latest
./tools/build.sh
```
This will generate the image **`cor-categorization:latest`**


## Navigate and run the Docker image

### `For Development and testing`


To run the docker app, please do:

```
docker run --entrypoint /code/docker_entrypoint.sh -it cor-categorization:dev /bin/bash
```

Inside Docker, try installing `ipython`  (`pip install ipython`) and check the following import statement:

```
from categorization.models.sklearn.sk_models import Categorizer
```