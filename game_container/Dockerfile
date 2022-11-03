FROM ubuntu:14.04 as builder
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /root/

RUN apt update && apt install -qy wget tar unzip

RUN bash -c 'echo -e "https://pwnadventure.com/PwnAdventure3Server.tar.gz\nhttps://pwnadventure.com/PwnAdventure3_Linux.zip" | xargs -n1 -P2 wget'
RUN tar -xzf /root/PwnAdventure3Server.tar.gz -C /root/ && \
    unzip /root/PwnAdventure3_Linux.zip -d /root/

FROM ubuntu:14.04
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app/PwnAdventure3
EXPOSE 3000-4000

COPY --from=builder /root/PwnAdventure3/ ./pwn3
COPY --from=builder /root/PwnAdventure3Servers/GameServer/PwnAdventure3Server ./pwn3/PwnAdventure3/Binaries/Linux/

COPY server.ini ./pwn3/PwnAdventure3/Content/Server/server.ini

WORKDIR /app/PwnAdventure3/pwn3/PwnAdventure3/Binaries/Linux/
ENTRYPOINT ["./PwnAdventure3Server"]
