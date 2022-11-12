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
	log.Printf("Loaded config: %+v", config)
	return config
}
