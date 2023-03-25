# How to use this template

This template use mocha test framework into a docker container, in that way, if you have a docker installation in your
machine, you don't need to have a node installation to run test over your JS code.

1. Clone or download this repository.
2. Into the `js` directory, make a new directory to each one JS kata.
3. Copy into the maked directory in the last step, the three files that have into the `template` directory.
4. Use the `Makefile` to prepare the framework test and run the tests.
   1. Run: `make mocha KATA_DIRECTORY=kata-directory` - this command will create the docker image and will install all
      the stuff needed. Previous to this command. (in `docker pull piratax007dockerhub/js-katas` exists a prepared image.)
   2. Run (each time that you want to run the tests): `make test KATA_DIRECTORY=kata-directory`.
5. At the end of the exercise, can you clean the useless stuff running: `make clean KATA_DIRECTORY=kata-directory`.

**Notes:** 
- This template use mocha test framework, full documentation can be found [here](https://mochajs.org/).
- The `test.js` file is prepared to use the assert, assertion style from `chai`, can you find how to set another
assertion style [here](https://www.chaijs.com/guide/styles/), and the complete API reference for `assert style` [here](https://www.chaijs.com/api/assert/).
