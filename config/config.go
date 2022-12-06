package config

import (
	"log"
	"os"

	"gopkg.in/yaml.v3"
)

type Server struct {
	Host string `yaml:"host"`
	Port int    `yaml:"port"`
}

type Baidu struct {
	Cookie string `yaml:"cookie"`
}
type ReShare struct {
	Enable     bool    `yaml:"enable"`
	Ignore     []int64 `yaml:"ignore"`
	Interval   int     `yaml:"interval"`
	ErrorEetry int     `yaml:"errorretry"`
}

type Config struct {
	Server  Server  `yaml:"server"`
	ReShare ReShare `yaml:"reshare"`
	Baidu   Baidu   `yaml:"baidu"`
	Notify  Notify  `yaml:"notify"`
}

type Notify struct {
	Cron           string         `yaml:"cron"`
	Enable         bool           `yaml:"enable"`
	SctConfig      SctConfig      `yaml:"sct"`
	PushPlusConfig PushPlusConfig `yaml:"push-plus"`
}

type SctConfig struct {
	Enable  bool   `yaml:"enable"`
	Key     string `yaml:"key"`
	Channel string `yaml:"channel"`
}
type PushPlusConfig struct {
	Enable  bool   `yaml:"enable"`
	Token   string `yaml:"token"`
	Channel string `yaml:"channel"`
}

func Load() *Config {
	config := &Config{}
	content, err := os.ReadFile("config.yaml")
	if err != nil {
		panic(err)
	}
	yaml.Unmarshal(content, config)
	if config.Baidu.Cookie == "" {
		log.Println("Baidu Cookie is empty in config file")
		cookie, ok := os.LookupEnv("BAIDU_COOKIE")
		if ok {
			config.Baidu.Cookie = cookie
			log.Println("Baidu Cookie is loaded from env")
		} else {
			log.Println("Baidu Cookie is empty in env")
		}
	}
	if config.Notify.Cron == "" {
		config.Notify.Enable = false
	}
	if config.Notify.SctConfig.Key == "" {
		key, ok := os.LookupEnv("SCT_KEY")
		if ok {
			config.Notify.SctConfig.Key = key
		}
	}
	if config.Notify.PushPlusConfig.Token == "" {
		token, ok := os.LookupEnv("PUSH_PLUS_TOKEN")
		if ok {
			config.Notify.PushPlusConfig.Token = token
		}
	}
	if config.Notify.PushPlusConfig.Channel == "" {
		config.Notify.PushPlusConfig.Channel = "wechat"
	}
	log.Printf("Loaded config: %+v", config)
	return config
}
