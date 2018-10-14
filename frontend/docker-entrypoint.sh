#!/bin/sh
set -e

if [ -z "$BACKEND_SVC" ]; then
    cat >&2 <<EOF
The environment variable BACKEND_SVC must be set.
EOF
    exit 1
fi

if [ -f /nginx.conf.template ]; then
    envsubst '${BACKEND_SVC}' < /nginx.conf.template > /etc/nginx/conf.d/default.conf
fi

echo
echo 'Frontend init process complete; ready for start up.'
echo

exec "$@"
