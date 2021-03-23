FROM mysql:5.7

COPY backup.sh /backup.sh

HEALTHCHECK --interval=30s --retries=10 CMD mysqlshow ${MYSQL_DATABASE}
