all: test

#: interpreter version (ex.: 3.6) or use all current available
PYTHON ?= __all_available__

OPEN = $(shell which kde-open || which xdg-open || which gnome-open || which open)

# -- Tests --------------------------------------------------------------------

TEST_COMMAND = tox --recreate
ifeq "$(PYTHON)" "__all_available__"
	TEST_COMMAND += --skip-missing-interpreters
else
	TEST_COMMAND += -e py$(PYTHON)
endif

# -- Tests --------------------------------------------------------------------

.PHONY: test
test:
	$(TEST_COMMAND)

# -- Builds -------------------------------------------------------------------

.PHONY: build_dist
build_dist: clean_dist
	pip wheel --wheel-dir dist/ .[dist]
	python setup.py --version > dist/__version__

# -- Installs -----------------------------------------------------------------

.PHONY: install
install:
	pip install --upgrade .

.PHONY: install_dev
install_dev:
	pip install --upgrade --editable .[develop,testing,dist]

.PHONY: _check_dist
_check_dist:
	test -d dist/ || ( \
		echo -e "\n--> [!] run 'make build_dist' before!\n" && exit 1 \
	)

.PHONY: install_dist
install_dist: _check_dist
	pip install --no-index --no-cache-dir --find-links=dist/ \
	    --upgrade --force-reinstall \
	    online_market[dist]==$(shell cat dist/__version__)


# -- Cleans -------------------------------------------------------------------

.PHONY: clean
clean: clean_dist clean_build clean_images

.PHONY: clean_dist
clean_dist:
	-rm -rv dist/

.PHONY: clean_build
clean_build:
	-rm -rv build/

.PHONY: clean_images
clean_images:
	- docker ps -a | grep online_market | awk '{print $$1}' | \
	 xargs --no-run-if-empty docker rm
	- docker images | grep online_market | awk '{print $$1":"$$2}' | \
	 xargs --no-run-if-empty docker rmi
