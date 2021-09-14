#!/bin/bash
cd ../
ansible-galaxy init --role-skeleton=ansible-docker-skeleton ${1}
rm ./${1}/initRole.sh