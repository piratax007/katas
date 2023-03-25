KATA_DIRECTORY=$1

default: create-image

create-image:
	docker build -t js-katas -f Dockerfile .

mocha: create-image
	docker run -d --rm -v $(PWD)/$(KATA_DIRECTORY):/root/src -t js-katas npm install mocha chai

test:
	docker run --rm -v $(PWD)/$(KATA_DIRECTORY):/root/src -t js-katas npm test

clean:
	docker run -d --rm -v $(PWD)/$(KATA_DIRECTORY):/root/src -t js-katas rm -r node_modules package-lock.json
