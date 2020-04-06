# skillfactory_rds

## Run Jupyter Notebook via docker
Display a list of available images
```console
docker search continuumio
```

Download Anaconda3 image
```console
docker pull continuumio/anaconda3
```

Run container with Jupyter Notebook
```console
docker run -i -t -p 8888:8888 continuumio/anaconda3 /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet && mkdir /opt/notebooks && /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser --allow-root"
```

To access the Jupyter Notebook open http://localhost:8888/?token=1e26ffc7b9... in your browser.
Url with token you can find in docker ouptput.

## Unit 0

```console
$ python unit_0/app.py
Алгоритм <function game_core_v1 at 0x104c4af28> угадывает число в среднем за 101 попыток
Алгоритм <function game_core_v2 at 0x104e9e6a8> угадывает число в среднем за 33 попыток
Алгоритм <function game_core_v3 at 0x10bf5ae18> угадывает число в среднем за 5 попыток
```
