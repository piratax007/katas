KATA_DIRECTORY=$1
JUPYTER_NOTEBOOK=jupyter
JUPYTER_PANDAS_NUMPY=jupyter_pandas_numpy

create-jupyter-image:
	docker build -t jupyter-minimal:latest $(PWD)/$(JUPYTER_NOTEBOOK)

create-pandas-numpy-image:
	docker build -t jupyter-pandas:latest $(PWD)/$(JUPYTER_PANDAS_NUMPY)

jupyter-minimal-run:
	docker run --rm -p 8888:8888 -v $(PWD)/$(KATA_DIRECTORY):/home/jovyan/src -t jupyter-minimal:latest

jupyter-pandas-numpy-run:
	docker run --rm -p 8888:8888 -v $(PWD)/$(KATA_DIRECTORY):/home/jovyan/src -t jupyter-pandas:latest
