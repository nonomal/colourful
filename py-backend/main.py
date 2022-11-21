import atexit
import os

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template, send_from_directory, jsonify

from config import Config
from baidu_storage import BaiduStorage

conf = Config()

template_folder = os.path.abspath('./../front/dist')
static_folder = os.path.abspath('./../front/dist/assets')
app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)
baidu = BaiduStorage(conf.baidu.cookie)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/favicon.png')
def favicon():
    return send_from_directory(app.template_folder, 'favicon.png')


@app.route('/api/sharefiles', methods=['GET'])
def share_files():
    return jsonify(baidu.share_files())


@app.route('/api/userinfo', methods=['GET'])
def user_info():
    return jsonify(baidu.user_info())


@app.route('/api/getpwd/<int:shareid>', methods=['GET'])
def get_pwd(shareid):
    return jsonify(baidu.get_passwd(shareid))


@app.route('/api/reshare/<int:shareid>', methods=['GET'])
def re_share(shareid):
    data, _ = baidu.re_share(shareid)
    return jsonify(data)


@app.route('/api/cancelshare/<int:shareid>', methods=['GET'])
def cancel_share(shareid):
    return jsonify(baidu.cancel_share(shareid))


@app.route('/api/getfileshare/<int:fsid>', methods=['GET'])
def get_file_share(fsid):
    return jsonify(baidu.get_file_share(fsid))


scheduler = BackgroundScheduler()
scheduler.add_job(func=baidu.auto_reshare, args=(conf.reshare,), trigger="interval", seconds=conf.reshare.interval)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    app.run(host=conf.server.host, port=conf.server.port)
