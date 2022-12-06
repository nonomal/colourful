package notify

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strings"

	"github.com/xi-mad/colourful/config"
	"github.com/xi-mad/colourful/storage"
)

type Notify interface {
	Notify(baiduStorage *storage.BaiduStorage) error
}

func NewNotifys(notify config.Notify) []Notify {
	return []Notify{
		NewPushPlusNotify(notify.PushPlusConfig),
		NewSctNotify(notify.SctConfig),
	}
}

type PushPlusNotify struct {
	PushPlusConfig config.PushPlusConfig
}

func NewPushPlusNotify(config config.PushPlusConfig) *PushPlusNotify {
	return &PushPlusNotify{
		PushPlusConfig: config,
	}
}

func (notify *PushPlusNotify) Notify(baiduStorage *storage.BaiduStorage) error {
	if notify.PushPlusConfig.Enable {
		log.Println("send pushplus notify")
		url := "http://www.pushplus.plus/send"
		type ReqBody struct {
			Token   string `json:"token"`
			Title   string `json:"title"`
			Content string `json:"content"`
			Channel string `json:"channel"`
		}
		body := &ReqBody{
			Token:   notify.PushPlusConfig.Token,
			Title:   "百度云盘自动补档通知",
			Content: render(baiduStorage, "\n"),
			Channel: notify.PushPlusConfig.Channel,
		}
		body_json, _ := json.Marshal(body)
		return sendNotify(url, strings.NewReader(string(body_json)))
	}
	return nil
}

type SctNotify struct {
	SctConfig config.SctConfig
}

func NewSctNotify(config config.SctConfig) *SctNotify {
	return &SctNotify{
		SctConfig: config,
	}
}

func (notify *SctNotify) Notify(baiduStorage *storage.BaiduStorage) error {
	if notify.SctConfig.Enable {
		log.Println("send sct notify")
		url := fmt.Sprintf("https://sctapi.ftqq.com/%s.send", notify.SctConfig.Key)
		type ReqBody struct {
			Title   string `json:"title"`
			Desp    string `json:"desp"`
			Channel string `json:"channel"`
		}
		body := &ReqBody{
			Title:   "百度云盘自动补档通知",
			Desp:    render(baiduStorage, "\n\n"),
			Channel: notify.SctConfig.Channel,
		}
		body_json, _ := json.Marshal(body)
		return sendNotify(url, strings.NewReader(string(body_json)))
	}
	return nil
}

func sendNotify(url string, body *strings.Reader) error {
	req, _ := http.NewRequest("POST", url, body)
	req.Header.Set("Content-Type", "application/json;charset=utf-8")
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	fmt.Println("url: ", url)
	fmt.Println("response Status:", resp.Status)
	fmt.Println("response Headers:", resp.Header)
	b, _ := ioutil.ReadAll(resp.Body)
	fmt.Println("response Body:", string(b))
	return nil
}

func render(baiduStorage *storage.BaiduStorage, sep string) string {
	return baiduStorage.Render(sep)
}
