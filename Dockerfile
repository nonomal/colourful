FROM alpine:3

WORKDIR /app

ARG NAME
ARG VERSION

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories && \
    apk --update add tzdata && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del tzdata && \
    rm -rf /var/cache/apk/* && \
    echo "/app/$NAME-$VERSION-linux-amd64" > /app/start.sh && \
    chmod +x /app/start.sh

COPY ./release/${NAME}-${VERSION}-linux-amd64 /app/
COPY ./release/config.yaml /app/


EXPOSE 8000

ENTRYPOINT ["/bin/sh", "-c", "/app/start.sh"]
