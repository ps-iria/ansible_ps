#!/usr/bin/env bash

docker-compose up -d
ansible-playbook playbook/site.yml -i playbook/inventory/prod.yml --vault-password-file /home/ansible_vault_pass
docker-compose stop