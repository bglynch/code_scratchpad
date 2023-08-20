# Dockerfile

---

### What is a Dockerfile?

- a text file that contains all commands, **in order,** needed to build a given image

### What is a Docker Image?

- Docker image consists of read-only layers each of which represents a Dockerfile instruction
- The layers are stacked and each one is a delta of the changes from the previous layer

---

## Best Practices for writing Dockerfiles

- use `.dockerignore` file to exclude file from the build

- use multi-stage builds

- minimize number of layers

  - Only the instructions `RUN`, `COPY`, `ADD` create layers

- sort multiline arguements

  - ```dockerfile
    RUN apt-get update && apt-get install -y \
      bzr \
      cvs \
      git \
      mercurial \
      subversion \
      && rm -rf /var/lib/apt/lists/*
    ```

- leverage build cache

  - Once the cache is invalidated, all subsequent `Dockerfile` commands generate new images and the cache is not used.

#### Example `Dockerfile`

> ```dockerfile
> # syntax=docker/dockerfile:1
> FROM ubuntu:18.04          # creates a layer from the ubuntu:18.04 Docker image
> COPY . /app                # adds files from your Docker client’s current directory 
> RUN make /app              # builds your application with `make`
> CMD python /app/app.py     # specifies what command to run within the container
> ```
>
> 

## Commands

#### `ADD`/ `COPY`

> - Similar commands but `COPY` is preferred 
> - If you have multiple `Dockerfile` steps that use different files from your context, `COPY` them individually, rather than all at once
> - ensures that each step’s build cache is only invalidated if the specifically required files change
>
> ```dockerfile
> COPY requirements.txt /tmp/
> RUN pip install --requirement /tmp/requirements.txt
> COPY . /tmp/
> ```
>
> #### fetch packages from remote URLs
>
> ```dockerfile
> # BAD
> ADD https://example.com/big.tar.xz /usr/src/things/
> RUN tar -xJf /usr/src/things/big.tar.xz -C /usr/src/things
> RUN make -C /usr/src/things all
> ```
>
> ```dockerfile
> # GOOD
> RUN mkdir -p /usr/src/things \
>     && curl -SL https://example.com/big.tar.xz \
>     | tar -xJC /usr/src/things \
>     && make -C /usr/src/things all
> ```

#### `RUN`

> - will execute any commands in a new layer on top of the current image and commit the results
> - 2 types of Run commands
>   - `shell form`:  `RUN <command>`
>   - `exec form`: `RUN ["executable", "param1", "param2"]`
>
> ###### Shell form
>
> ```bash
> RUN /bin/bash -c 'source $HOME/.bashrc; echo $HOME'
> # or split up lines using '\'
> RUN /bin/bash -c 'source $HOME/.bashrc; \
> echo $HOME'
> ```
>
> ###### exec Form
>
> - *exec* form is parsed as a JSON array, which means that you **must use double-quotes** (“)
>
> ```bash
> RUN ["/bin/bash", "-c", "echo hello"]
> ```

#### `CMD`

> - There can only be **one `CMD` instruction** in a `Dockerfile`
> - Has 3 forms
>   - **exec form (preferred)**: `CMD ["executable","param1","param2"]`
>   - **default parameters to ENTRYPOINT**: `CMD ["param1","param2"]`
>   - **shell form:** `CMD command param1 param2`
>
> ###### shell form
>
> ```dockerfile
> FROM ubuntu
> CMD echo "This is a test." | wc -
> ```
>
> ###### exec form
>
> ```dockerfile
> FROM ubuntu
> CMD ["/usr/bin/wc","--help"]
> ```
>
> Do not confuse `RUN` with `CMD`. `RUN` actually runs a command and commits the result;
>  `CMD` does not execute anything at build time, but specifies the intended command for the image.

#### `WORKDIR`

> - instruction sets the working directory for any `RUN`, `CMD`, `ENTRYPOINT`, `COPY` and `ADD` instructions that follow it
> - can be used multiple times in a `Dockerfile`
>
> ```
> WORKDIR /path/to/workdir
> ```

#### `ARG`

> - defines a variable that users can pass at build-time to the builder with the `docker build`
>   - `--build-arg <varname>=<value>`
> - Dockerfile can have 1 or more `ARG` instructions
> - `ARG` can have a default value
>
> ###### basic
>
> ```
> ARG <name>[=<default value>]
> ```
>
> ###### default values
>
> ```dockerfile
> FROM busybox
> ARG user1=someuser
> ARG buildno=1
> # ...
> ```
>
> ```bash
> docker build --build-arg user=what_user .   # overwrite default for 'user' at build time
> ```



---

## Example: Basic Flask Python App

#### Existing Flask App

> ###### Directory structure
>
> ```
> ├── venv
> ├── app.py
> └── requirements.txt
> ```
>
> ###### app.py contents
>
> ```python
> from flask import Flask
> app = Flask(__name__)
> 
> @app.route('/')
> def hello_world():
>     return 'Hello, Docker!'
> ```
>
> ###### run the app
>
> ```bash
> python3 -m flask run
> ```

#### Create Dockerfile

> ###### Directory. Structure
>
> ```bash
> python-docker
> ├── venv
> ├── app.py
> ├── Dockerfile          # Dockerfile added
> └── requirements.txt          
> ```
>
> ###### Dockerfile
>
> ```dockerfile
> # syntax=docker/dockerfile:1
> FROM python:3.8-slim-buster
> 
> WORKDIR /app
> 
> # install dependencies
> COPY requirements.txt requirements.txt
> RUN pip3 install -r requirements.txt
> 
> # add source code
> COPY . .
> 
> # run the app
> CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
> ```
> 
>###### Build the Image
> 
>```bash
> docker build --tag python-docker .
> ```
> 
>###### Run Image in a Container
> 
>```bash
> # flask runs on port 5000 by default
> docker run --publish 8000:5000 python-docker
> ```



---

## Links

#### Official Docker Docs

- [Guide Get Started](https://docs.docker.com/get-started/)

- [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)

- [Build context](https://docs.docker.com/build/building/context/)

- [`.dockerignore` file](https://docs.docker.com/engine/reference/builder/#dockerignore-file)

- [Python Guide](https://docs.docker.com/language/python/)

  