- [About](#about)
- [Installation](#installation)
- [How to setup](#how-to-setup)
- [Variables and Defaults](#variables-and-defaults)
  - [Variables](#variables)
  - [Defaults](#defaults)

# About

This role skeleton role can be used to deploy and remove Docker containers using the Ansible docker-compose module. Additionally, these containers can optionally be added to [PiHole](https://github.com/pi-hole/pi-hole), [SWAG](https://github.com/linuxserver/docker-swag), and [SUI](https://github.com/jeroenpardon/sui). 

# Installation

1. Clone this repository or install using Ansible galaxy
2. Create a new role using this role as skeleton: `ansible-galaxy init --role-skeleton=ansible-docker-skeleton NEW_ROLE` (both parameters relative to current directory)
  alternatively you could use the `initRole.sh` script with the NEW_ROLE name as parameter: `initRole.sh NEW_ROLE`. The NEW_ROLE will be created in the parent directory of the `ansible-docker-skeleton` role

# How to setup

1. First install the role as instructed under [installation](#installation)
2. Add `docker-compose.yml` to `NEW_ROLE/templates`
3. Fill in the variables: `NEW_ROLE/vars/main.yml`
4. If applicable, add a `swag-template.conf` to `NEW_ROLE/templates`
5. Include the NEW_ROLE in a playbook.

# Variables and Defaults

## Variables

Variables have not been prefilled.
For variables see: `vars/main.yml`

## Defaults

Defaults have been prefilled.

For defaults see: `defaults/main.yml`

