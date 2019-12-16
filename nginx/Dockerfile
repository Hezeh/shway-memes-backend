FROM nginx:1.17.6

RUN rm /etc/nginx/conf.d/default.conf
COPY uwgi_params /etc/nginx/
COPY nginx.conf /etc/nginx/conf.d
