import os

__all__ = ['BASE_PATH', 'PROJECT_NAME', 'PROJECT_INSTANCE', 'APP_NAME']

file_path = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/').split('/')
file_path = filter(lambda s: s != '', file_path)

BASE_PATH = os.path.join('/', *file_path)
PROJECT_NAME = 'virtual_class'
PROJECT_INSTANCE = file_path[-1]
APP_NAME = 'app_' + PROJECT_INSTANCE
