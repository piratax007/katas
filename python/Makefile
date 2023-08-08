KATA_DIRECTORY=$1
JUPYTER_NOTEBOOK=jupyter

create-jupyter-image:
	docker build -t jupyter-minimal:latest $(PWD)/$(JUPYTER_NOTEBOOK)

jupyter-run:
	docker run --rm -p 8888:8888 -v $(PWD)/$(KATA_DIRECTORY):/home/jovyan/src -t jupyter-minimal:latest

