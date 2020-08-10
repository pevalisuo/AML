#!/bin/bash

export GIT_COMMITTER_NAME=anonymous
export GIT_COMMITTER_EMAIL=anon@localhost
git clone https://github.com/pevalisuo/AML.git

pip install -r AML/requirements.txt

