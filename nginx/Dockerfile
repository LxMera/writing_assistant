FROM nginx:1.25-alpine

# Instalar apache2-utils para htpasswd
RUN apk add --no-cache apache2-utils

# Copiar configuración de nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copiar archivo de contraseñas
COPY .htpasswd /etc/nginx/.htpasswd

# Exponer puerto 80
EXPOSE 80

# Comando por defecto
CMD ["nginx", "-g", "daemon off;"]