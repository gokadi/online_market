
# -- Build --------------------------------------------------------------------
# hadolint ignore=DL3007
FROM python:3.7 AS build

WORKDIR /build/
COPY ./ ./
RUN make build_dist

# -- App ----------------------------------------------------------------------
FROM python:3.7
ARG APP_DIR=/app

RUN pip install pip setuptools -U

ENV STATIC_ROOT ${APP_DIR}/static/
ENV MEDIA_ROOT ${APP_DIR}/media/
RUN mkdir -p ${STATIC_ROOT}
RUN mkdir -p ${MEDIA_ROOT}
RUN chmod -R 777 ${MEDIA_ROOT}
COPY media ${MEDIA_ROOT}
RUN git clone https://github.com/vishnubob/wait-for-it.git

WORKDIR /tmp/setup/

COPY --from=build /build/ ./

RUN make install_dist
RUN rm -rf /tmp/setup/

ENV DJANGO_SETTINGS_MODULE online_market.settings
RUN django-admin collectstatic --noinput

WORKDIR /tmp/

COPY docker/online_market/files/gunicorn.conf ${APP_DIR}
COPY db.json ${APP_DIR}

CMD [ \
    "gunicorn","-c","/app/gunicorn.conf","online_market.wsgi:application" \
]

ENV PYTHONUNBUFFERED 1
ENV WEB_CONCURRENCY 4
