# =========================
# Stage único: Runtime
# =========================
FROM eclipse-temurin:17-jre-focal
WORKDIR /app

# Copiar o JAR já compilado (gerado localmente pelo Maven)
COPY target/*.jar app.jar

# Variáveis de ambiente para Spring Boot / MySQL
ENV SPRING_PROFILES_ACTIVE=prod
ENV DB_HOST=mysql-db
ENV DB_PORT=3306
ENV DB_NAME=imobiliaria
ENV DB_USER=root
ENV DB_PASS=Felipe123

# Porta padrão do Spring Boot
EXPOSE 8080

# Comando para rodar a aplicação
ENTRYPOINT ["java", "-jar", "app.jar"]
