import platform
import sys

from config import settings


def create_allure_environment_file():
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]# список с {key}={value} в единой строке
    items.append(f'os_info={platform.system()}, {platform.release()}')# добавление версии ос
    items.append(f'python_version={sys.version}')# добавление версии системы(python)

    properties = '\n'.join(items)# перенос по строкам

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)# запись переменных в файл