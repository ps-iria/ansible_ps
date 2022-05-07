# Домашнее задание к занятию "08.02 Работа с Playbook"

## Подготовка к выполнению

1. Создайте свой собственный (или используйте старый) публичный репозиторий на github с произвольным именем.
2. Скачайте [playbook](./playbook/) из репозитория с домашним заданием и перенесите его в свой репозиторий.
3. Подготовьте хосты в соответствии с группами из предподготовленного playbook.

## Основная часть

1. Приготовьте свой собственный inventory файл `prod.yml`.
2. Допишите playbook: нужно сделать ещё один play, который устанавливает и настраивает [vector](https://vector.dev).
3. При создании tasks рекомендую использовать модули: `get_url`, `template`, `unarchive`, `file`.
4. Tasks должны: скачать нужной версии дистрибутив, выполнить распаковку в выбранную директорию, установить vector.
```text
sh-4.2# echo 'Hello world!' | vector
2022-05-07T08:47:03.080863Z  INFO vector::app: Log level is enabled. level="vector=info,codec=info,vrl=info,file_source=info,tower_limit=trace,rdkafka=info,buffers=info,kube=info"
2022-05-07T08:47:03.080986Z  INFO vector::app: Loading configs. paths=["/etc/vector/vector.toml"]
2022-05-07T08:47:03.082972Z  INFO vector::topology::running: Running healthchecks.
2022-05-07T08:47:03.083047Z  INFO vector::topology::builder: Healthcheck: Passed.
2022-05-07T08:47:03.083154Z  INFO vector: Vector has started. debug="false" version="0.21.2" arch="x86_64" build_id="1f01009 2022-05-05"
2022-05-07T08:47:03.083217Z  INFO vector::app: API is disabled, enable by setting `api.enabled` to `true` and use commands like `vector top`.
2022-05-07T08:47:03.085009Z  INFO vector::sources::stdin: Capturing STDIN.
2022-05-07T08:47:03.085215Z  INFO vector::shutdown: All sources have finished.
2022-05-07T08:47:03.085243Z  INFO vector: Vector has stopped.
2022-05-07T08:47:03.085233Z  INFO source{component_kind="source" component_id=in component_type=stdin component_name=in}: vector::sources::stdin: Finished sending.
Hello world!
```
5. Запустите `ansible-lint site.yml` и исправьте ошибки, если они есть.
```text
Ошибок нет
```
6. Попробуйте запустить playbook на этом окружении с флагом `--check`.
7. Запустите playbook на `prod.yml` окружении с флагом `--diff`. Убедитесь, что изменения на системе произведены.
8. Повторно запустите playbook с флагом `--diff` и убедитесь, что playbook идемпотентен.
9. Подготовьте README.md файл по своему playbook. В нём должно быть описано: что делает playbook, какие у него есть параметры и теги.
10. Готовый playbook выложите в свой репозиторий, поставьте тег `08-ansible-02-playbook` на фиксирующий коммит, в ответ предоставьте ссылку на него.

---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
