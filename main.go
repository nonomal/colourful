package main

import (
	"fmt"
	"log"
	"time"

	"github.com/go-co-op/gocron"
	"github.com/gofiber/fiber/v2"
	"github.com/robfig/cron"
	"github.com/xi-mad/colourful/config"
	"github.com/xi-mad/colourful/notify"
	"github.com/xi-mad/colourful/storage"
)

func main() {
	config := config.Load()
	app := fiber.New()

	baiduStorage := storage.NewBaiduStorage(config.Baidu.Cookie)
	runReshare(config.ReShare, baiduStorage)
	runNotify(config.Notify, baiduStorage)

	apiRoute := app.Group("/api")

	apiRoute.Get("/files", baiduStorage.Files)
	apiRoute.Get("/sharefiles", baiduStorage.ShareFiles)
	apiRoute.Get("/userinfo", baiduStorage.UserInfo)
	apiRoute.Get("/getpwd/:shareid", baiduStorage.GetPasswd)
	apiRoute.Get("/reshare/:shareid", baiduStorage.ReShare)
	apiRoute.Get("/cancelshare/:shareid", baiduStorage.CancelShare)
	apiRoute.Get("/getfileshare/:fsid", baiduStorage.GetFileShare)
	app.Static("/", "./front/dist")

	app.Listen(fmt.Sprintf("%s:%d", config.Server.Host, config.Server.Port))
}

func runNotify(conf config.Notify, baiduStorage *storage.BaiduStorage) {
	if conf.Enable {
		log.Println("开启通知")
		go func() {
			c := cron.New()
			nfs := notify.NewNotifys(conf)
			c.AddFunc(conf.Cron, func() {
				for _, n := range nfs {
					err := n.Notify(baiduStorage)
					if err != nil {
						log.Println(err.Error())
					}
				}
			})
			c.Start()
			defer c.Stop()
			select {}
		}()
	}
}

func runReshare(reshare config.ReShare, baiduStorage *storage.BaiduStorage) {
	if reshare.Enable {
		log.Println("开启分享自动补档")
		go func() {
			timezone, err := time.LoadLocation("Asia/shanghai")
			if err != nil {
				log.Println(err.Error())
				timezone = time.FixedZone("CST", 8*3600)
			}
			s := gocron.NewScheduler(timezone)
			s.Every(reshare.Interval).Seconds().Do(func() {
				go baiduStorage.AutoReShare(reshare)
			})
			s.StartBlocking()
		}()
	}
}
