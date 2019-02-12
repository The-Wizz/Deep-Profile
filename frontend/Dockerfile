FROM nginx:alpine
LABEL name=goldenprofile-frontend \
      version=0.0.1 \
      maintainer="dev@florianrusch.de"

# Updating the system
RUN apk update && \
    apk upgrade && \
    rm -rf /var/cache/apk/* /tmp/* /usr/share/man

# Configure nginx + php
COPY nginx.conf /nginx.conf.template

# Add docker-entrypoint.sh script which will be called when the container starts
COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]

WORKDIR /usr/share/nginx/html

EXPOSE 80
# EXPOSE 443
