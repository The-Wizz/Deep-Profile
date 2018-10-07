FROM nginx:alpine
LABEL name=goldenprofile-frontend \
      version=0.0.1 \
      maintainer="dev@florianrusch.de"

# Updating the system
RUN apk update && \
    apk upgrade && \
    rm -rf /var/cache/apk/* /tmp/* /usr/share/man

# Configure nginx + php
ADD nginx.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]

WORKDIR /usr/share/nginx/html

EXPOSE 80
EXPOSE 443
