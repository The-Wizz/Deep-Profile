FROM registry.gitlab.com/the-wizz/deep-profile-registry/deep-profile-server:f0bbfd7415a60d4666b395783380a4766902c388

WORKDIR /app
COPY ./server/ /app

EXPOSE 5000
