name = colourful
version = v1.1.2

build-linux:
	CGO_ENABLED=0 GOOS=linux GOARCH=arm go build -o release/$(name)-$(version)-linux-arm main.go
	CGO_ENABLED=0 GOOS=linux GOARCH=arm64 go build -o release/$(name)-$(version)-linux-arm64 main.go
	CGO_ENABLED=0 GOOS=linux GOARCH=386 go build -o release/$(name)-$(version)-linux-386 main.go
	CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o release/$(name)-$(version)-linux-amd64 main.go
	
build-win:
	CGO_ENABLED=0 GOOS=windows GOARCH=386 go build -o release/$(name)-$(version)-windows-386.exe main.go
	CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build -o release/$(name)-$(version)-windows-amd64.exe main.go
	
cp-config:
	cp config.yaml release/

package:
	tar -czvf release/$(name)-$(version)-linux-arm.tar.gz release/$(name)-$(version)-linux-arm release/config.yaml
	tar -czvf release/$(name)-$(version)-linux-arm64.tar.gz release/$(name)-$(version)-linux-arm64 release/config.yaml
	tar -czvf release/$(name)-$(version)-linux-386.tar.gz release/$(name)-$(version)-linux-386 release/config.yaml
	tar -czvf release/$(name)-$(version)-linux-amd64.tar.gz release/$(name)-$(version)-linux-amd64 release/config.yaml
	tar -czvf release/$(name)-$(version)-windows-386.tar.gz release/$(name)-$(version)-windows-386.exe release/config.yaml
	tar -czvf release/$(name)-$(version)-windows-amd64.tar.gz release/$(name)-$(version)-windows-amd64.exe release/config.yaml
	rm release/$(name)-$(version)-linux-arm
	rm release/$(name)-$(version)-linux-arm64
	rm release/$(name)-$(version)-linux-386
	rm release/$(name)-$(version)-linux-amd64
	rm release/$(name)-$(version)-windows-386.exe
	rm release/$(name)-$(version)-windows-amd64.exe
	rm release/config.yaml

build-image:
	docker build --build-arg NAME=$(name) --build-arg VERSION=$(version) -t namedlxd/$(name):$(version) .
	docker push namedlxd/colourful:$(version)

clean:
	rm -rf release/*

build: build-linux build-win cp-config build-image package

