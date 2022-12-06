# 百度网盘自动补档

## 简介
自动检测百度网盘分享是否过期，并自动新建分享，密码与原来相同   

---
## 功能
- [x] 获取个人信息
- [x] 获取分享列表
- [x] 获取分享密码
- [x] 重新分享已有的分享
- [x] 取消分享
- [x] 获取一个文件的分享，从该链接获取的分享永远有效
- [x] 定时扫描已有分享，重新分享过期的分享
- [x] 推送分享结果到wechat等

**如果您需要别的功能，请提交issue并附带描述。**  
**如果本程序对您有帮助，欢迎star。**  

---
## 运行
1. 克隆本项目
2. 运行前端  
    `cd front`  
    `npm install`  
    `npm run dev`  

3. 构建前端  
    `npm run build`  

4. 运行go后端  
    `go mod tidy`  
    `go run main.go`   

5. 构建go后端  
    `go build`  

6. 运行python3后端  
    `cd py-backend`  
    `pip install -r requirements.txt`  
    `python main.py`  
    请确保你拥有python3环境  


运行截图  

![运行截图](/img/运行截图.png)

**访问后端时，请先构建出前端代码，否则会404，因为后端使用的资源文件是前端构建的路径**  


---

## 配置文件
1. 服务器配置  
`server.host` 监听主机，本机为`127.0.0.1`，任意主机为`0.0.0.0`  
`server.port` 监听端口  
2. 自动补档配置  
`reshare.enable` 是否开启自动扫描  
`reshare.ignore` 忽略的分享id  
`reshare.interval` 扫描间隔，单位秒  
`reshare.errorretry` 重新分享时，如果出现错误，该分享id冷却时间，单位秒  
3. 百度云cookie  
`baidu.cookie` 百度云盘的cookie，如果为空则会尝试从环境变量中取`BAIDU_COOKIE`
4. 通知  
`notify.enable` 是否启用通知, true or false  
`notify.cron` 执行通知cron表达式, 可以参考`https://cron.qqe2.com/`  
server酱通知 `https://sct.ftqq.com/`  
`notify.sct.enable` 是否启用server酱通知, true or false  
`notify.sct.key` server酱的key, 如果为空则会尝试从环境变量中取`SCT_KEY`  
`notify.sct.channel` 推送的channel  
push-plus通知 `https://www.pushplus.plus/`  
`notify.push-plus.enable` 是否启用push-plus通知, true or false  
`notify.push-plus.toke` push-plus的token, 如果为空则会尝试从环境变量中取`PUSH_PLUS_TOKEN`  
`notify.push-plus.channel` 推送的channel  

---
## 接口
   `/sharefiles`           获取分享列表  
   `/userinfo`             获取个人信息  
   `/getpwd/:shareid`      获取分享的密码，需要传递分享id(`:shareid` 替换为分享id)  
   `/reshare/:shareid`     重新分享一个分享，需要传递分享id(`:shareid` 替换为分享id)    
   `/cancelshare/:shareid` 取消一个分享，需要传递分享id(`:shareid` 替换为分享id)    
   `/getfileshare/:fsid`   获取一个文件的分享，从该接口获取的分享永远有效，需要传递文件id(`:fsid` 替换为文件id)    

---
## 讨论
有任何问题请提交issue，并附带相关信息。

---
## 许可
Colorful 是在 AGPL-3.0 许可下许可的开源软件。

---
## 免责声明
- 本程序为免费开源项目，旨在分享网盘文件，方便下载以及学习Golang，使用时请遵守相关法律法规，请勿滥用；
- 本程序通过调用官方sdk/接口实现，无破坏官方接口行为；
- 本程序不拦截、存储、篡改任何用户数据；
- 在使用本程序之前，您应了解并承担相应的风险，包括但不限于账号被ban，下载限速等，与本程序无关；
- 如有侵权，请通过[邮件](1171866049@qq.com)与我联系，会及时处理。