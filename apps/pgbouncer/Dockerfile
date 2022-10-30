FROM edoburu/pgbouncer:1.17.0
MAINTAINER Edi Santoso <repodevs@gmail.com>

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/bin/pgbouncer", "/etc/pgbouncer/pgbouncer.ini"]
