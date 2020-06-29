FROM online_market_app AS backend
FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

COPY default.crt /etc/nginx
COPY default.key /etc/nginx

COPY --from=backend /app/static/ /app/static/
COPY --from=backend /app/media/ /app/media/


CMD ["nginx", "-g", "daemon off;"]
