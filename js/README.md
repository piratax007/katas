# How to use this template

This template use mocha or jest test framework into a docker container. In that way, if you have a docker installation in your
machine, you don't need to have a node installation to run test over your JS code.

1. Clone or download this repository.
2. Into the `js` directory, make a new directory to each one JS kata.
3. Copy into the made directory from the last step, the two files that have into the `mocha_template` directory. Do the same
   when you use jest using the files from `jest_template`.
4. Use the `Makefile` to prepare the framework test and run the tests.
   1. Run: `make create-mocha-image` if you will use mocha test framework or `make create-jest-image` if you will use jest
   test framework - this command will create the docker image and will install all the stuff needed. You can find pre-build
   images in [here](https://hub.docker.com/repositories/piratax007dockerhub).
   2. Run (each time that you want to run the tests): `make mocha-test KATA_DIRECTORY=kata-directory`, or `make jest-test KATA_DIRECTORY=kata-directory`

**Notes:** 
- All these commands must be executed from the `js` directory.
- Full documentation for mocha can be found [here](https://mochajs.org/).
- The `test.js` file is prepared to use the assert, assertion style from `chai`, can you find how to set another
assertion style [here](https://www.chaijs.com/guide/styles/), and the complete API reference for `assert style` [here](https://www.chaijs.com/api/assert/).
- Full documentation for jest can be found [here](https://jestjs.io/).
