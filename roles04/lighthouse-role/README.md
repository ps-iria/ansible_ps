Role Name
=========

A brief description of the role goes here.

Requirements
------------

Для настройки необходимы установленные python и ansible

Role Variables
--------------

nginx_user_name - Пользователь Nginx
access_log_name - Название файла логов
lighthouse_location_dir - Папка для файлов Lighthouse
lighthouse_vcs - Гит lighthouse

Dependencies
------------

Нет зависимостей 

Example Playbook
----------------

    - hosts: lighthouse
      roles:
         - { role: ps-iria.lighthouse-role }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
