FROM ubuntu:18.04 as builder
ARG PYTHON_REDMINE=2.3.0

RUN apt-get update && \
    apt-get install -y --no-install-recommends python python-pip

RUN pip install python-redmine==${PYTHON_REDMINE}


FROM kcollins/ignition:8.1.3

COPY --from=builder --chown=ignition:ignition /usr/local/lib/python2.7/dist-packages/certifi user-lib/pylib/site-packages/certifi
COPY --from=builder --chown=ignition:ignition /usr/local/lib/python2.7/dist-packages/chardet user-lib/pylib/site-packages/chardet
COPY --from=builder --chown=ignition:ignition /usr/local/lib/python2.7/dist-packages/idna user-lib/pylib/site-packages/idna
COPY --from=builder --chown=ignition:ignition /usr/local/lib/python2.7/dist-packages/redminelib user-lib/pylib/site-packages/redminelib
COPY --from=builder --chown=ignition:ignition /usr/local/lib/python2.7/dist-packages/requests user-lib/pylib/site-packages/requests
COPY --from=builder --chown=ignition:ignition /usr/local/lib/python2.7/dist-packages/urllib3 user-lib/pylib/site-packages/urllib3

