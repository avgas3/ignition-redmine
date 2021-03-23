#!/bin/sh
BACKUP_TARGET=/backups

BACKUP_FILE=${BACKUP_TARGET}/backup_`date +%Y%m%d_%H%M%S`.sql.gz
/usr/bin/mysqldump -u ${MYSQL_USER} ${MYSQL_DATABASE} --databases | gzip -9 > ${BACKUP_FILE}
chmod 640 ${BACKUP_FILE}

if [ -z ${RETAIN_FILES_COUNT} ]; then
	echo "Must set RETAIN_FILES_COUNT! Skipping rotation."
else
	ls -1 ${BACKUP_TARGET}/*.sql.gz | sort -r | tail -n +`expr ${RETAIN_FILES_COUNT} + 1` | xargs rm > /dev/null 2>&1
fi
