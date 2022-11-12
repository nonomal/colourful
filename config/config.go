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
	log.Printf("Loaded config: %+v", config)
	return config
}
