#!/bin/bash

cd /home/user_name/mastobutler/

sed -i 's/disable_post: True/disable_post: False/g' config.yaml
sed -i 's/disable_dismiss: True/disable_dismiss: False/g' config.yaml
sed -i 's/loglevel: 10/loglevel: 20/g' config.yaml
