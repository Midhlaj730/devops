FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*
COPY login.html /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/nginx.conf
COPY style.html /usr/share/nginx/html/

CMD ["nginx", "-g", "daemon off;"]
