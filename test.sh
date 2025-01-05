#!/bin/bash

set -e
MIN_COVERAGE_PERCENTAGE=80
coverage run manage.py test
coverage report --fail-under=${MIN_COVERAGE_PERCENTAGE}
