import configparser
import os


class Tools:

    @staticmethod
    def create_config_file(path):

        config = """
            [window] \n
            width=600 \n
            height=800 \n
            fps = 30 \n   
            """

        with open(path, 'a+') as file:
            file.write(config)

    @staticmethod
    def check_files(file_name_list):
        return [file for file in file_name_list if not os.path.isfile('images/' + file)]

    @staticmethod
    def get_config(config_file_path='config.ini'):
        if not os.path.exists(config_file_path):
            Tools.create_config_file(os.getcwd())
        config = configparser.ConfigParser()
        config.read(config_file_path)
        return config
