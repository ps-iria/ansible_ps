# Описаное

Настройка серверов для работы Clickhouse, Lighthouse, Vector

До запуска необходимо настроить виртуальные машины, облачные(prod) или локальные(test)
и в inventory и group_vars ввести адреса серверов для продакшен-окружения

для заупуска необходимо ввести

###### для тестового окружения:
```shell script
sudo ansible-playbook site.yml -i inventory/test.yml
```
###### для продакшен-окружению:
```shell script
sudo ansible-playbook site.yml -i inventory/prod.yml
```


# GROUP VARS
clickhouse_version - используемая версия Clickhouse
clickhouse_packages - Пакеты установки Cickhouse
listen_host - Ограничение по хостам, с которых может прийти запрос

nginx_user_name - Пользователь Nginx
access_log_name - Название файла логов
lighthouse_location_dir - Папка для файлов Lighthouse
lighthouse_vcs - Гит lighthouse

vector_version - версия Vector
vector_rpm - Файл установки Vector
vector_config_dir - Папка конфигураций Vector
vector_config - Конфигурация Vector

## Описание Play 

### Install Clickhouse
 установлены тэги *clickhous*e для дальнейшего использования и отладки 
 - загрузка установочных пакетов
 - установка пакетов
 - создание бд логов
 - создание таблицы логов

 
### Install Vector
 установлены тэги *vector* для дальнейшего использования и отладки 
 - загрузка установочного пакета 
 - установка пакетов
 - копирование шаблова файла конфигурации (templates)
 
### Logging
 - Установка пакета rsyslog
 - Настройка окружения для записи логов
 
### Install Lighthouse + Nginx
 - Установка epel
 - Установка Nginx
 - Настройка Nginx по шаблону
 - Скачивание Lighthouse
 - Настройка Lighthouse по шаблону
