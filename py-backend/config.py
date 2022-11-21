from yaml import load, CLoader
import os


class Config:
    def __init__(self):
        try:
            data = load(open('./config.yaml'), Loader=CLoader)
        except Exception:
            data = load(open('./../config.yaml'), Loader=CLoader)
        self.server = ServerConfig(data['server'])
        self.reshare = ReshareConfig(data['reshare'])
        self.baidu = BaiduConfig(data['baidu'])


class BaiduConfig:
    def __init__(self, config):
        self.cookie = config['cookie']
        if self.cookie is None or self.cookie == '':
            self.cookie = os.environ.get('BAIDU_COOKIE')


class ServerConfig:
    def __init__(self, config):
        self.host = config['host']
        self.port = int(config['port'])


class ReshareConfig:
    def __init__(self, config):
        self.enable = config['enable']
        self.ignore = config['ignore']
        self.interval = int(config['interval'])
        self.errorretry = config['errorretry']


if __name__ == '__main__':
    c = Config()
    print(c.server.host)
    print(c.reshare.errorretry)
    print(c.baidu.cookie)
