# Docker image

In order to ensure reproducibility and an environment ready to be used to test the examples from the different chapters, we provide a Docker image with several Python environments already installed, corresponding to the dependencies set of the different chapters.

The dependencies sets of the different chapters are handled using [Poetry](https://python-poetry.org/) to both provide an easy way to manage dependencies updates as well as produce pinned `requirements.txt` files representing the entire environment. In fact, in the first version of the book, we realized that transitive dependendencies of some of the packages we used, when not explicitely pinned, could break the installation process.

## Usage

### Build the images

To build the image from this local directory, run the following command

```bash
$ docker build . -t graph-machine-learning:latest --no-cache
```

### Run the image

We generally recommend to create a local directory where to store data, results and images

```bash 
$ mkdir data
```

Then, use the following command

```bash
$ docker run --rm \
  	 -p <port>:8888 \
	 -v "$(pwd)/data:/data"  \
	 --name graph-machine-learning-box \
	 graph-machine-learning:latest
```

to start the image. Please make sure that the data folder can be written by the Docker image. We suggest to use the default port 8888 for the `<port>`. This will start a Jupyter server which should be locally accessible at `[http://localhost:8888](http://localhost:8888)` (or change the port accordingly). 

## For Developers

Make sure that in your system, [Poetry]((https://python-poetry.org/) is correctly installed and configured, use the following command to verify this

```bash
$ poetry --version
```

### Update Dependencies

Dependencies may need to be updated, when:

* **Adding new packages**
New dependencies can be added directly using Poetry with the following command
```bash
$ poetry add <package>
```
This should modify the `pyproject.toml` file with the new dependency. 

* **Update dependent packages to new release**
```bash
$ poetry update
```

Both these action will create a new `poetry.lock` file. 

Once the `poetry.lock` file is updated, we can then export a new `requirements.txt` file using

```bash
$ poetry export -f requirements.txt --output requirements.txt --without-hashes
```

### Testing

In order to make sure that the docker image is fully working, we provide a Bash script to run through all the notebooks of the image, and provide a summary of successful/failing notebooks.

Before running the tests, make sure the image is running with the `graph-machine-learning-box` name attached to it (see section *Usage* above).

To run the tests, use

```bash 
./tests.sh
```

In order to run tests only for particular chapters, provide the name of the chapters as extra arguments, e.g. 

```bash 
./tests.sh Chapter01 Chapter02
```

Needless to say, we expect all of the notebooks to properly run.

