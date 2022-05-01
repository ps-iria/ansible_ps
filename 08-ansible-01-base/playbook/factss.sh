#!/usr/bin/env bash

docker-compose up -d
ansible-playbook site.yml -i inventory/prod.yml --vault-password-file /home/ansible_vault_pass
docker-compose stop