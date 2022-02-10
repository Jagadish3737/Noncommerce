import configparser

config= configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url= config.get('comman info', 'baseURL')
        return url


    @staticmethod
    def getUseremail():
        username = config.get('comman info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('comman info', 'password')
        return password

