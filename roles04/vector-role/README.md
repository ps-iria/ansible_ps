Vector-role
=========

A brief description of the role goes here.

Requirements
------------

Для настройки необходимы установленные python и ansible

Role Variables
--------------

vector_version - версия Vector
vector_rpm - Файл установки Vector
vector_config_dir - Папка конфигураций Vector
vector_config - Конфигурация Vector

Dependencies
------------

Нет зависимостей

Example Playbook
----------------

    - hosts: vector
      roles:
         - { role: ps-iria.vector-role }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
