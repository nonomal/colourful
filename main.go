package main

import (
	"fmt"
	"time"

	"github.com/go-co-op/gocron"
	"github.com/gofiber/fiber/v2"
	"github.com/xi-mad/colorful/config"
	"github.com/xi-mad/colorful/storage"
)

func main() {
	config := config.Load()

	app := fiber.New()

	baiduStorage := storage.NewBaiduStorage(config.Baidu.Cookie)

	if config.ReShare.Enable {
		go func() {
			timezone, _ := time.LoadLocation("Asia/Shanghai")
			s := gocron.NewScheduler(timezone)
			s.Every(config.ReShare.Interval).Seconds().Do(func() {
				go baiduStorage.AutoReShare(config.ReShare)
			})
			s.StartBlocking()
		}()
	}

	apiRoute := app.Group("/api")

	apiRoute.Get("/sharefiles", baiduStorage.ShareFiles)
	apiRoute.Get("/userinfo", baiduStorage.UserInfo)
	apiRoute.Get("/getpwd/:shareid", baiduStorage.GetPasswd)
	apiRoute.Get("/reshare/:shareid", baiduStorage.ReShare)
	apiRoute.Get("/cancelshare/:shareid", baiduStorage.CancelShare)
	apiRoute.Get("/getfileshare/:fsid", baiduStorage.GetFileShare)
	app.Static("/", "./front/dist")

	app.Listen(fmt.Sprintf("%s:%d", config.Server.Host, config.Server.Port))
}
