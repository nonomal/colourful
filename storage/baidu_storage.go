package storage

import (
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"log"
	"net/http"
	"net/url"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/gofiber/fiber/v2"
	"github.com/robertkrimen/otto"
	"github.com/xi-mad/colourful/config"
	"github.com/xi-mad/colourful/util"
)

var vm *otto.Otto

func init() {
	vm = otto.New()
	vm.Run(`
		"use strict";
		function o(e, t) {
			var n = (65535 & e) + (65535 & t)
			, i = (e >> 16) + (t >> 16) + (n >> 16);
			return i << 16 | 65535 & n
		}
		function s(e, t) {
			return e << t | e >>> 32 - t
		}
		function a(e, t, n, i, r, a) {
			return o(s(o(o(t, e), o(i, a)), r), n)
		}
		function c(e, t, n, i, r, o, s) {
			return a(t & n | ~t & i, e, t, r, o, s)
		}
		function l(e, t, n, i, r, o, s) {
			return a(t & i | n & ~i, e, t, r, o, s)
		}
		function u(e, t, n, i, r, o, s) {
			return a(t ^ n ^ i, e, t, r, o, s)
		}
		function d(e, t, n, i, r, o, s) {
			return a(n ^ (t | ~i), e, t, r, o, s)
		}
		function A(e, t) {
			var n, i, r, s, a;
			e[t >> 5] |= 128 << t % 32,
			e[14 + (t + 64 >>> 9 << 4)] = t;
			var A = 1732584193
			, f = -271733879
			, p = -1732584194
			, h = 271733878;
			for (n = 0; n < e.length; n += 16)
				i = A,
				r = f,
				s = p,
				a = h,
				A = c(A, f, p, h, e[n], 7, -680876936),
				h = c(h, A, f, p, e[n + 1], 12, -389564586),
				p = c(p, h, A, f, e[n + 2], 17, 606105819),
				f = c(f, p, h, A, e[n + 3], 22, -1044525330),
				A = c(A, f, p, h, e[n + 4], 7, -176418897),
				h = c(h, A, f, p, e[n + 5], 12, 1200080426),
				p = c(p, h, A, f, e[n + 6], 17, -1473231341),
				f = c(f, p, h, A, e[n + 7], 22, -45705983),
				A = c(A, f, p, h, e[n + 8], 7, 1770035416),
				h = c(h, A, f, p, e[n + 9], 12, -1958414417),
				p = c(p, h, A, f, e[n + 10], 17, -42063),
				f = c(f, p, h, A, e[n + 11], 22, -1990404162),
				A = c(A, f, p, h, e[n + 12], 7, 1804603682),
				h = c(h, A, f, p, e[n + 13], 12, -40341101),
				p = c(p, h, A, f, e[n + 14], 17, -1502002290),
				f = c(f, p, h, A, e[n + 15], 22, 1236535329),
				A = l(A, f, p, h, e[n + 1], 5, -165796510),
				h = l(h, A, f, p, e[n + 6], 9, -1069501632),
				p = l(p, h, A, f, e[n + 11], 14, 643717713),
				f = l(f, p, h, A, e[n], 20, -373897302),
				A = l(A, f, p, h, e[n + 5], 5, -701558691),
				h = l(h, A, f, p, e[n + 10], 9, 38016083),
				p = l(p, h, A, f, e[n + 15], 14, -660478335),
				f = l(f, p, h, A, e[n + 4], 20, -405537848),
				A = l(A, f, p, h, e[n + 9], 5, 568446438),
				h = l(h, A, f, p, e[n + 14], 9, -1019803690),
				p = l(p, h, A, f, e[n + 3], 14, -187363961),
				f = l(f, p, h, A, e[n + 8], 20, 1163531501),
				A = l(A, f, p, h, e[n + 13], 5, -1444681467),
				h = l(h, A, f, p, e[n + 2], 9, -51403784),
				p = l(p, h, A, f, e[n + 7], 14, 1735328473),
				f = l(f, p, h, A, e[n + 12], 20, -1926607734),
				A = u(A, f, p, h, e[n + 5], 4, -378558),
				h = u(h, A, f, p, e[n + 8], 11, -2022574463),
				p = u(p, h, A, f, e[n + 11], 16, 1839030562),
				f = u(f, p, h, A, e[n + 14], 23, -35309556),
				A = u(A, f, p, h, e[n + 1], 4, -1530992060),
				h = u(h, A, f, p, e[n + 4], 11, 1272893353),
				p = u(p, h, A, f, e[n + 7], 16, -155497632),
				f = u(f, p, h, A, e[n + 10], 23, -1094730640),
				A = u(A, f, p, h, e[n + 13], 4, 681279174),
				h = u(h, A, f, p, e[n], 11, -358537222),
				p = u(p, h, A, f, e[n + 3], 16, -722521979),
				f = u(f, p, h, A, e[n + 6], 23, 76029189),
				A = u(A, f, p, h, e[n + 9], 4, -640364487),
				h = u(h, A, f, p, e[n + 12], 11, -421815835),
				p = u(p, h, A, f, e[n + 15], 16, 530742520),
				f = u(f, p, h, A, e[n + 2], 23, -995338651),
				A = d(A, f, p, h, e[n], 6, -198630844),
				h = d(h, A, f, p, e[n + 7], 10, 1126891415),
				p = d(p, h, A, f, e[n + 14], 15, -1416354905),
				f = d(f, p, h, A, e[n + 5], 21, -57434055),
				A = d(A, f, p, h, e[n + 12], 6, 1700485571),
				h = d(h, A, f, p, e[n + 3], 10, -1894986606),
				p = d(p, h, A, f, e[n + 10], 15, -1051523),
				f = d(f, p, h, A, e[n + 1], 21, -2054922799),
				A = d(A, f, p, h, e[n + 8], 6, 1873313359),
				h = d(h, A, f, p, e[n + 15], 10, -30611744),
				p = d(p, h, A, f, e[n + 6], 15, -1560198380),
				f = d(f, p, h, A, e[n + 13], 21, 1309151649),
				A = d(A, f, p, h, e[n + 4], 6, -145523070),
				h = d(h, A, f, p, e[n + 11], 10, -1120210379),
				p = d(p, h, A, f, e[n + 2], 15, 718787259),
				f = d(f, p, h, A, e[n + 9], 21, -343485551),
				A = o(A, i),
				f = o(f, r),
				p = o(p, s),
				h = o(h, a);
			return [A, f, p, h]
		}
		function f(e) {
			var t, n = "", i = 32 * e.length;
			for (t = 0; t < i; t += 8)
				n += String.fromCharCode(e[t >> 5] >>> t % 32 & 255);
			return n
		}
		function p(e) {
			var t, n = [];
			for (n[(e.length >> 2) - 1] = void 0,
			t = 0; t < n.length; t += 1)
				n[t] = 0;
			var i = 8 * e.length;
			for (t = 0; t < i; t += 8)
				n[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
			return n
		}
		function h(e) {
			return f(A(p(e), 8 * e.length))
		}
		function m(e, t) {
			var n, i, r = p(e), o = [], s = [];
			for (o[15] = s[15] = void 0,
			r.length > 16 && (r = A(r, 8 * e.length)),
			n = 0; n < 16; n += 1)
				o[n] = 909522486 ^ r[n],
				s[n] = 1549556828 ^ r[n];
			return i = A(o.concat(p(t)), 512 + 8 * t.length),
			f(A(s.concat(i), 640))
		}
		function v(e) {
			var t, n, i = "0123456789abcdef", r = "";
			for (n = 0; n < e.length; n += 1)
				t = e.charCodeAt(n),
				r += i.charAt(t >>> 4 & 15) + i.charAt(15 & t);
			return r
		}
		function g(e) {
			return unescape(encodeURIComponent(e))
		}
		function y(e) {
			return h(g(e))
		}
		function b(e) {
			return v(y(e))
		}
		function w(e, t) {
			return m(g(e), g(t))
		}
		function C(e, t) {
			return v(w(e, t))
		}
		function x(e, t, n) {
			return t ? n ? w(t, e) : C(t, e) : n ? y(e) : b(e)
		}
	`)
}

type BaiduStorage struct {
	LoginInfo     *LoginInfo
	Cookie        string
	UserAgent     string
	ShareErrorMap map[int64]int64
	Lock          sync.Mutex
}

/*
{
"errno": 0,
"newno": "",
"request_id": 1305775965182272800,
"show_msg": ""
}
*/
type TestResult struct {
	ErrNo     int       `json:"errno"`
	NewNo     string    `json:"newno"`
	RequestId int64     `json:"request_id"`
	ShowMsg   string    `json:"show_msg"`
	LoginInfo LoginInfo `json:"login_info"`
}

type LoginInfo struct {
	Bdstoken string `json:"bdstoken"`
	PhotoUrl string `json:"photo_url"`
	Svip10Id string `json:"svip10_id"`
	Uk       int    `json:"uk"`
	UkStr    string `json:"uk_str"`
	UserName string `json:"username"`
	VipId    string `json:"vip_identity"`
	VipLevel int    `json:"vip_level"`
	VipPoint int    `json:"vip_point"`
	VipType  string `json:"vip_type"`
}

type ShareReuslt struct {
	Count     int    `json:"count"`
	ErrNo     int    `json:"errno"`
	NewNo     string `json:"newno"`
	NextPage  int    `json:"nextpage"`
	RequestId int64  `json:"request_id"`
	ShowMsg   string `json:"show_msg"`
	ShareInfo []struct {
		AppId           int     `json:"appId"`
		Bitmap          int     `json:"bitmap"`
		Channel         int     `json:"channel"`
		ChannelInfo     string  `json:"channelInfo"`
		Ctime           int     `json:"ctime"`
		DCnt            int     `json:"dCnt"`
		Description     string  `json:"description"`
		Dtime           int     `json:"dtime"`
		ExpiredTime     int     `json:"expiredTime"`
		ExpiredType     int     `json:"expiredType"`
		FsIds           []int64 `json:"fsIds"`
		Ip              int     `json:"ip"`
		IsElink         int     `json:"isElink"`
		IsCard          int     `json:"is_card"`
		Name            string  `json:"name"`
		Passwd          string  `json:"passwd"`
		Port            int     `json:"port"`
		PrivilegeType   int     `json:"privilege_type"`
		Public          int     `json:"public"`
		PublicChannel   int     `json:"publicChannel"`
		ShareId         int64   `json:"shareId"`
		ShareInfo       string  `json:"shareinfo"`
		ShareType       int     `json:"sharetype"`
		ShortLink       string  `json:"shortlink"`
		ShortUrl        string  `json:"shorturl"`
		Sinfo           string  `json:"sinfo"`
		Status          int     `json:"status"`
		SubStatus       string  `json:"substatus"`
		TCnt            int     `json:"tCnt"`
		Tag             int     `json:"tag"`
		TplId           int     `json:"tplId"`
		TypicalCategory int     `json:"typicalCategory"`
		TypicalPath     string  `json:"typicalPath"`
		VCnt            int     `json:"vCnt"`
	} `json:"list"`
}

type PasswdResult struct {
	ErrNo     int    `json:"errno"`
	IsElink   int    `json:"isElink"`
	NewNo     string `json:"newno"`
	Pwd       string `json:"pwd"`
	RequestId int64  `json:"request_id"`
	ShortUrl  string `json:"shorturl"`
	ShowMsg   string `json:"show_msg"`
}

type ReShareResult struct {
	AheadMsg       string `json:"aheadmsg"`
	CreateShareTip string `json:"createsharetips_ldlj"`
	Ctime          int    `json:"ctime"`
	ErrNo          int    `json:"errno"`
	ExpiredType    int    `json:"expiredType"`
	ExpireTime     int    `json:"expiretime"`
	ImageType      int    `json:"imagetype"`
	Link           string `json:"link"`
	NewNo          string `json:"newno"`
	Premis         bool   `json:"premis"`
	PromptType     int    `json:"prompt_type"`
	QrcodeUrl      string `json:"qrcodeurl"`
	RequestId      int64  `json:"request_id"`
	ShareId        int64  `json:"shareid"`
	ShortUrl       string `json:"shorturl"`
	ShowMsg        string `json:"show_msg"`
	TailMsg        string `json:"tailmsg"`
}

type ShareForever struct {
	ShortUrl string `json:"shorturl"`
	Pwd      string `json:"pwd"`
	Url      string `json:"url"`
	Errno    int    `json:"errno"`
	ShowMsg  string `json:"show_msg"`
}

func NewBaiduStorage(cookie string) *BaiduStorage {
	baiduStorage := &BaiduStorage{ShareErrorMap: map[int64]int64{}, Lock: sync.Mutex{}, Cookie: cookie, UserAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
	err := baiduStorage.test()
	if err != nil {
		panic(err)
	}
	return baiduStorage
}

func (m *BaiduStorage) doRequest(url string, method string, form url.Values) ([]byte, error) {
	var req *http.Request
	var err error
	if form == nil {
		req, err = http.NewRequest(method, url, nil)
	} else {
		req, err = http.NewRequest(method, url, strings.NewReader(form.Encode()))
		req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
	}

	if err != nil {
		// 不应该发生
		return nil, errors.New("创建请求失败, 这不是应该发生的")
	}
	req.Header.Set("Cookie", m.Cookie)
	req.Header.Set("User-Agent", m.UserAgent)
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return nil, errors.New("请求失败, 请检查网络连接")
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusOK {
		return nil, errors.New("请求失败, 请重试")
	}
	data, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, errors.New("读取响应失败")
	}
	return data, nil
}

func (m *BaiduStorage) test() error {
	testUrl := "https://pan.baidu.com/api/loginStatus?clienttype=0"
	data, err := m.doRequest(testUrl, http.MethodGet, nil)
	if err != nil {
		return err
	}

	cr := &TestResult{}
	json.Unmarshal(data, cr)
	if cr.ErrNo != 0 {
		return errors.New(cr.ShowMsg)
	}
	m.LoginInfo = &cr.LoginInfo
	return nil
}

func (m *BaiduStorage) ShareFiles(c *fiber.Ctx) error {
	data, err := m.shareFiles()
	if err != nil {
		return err
	}
	return c.JSON(data)
}

func (m *BaiduStorage) shareFiles() (*ShareReuslt, error) {
	shareUrl := "https://pan.baidu.com/share/record?num=1000&page=1&order=ctime&desc=1"
	data, err := m.doRequest(shareUrl, http.MethodGet, nil)
	if err != nil {
		return nil, err
	}
	sr := &ShareReuslt{}
	json.Unmarshal(data, sr)
	return sr, nil
}

func (m *BaiduStorage) CancelShare(c *fiber.Ctx) error {
	shareId := c.Params("shareId")
	data, err := m.cancelshare(shareId)
	if err != nil {
		return err
	}
	return c.SendString(string(data))
}

func (m *BaiduStorage) cancelshare(shareId string) ([]byte, error) {
	cancelShareUrl := "https://pan.baidu.com/share/cancel"
	form := url.Values{}
	form.Add("shareid_list", fmt.Sprintf("[%s]", shareId))
	return m.doRequest(cancelShareUrl, http.MethodPost, form)
}

func (m *BaiduStorage) GetFileShare(c *fiber.Ctx) error {
	fsId := c.Params("fsid")
	sf, err := m.getFileShare(fsId)
	if err != nil {
		return err
	}
	return c.JSON(sf)
}

func (m *BaiduStorage) getFileShare(fsId string) (*ShareForever, error) {
	sr, err := m.shareFiles()
	if err != nil {
		return nil, err
	}
	var shareId int64
	var shortLink string
	var expiredType int
	var typicalPath string
	find := false
	for _, v := range sr.ShareInfo {
		for _, vv := range v.FsIds {
			if fmt.Sprint(vv) == fsId {
				shareId = v.ShareId
				shortLink = v.ShortLink
				expiredType = v.ExpiredType
				typicalPath = v.TypicalPath
				find = true
				break
			}
		}
		if find {
			break
		}
	}
	if typicalPath == "分享的文件已被删除" {
		return &ShareForever{Errno: -1, ShowMsg: "分享的文件已被删除"}, nil
	}
	if find {
		if expiredType == 0 || expiredType == 1 {
			pr, err := m.getPasswd(fmt.Sprint(shareId))
			if err != nil {
				return nil, err
			}
			return &ShareForever{ShortUrl: shortLink, Pwd: pr.Pwd, Url: shortLink + "?pwd=" + pr.Pwd, Errno: 0, ShowMsg: "已有分享未过期, 获取成功"}, nil
		} else if expiredType == -1 {
			data, pwd, err := m.reShare(fmt.Sprint(shareId))
			if err != nil {
				return nil, err
			}
			rsr := &ReShareResult{}
			json.Unmarshal(data, rsr)
			if rsr.ErrNo != 0 {
				return &ShareForever{Errno: -1, ShowMsg: rsr.ShowMsg}, nil
			}
			return &ShareForever{ShortUrl: rsr.ShortUrl, Pwd: pwd, Url: rsr.ShortUrl + "?pwd=" + pwd, Errno: 0, ShowMsg: "分享已过期, 重新分享成功"}, nil
		}
	} else {
		pwd := util.RandomString(4)
		fsids, err := strconv.ParseInt(fsId, 10, 64)
		if err != nil {
			return nil, err
		}
		pr, pwd, err := m.share([]int64{fsids}, pwd)
		if err != nil {
			return nil, err
		}
		rsr := &ReShareResult{}
		json.Unmarshal(pr, rsr)
		if rsr.ErrNo != 0 {
			return &ShareForever{Errno: rsr.ErrNo, ShowMsg: rsr.ShowMsg}, nil
		}
		return &ShareForever{ShortUrl: rsr.ShortUrl, Pwd: pwd, Url: rsr.ShortUrl + "?pwd=" + pwd, Errno: 0, ShowMsg: "未找到已有分享, 新建分享成功"}, nil
	}
	return &ShareForever{Errno: -1, ShowMsg: "未考虑到的情况, 请提交issue, 并附上相关信息, 谢谢"}, nil
}

func (m *BaiduStorage) reShare(shareId string) ([]byte, string, error) {
	pr, err := m.getPasswd(shareId)
	if err != nil {
		return nil, "", err
	}
	if pr.Pwd == "" {
		pr.Pwd = util.RandomString(4)
	}
	shareFiles, err := m.shareFiles()
	if err != nil {
		return nil, "", err
	}
	shareIdInt, err := strconv.Atoi(shareId)
	if err != nil {
		return nil, "", err
	}
	var fsids []int64
	for _, v := range shareFiles.ShareInfo {
		if int(v.ShareId) == shareIdInt {
			fsids = v.FsIds
			break
		}
	}
	if len(fsids) == 0 {
		return nil, "", errors.New("未找到分享文件")
	}
	return m.share(fsids, pr.Pwd)
}

func (m *BaiduStorage) share(fsids []int64, pwd string) ([]byte, string, error) {
	fidList, err := json.Marshal(fsids)
	if err != nil {
		return nil, pwd, err
	}
	shareUrl := "https://pan.baidu.com/share/set"
	form := url.Values{}
	form.Add("period", "0")
	form.Add("pwd", pwd)
	form.Add("fid_list", string(fidList))
	form.Add("schannel", "4")
	data, err := m.doRequest(shareUrl, http.MethodPost, form)
	return data, pwd, err
}

func (m *BaiduStorage) ReShare(c *fiber.Ctx) error {
	shareId := c.Params("shareid")
	data, _, err := m.reShare(shareId)
	if err != nil {
		return err
	}
	return c.SendString(string(data))
}

func (m *BaiduStorage) GetPasswd(c *fiber.Ctx) error {
	shareId := c.Params("shareid")
	pr, err := m.getPasswd(shareId)
	if err != nil {
		return err
	}
	return c.JSON(pr)
}

func (m *BaiduStorage) getPasswd(shareId string) (*PasswdResult, error) {
	sign, err := m.sign(shareId + "_sharesurlinfo!@#")
	if err != nil {
		return nil, err
	}

	passwdUrl := fmt.Sprintf("https://pan.baidu.com/share/surlinfoinrecord?shareid=%s&sign=%s", shareId, sign)
	data, err := m.doRequest(passwdUrl, http.MethodGet, nil)
	if err != nil {
		return nil, err
	}
	pr := &PasswdResult{}
	json.Unmarshal(data, pr)
	return pr, nil
}

func (m *BaiduStorage) UserInfo(c *fiber.Ctx) error {
	return c.JSON(m.LoginInfo)
}

func (m *BaiduStorage) sign(s string) (string, error) {
	return sign(s)
}

func sign(s string) (string, error) {
	value, err := vm.Call("x", nil, s)
	if err != nil {
		return "", err
	}
	return value.String(), nil
}

func (m *BaiduStorage) AutoReShare(conf config.ReShare) {
	shareFiles, err := m.shareFiles()
	if err != nil {
		log.Println(err)
		return
	}
	shields := []int64{}
	wrongStatus := map[int64]string{}
	notExpired := []int64{}
	realIgnore := []int64{}
	deleted := []int64{}
	errors := map[int64]string{}
	update := map[int64]string{}

	statusMap := map[int]string{1: "分享失败", 2: "暂时不可访问", 3: "分享失败", 4: "审核未通过", 19: "已被冻结"}

	for _, v := range shareFiles.ShareInfo {
		// 已屏蔽
		if v.Tag == 7 {
			shields = append(shields, v.ShareId)
			continue
		}
		/*
			1: "分享失败",
			2: "暂时不可访问",
			3: "分享失败",
			4: "审核未通过",
			19: "已被冻结",
		*/
		if v.Status == 1 || v.Status == 2 || v.Status == 3 || v.Status == 4 || v.Status == 19 {
			wrongStatus[v.ShareId] = statusMap[v.Status]
			continue
		}
		// 0: 期限分享 1: 永久分享
		if v.ExpiredType == 0 || v.ExpiredType == 1 {
			notExpired = append(notExpired, v.ShareId)
			continue
		}
		// 忽略
		contains := false
		for _, ig := range conf.Ignore {
			if ig == v.ShareId {
				realIgnore = append(realIgnore, v.ShareId)
				contains = true
			}
		}
		if contains {
			continue
		}

		m.Lock.Lock()
		value, ok := m.ShareErrorMap[v.ShareId]
		m.Lock.Unlock()
		if ok {
			if time.Now().Unix()-value >= int64(conf.ErrorEetry) {
				m.Lock.Lock()
				delete(m.ShareErrorMap, v.ShareId)
				m.Lock.Unlock()
			} else {
				errors[v.ShareId] = "上次尝试分享失败"
				continue
			}
		}

		if v.TypicalPath == "分享的文件已被删除" {
			deleted = append(deleted, v.ShareId)
			continue
		}

		for _, fsid := range v.FsIds {
			fs, err := m.getFileShare(fmt.Sprint(fsid))
			if err != nil {
				log.Println(err)
				continue
			}

			if fs.Errno == 0 {
				update[v.ShareId] = " 文件id: " + fmt.Sprint(fsid) + ", " + fs.ShowMsg + ", 新的连接: " + fs.Url
			} else {
				m.Lock.Lock()
				m.ShareErrorMap[v.ShareId] = time.Now().Unix()
				m.Lock.Unlock()
				errors[v.ShareId] = "分享id: " + fmt.Sprint(v.ShareId) + ", 分享失败, 原因: " + fs.ShowMsg
			}
			time.Sleep(500 * time.Millisecond)
		}
	}
	logs := "\n尝试更新: \n" + mapToString(update) +
		"\n分享未过期: \n" + arrayToString(notExpired, ",") +
		"\n忽略: \n" + arrayToString(realIgnore, ",") +
		"\n文件已删除: \n" + arrayToString(deleted, ",") +
		"\n惨遭屏蔽: \n" + arrayToString(shields, ",") +
		"\n状态异常: \n" + mapToString(wrongStatus) +
		"\n分享错误: \n" + mapToString(errors)
	log.Println(logs)
}

func arrayToString(A []int64, delim string) string {
	return strings.Trim(strings.Join(strings.Fields(fmt.Sprint(A)), delim), "[]")
}

func mapToString(m map[int64]string) string {
	var s = ""
	for k, v := range m {
		s += fmt.Sprintf("分享id: %d: %s\n", k, v)
	}
	return s
}
