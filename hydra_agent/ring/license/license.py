from hydra_agent.ring import Ring


class LicenseManager(Ring):
    def __init__(self):
        pass

    """Получение лицензии из Центра лицензирования. Если параметр "pin" не установлен, то команда будет ожидать пользовательского ввода.
    
        Описание параметров:
        --apartment <значение>
            Квартира/офис.
        --building <значение>
            Корпус/строение/секция.
        --company <значение>
            Наименование огранизации.
        --country <значение>
            Обязательный параметр Наименование страны.
        --district <значение>
            Наименование района.
        --email <значение>
            Адрес электронной почты пользователя.
        --first-name <значение>
            Имя пользователя.
        --house <значение>
            Номер дома/квартала/владения.
        --last-name <значение>
            Фамилия пользователя.
        --middle-name <значение>
            Отчество пользователя.
        --path <значение>
            Путь к файлам лицензий.
        --pin <значение>
            Пин-код. Если не указано, будет ожидаться ввод пин-кода.
        --previous-pin <значение>
            Старый пин-код. Требуется для повторной регистрации лицензии.
        --region <значение>
            Наименование области/республики/края/штата.
        --serial <значение>
            Обязательный параметр Регистрационный номер.
        --street <значение>
            Обязательный параметр Наименование улицы.
        --town <значение>
            Обязательный параметр Наименование города.
        --validate <значение>
            Задает необходимо ли проверять корректность данных об устройствах, получаемых от системы. По умолчанию данные не проверяются.
        --zip-code <значение>
            Обязательный параметр Почтовый индекс.
    """

    def activate(self, parameters):
        pass

    """ring license get <параметры>
    Получение файла лицензии.

    Описание параметров:
    --license <значение>
        Путь к файлу лицензии.
    --name <значение>
        Обязательный параметр Наименование лицензии.
    --path <значение>
        Путь к файлам лицензий."""
    def get(self, name, path="", dir=""):
        pass

    """ring license info <параметры>
    Получение информации о лицензии. Если параметр "name" не установлен, то команда будет ожидать пользовательского ввода.

    Описание параметров:
    --name <значение>
        Наименование лицензии. Если не указано, будет ожидаться содержимое лицензии.
    --path <значение>
        Путь к файлам лицензий."""

    def info(self, name, path):
        pass

    """ring license list <параметры>
    Список установленных лицензий.

    Описание параметров:
    --path <значение>
        Путь к файлам лицензий."""

    def list(self, path=""):
        pass

    """ring license put <параметры>
    Добавление файла лицензии. Если параметр "license" не установлен, то команда будет ожидать пользовательского ввода.

    Описание параметров:
    --license <значение>
        Путь к файлу лицензии. Если не указано, будет ожидаться содержимое лицензии.
    --path <значение>
        Путь к файлам лицензий."""

    def put(self, parameters):
        pass

    """ring license remove <параметры>
        Удаление лицензии.
    
        Описание параметров:
        --all <значение>
            Удалить все лицензии по указанному имени.
        --name <значение>
            Обязательный параметр Наименование лицензии.
        --path <значение>
            Путь к файлам лицензий."""

    def remove(self, parameters):
        pass

    """ring license validate <параметры>
        Проверка лицензии. Если параметр "name" не установлен, то команда будет ожидать пользовательского ввода.
    
        Описание параметров:
        --name <значение>
            Наименование лицензии. Если не указано, будет ожидаться содержимое лицензии.
        --path <значение>
            Путь к файлам лицензий."""

    def validate(self, parameters):
        pass