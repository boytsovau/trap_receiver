[![Python 3.6.8](https://img.shields.io/badge/python-3.6.8-green.svg)](https://www.python.org/downloads/release/python-368/)
[![Python 3.11.9](https://img.shields.io/badge/python-3.11.9-green.svg)](https://www.python.org/downloads/release/python-3119/)
[![Maintainability](https://api.codeclimate.com/v1/badges/2d24a43fd107c7c9f694/maintainability)](https://codeclimate.com/github/boytsovau/trap_receiver/maintainability)

# SNMP Trap Receiver с уведомлениями по электронной почте

Этот проект представляет собой SNMP Trap Receiver, написанный на Python. Приложение слушает входящие SNMP Traps, обрабатывает их и отправляет уведомления по электронной почте на основе конкретных значений OID, указанных в конфигурации JSON. Все настройки, такие как отслеживаемые OID и получатели уведомлений, задаются в одном файле конфигурации.

## Возможности

- **Прием SNMP Traps:** Приложение прослушивает SNMP Traps на указанном порту.
- **Уведомления по OID:** Отправка уведомлений по электронной почте при получении определенных OID.
- **Настройка через JSON:** Настраиваемые OID и получатели уведомлений задаются в файлах JSON.
- **Логирование и отладка:** Вся информация о работе приложения, включая отправку писем и ошибки, записывается в лог-файл.

## Требования

- Python 3.x
- Необходимые Python модули:
  - `smtplib`
  - `json`
  - `logging`
  - `pysnmp`

## Установка

1. Клонируйте репозиторий или скачайте исходный код.
2. Убедитесь, что у вас установлен Python 3.x.
3. Разверните виртуальное окружение 
```bash
    python3 -m venv venv
```
4. Активируйте вирутальное окружение
```bash
    source venv/bin/activate
```
5. Установите необходимые зависимости (если требуются дополнительные модули).

## Конфигурация

### Конфигурация JSON

В проекте используются два файла JSON для настройки:

1. **notification_rules.json** — содержит OID, при получении которых будут отправляться уведомления.
2. **recipients.json** — содержит список получателей уведомлений.

Вы можете сами редактировать уровни оповещний, просто добавив новые значения и получателей.

### Пример `notification_rules.json`

```json
{
    "notifications": [
        {
            "oid": "1.3.6.1.4.1.2011.5.25.123.1.28.8.0",
            "description": "TEST",
            "email_subject": "TEST",
            "sensitivity": "critical"
        }
    ]
}
```

### Пример `recipients.json`

```json
{
    "critical": ["admin@example.com", "support@example.com"],
    "info": ["admin@example.com", "support@example.com"]
}
```

 ### Запуск

 ```bash
    python3 main.py
```
В основной конфигурации можете использовать любой порт, можно также использовать стандартный 162, но тогда необходимо убедиться, что он не используется. Возможно, если вы будете использовать порт 162, то потребуются права Администратора для запуска.

```python

        config.addTransport(
            snmpEngine,
            udp.domainName,
            udp.UdpTransport().openServerMode(('0.0.0.0', 162))
        )

```

### Запуск скрипта как сервис.

1. Создайте файл traplog.service
```bash
touch traplog.service
```
2. Пропишите следующие настройки в данный файл:
```bash
[Unit]
Description=traplog
After=multi-user.arget

[Service]
User=root
Group=root
Type=simple
ExecStart=/home/ВАШ_USERNAME/trap_receiver/venv/bin/python /home/ВАШ_USERNAME/trap_receiver/main2.py
WorkingDirectory=/home/ВАШ_USERNAME/trap_receiver/
Restart=always

[Install]
WantedBy=multi-user.target

```

3. Скопиируйте и запустите сервис

```bash
cp traplog.service /etc/systemd/system
sudo systemctl enable whois.service
sudo systemctl restart whois.service
```