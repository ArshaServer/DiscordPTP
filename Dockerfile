FROM python:3

RUN mkdir -p /python/DiscordBot
WORKDIR /python/DiscordBot
ENV BOTDIR /python/DiscordBot
COPY ./ ./
ENTRYPOINT [  "./run.sh" ]