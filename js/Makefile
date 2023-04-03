KATA_DIRECTORY=$1
TEST_MOCHA_FRAMEWORK=mocha_test/
TEST_JEST_FRAMEWORK=jest_test/

create-mocha-image:
	docker build -t js-mocha:debian-bookworm $(PWD)/$(TEST_MOCHA_FRAMEWORK)

mocha-test:
	docker run --rm -v $(PWD)/$(KATA_DIRECTORY):/root/src/code -t js-mocha:debian-bookworm npm test

create-jest-image:
	docker build -t js-jest:alpine-latest $(PWD)/$(TEST_JEST_FRAMEWORK)

jest-test:
	docker run --rm -v $(PWD)/$(KATA_DIRECTORY):/root/src/code -t js-jest npm test