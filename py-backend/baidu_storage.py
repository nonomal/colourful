import json

from time import strftime, localtime
import js2py
from sign import sign
import time
import requests
from util import random_string

js2py.translate_file("sign.js", "sign.py")


def sign_content(content):
    return sign.x(content)


class BaiduStorage:
    def __init__(self, cookie):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        self.cookie = cookie
        self.login_info = self._test()
        self.share_error_map = {}

    def _do_request(self, url, method, data=None):
        headers = {
            'User-Agent': self.user_agent,
            'Cookie': self.cookie
        }
        if data is not None:
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
        r = None
        if str(method).lower() == 'get':
            r = requests.get(url, headers=headers, data=data)
        elif str(method).lower() == 'post':
            r = requests.post(url, headers=headers, data=data)
        if r is None:
            raise Exception('请传入get或post请求')
        if r.status_code != 200:
            raise Exception('Error: %s' % r.status_code)
        return r.content.decode(r.encoding)

    def _test(self):
        test_url = 'https://pan.baidu.com/api/loginStatus?clienttype=0'
        data = self._do_request(test_url, 'GET')
        r = json.loads(data)
        if r['errno'] != 0:
            raise Exception(r.show_msg)
        return r

    def share_files(self):
        share_url = 'https://pan.baidu.com/share/record?num=1000&page=1&order=ctime&desc=1'
        data = self._do_request(share_url, 'GET')
        return json.loads(data)

    def user_info(self):
        return self.login_info

    def get_passwd(self, shareid):
        passwd_url = 'https://pan.baidu.com/share/surlinfoinrecord?shareid=%s&sign=%s' % (
            shareid, sign_content(str(shareid) + "_sharesurlinfo!@#"))
        data = self._do_request(passwd_url, 'GET')
        return json.loads(data)

    def re_share(self, shareid):
        pwd = random_string(4)
        pwd_info = self.get_passwd(shareid)
        if 'pwd' in pwd_info.keys():
            pwd = pwd_info['pwd']
        share_files = self.share_files()
        fs_ids = None
        for share_info in share_files['list']:
            if share_info['shareId'] == shareid:
                fs_ids = share_info['fsIds']
                break

        if fs_ids is None:
            raise Exception('未找到分享文件 %s' % shareid)
        data, _ = self._share(json.dumps(fs_ids), pwd)
        return json.loads(data), pwd

    def cancel_share(self, shareid):
        cancel_share_url = 'https://pan.baidu.com/share/cancel'
        data = self._do_request(cancel_share_url, 'POST', data={
            'shareid_list': '[%s]' % shareid
        })
        return json.loads(data)

    def get_file_share(self, fsid):
        share_id = None
        short_link = None
        expire_type = None
        typical_path = None
        find = False
        share_files = self.share_files()
        for share_info in share_files['list']:
            for i in share_info['fsIds']:
                if i == fsid:
                    share_id = share_info['shareId']
                    short_link = share_info['shortlink']
                    expire_type = share_info['expiredType']
                    typical_path = share_info['typicalPath']
                    find = True
                    break
            if find:
                break
        if typical_path == "分享的文件已被删除":
            return {'errno': -1, 'show_msg': "分享的文件已被删除"}
        if find:
            if expire_type == 0 or expire_type == 1:
                pwd = self.get_passwd(share_id)
                return {'short_url': short_link, 'pwd': pwd['pwd'], 'url': short_link + "?pwd=" + pwd['pwd'],
                        'errno': 0, "show_msg": "已有分享未过期, 获取成功"}
            elif expire_type == -1:
                data, pwd = self.re_share(share_id)
                if data['errno'] != 0:
                    return {'errno': -1, 'show_msg': data['show_msg']}
                return {'short_url': data['shorturl'], 'pwd': pwd,
                        'url': data['shorturl'] + "?pwd=" + pwd, 'errno': 0, "show_msg": "分享已过期, 重新分享成功"}
        else:
            pwd = random_string(4)
            data, pwd = self._share('[%s]' % fsid, pwd)
            r = json.loads(data)
            if r['errno'] != 0:
                return {'errno': r['errno'], 'show_msg': r['show_msg']}
            return {'short_url': r['shorturl'], 'pwd': pwd, 'url': r['shorturl'] + "?pwd=" + pwd, 'errno': 0,
                    'show_msg': "未找到已有分享, 新建分享成功"}

    def auto_reshare(self, conf):
        status_map = {1: "分享失败", 2: "暂时不可访问", 3: "分享失败", 4: "审核未通过", 19: "已被冻结"}
        msg = []
        share_files = self.share_files()
        for si in share_files['list']:
            if si['tag'] == 7:
                msg.append("分享 %s 已被屏蔽, 跳过" % si['shareId'])
                continue
            if si['status'] == 1 or si['status'] == 2 or si['status'] == 3 or si['status'] == 4 or si['status'] == 19:
                msg.append("分享 %s %s, 跳过" % (si['shareId'], status_map[si['status']]))
                continue

            if si['expiredType'] == 0 or si['expiredType'] == 1:
                msg.append("分享 %s 未过期, 跳过" % si['shareId'])
                continue

            contains = False
            for ig in conf.ignore:
                if ig == si['shareId']:
                    msg.append("分享 %s 在忽略列表中, 跳过" % si['shareId'])
                    contains = True
                    break
            if contains:
                continue

            if si['shareId'] in self.share_error_map:
                if time.time() - self.share_error_map[si['shareId']] >= conf.errorretry:
                    del self.share_error_map[si['shareId']]
                else:
                    msg.append("分享 %s 上次尝试分享失败" % si['shareId'])
                    continue
            if si['typicalPath'] == "分享的文件已被删除":
                msg.append("分享 %s 已被删除, 跳过" % si['shareId'])
                continue

            for fsid in si['fsIds']:
                fs = self.get_file_share(fsid)
                if fs['errno'] == 0:
                    msg.append("分享id: {}, 文件id: {}, {}, 新的连接: {}".format(si['shareId'], fsid, fs['show_msg'], fs['url']))
                else:
                    self.share_error_map[si['shareId']] = time.time()
                    msg.append("分享id: {}, 分享失败, 原因: {}".format(si['shareId'], fs['show_msg']))
                time.sleep(0.5)

        print(strftime('%Y-%m-%d %H:%M:%S', localtime()))
        print('\n'.join(msg))

    def _share(self, fs_ids, pwd):
        share_url = 'https://pan.baidu.com/share/set'
        data = self._do_request(share_url, 'POST', data={
            'period': '0',
            'pwd': pwd,
            'fid_list': fs_ids,
            'schannel': '4'
        })
        return data, pwd
