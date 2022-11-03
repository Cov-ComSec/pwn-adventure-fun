FROM ubuntu:14.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y postgresql-client && \
    useradd -s /bin/sh postgres

COPY --chown=postgres ./MasterServer /app/PwnAdventure3/

USER postgres
EXPOSE 3333

ENTRYPOINT ["bash", "/app/PwnAdventure3/master.sh"]
