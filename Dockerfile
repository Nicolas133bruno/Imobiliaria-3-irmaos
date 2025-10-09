# Stage 1: Build
FROM eclipse-temurin:17-jdk-alpine AS builder
WORKDIR /app
COPY MinhaApp.java .
COPY mysql-connector-java-8.0.30.jar .
RUN javac -cp mysql-connector-java-8.0.30.jar MinhaApp.java

# Stage 2: Runtime
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=builder /app/MinhaApp.class .
COPY --from=builder /app/mysql-connector-java-8.0.30.jar .

ENV DB_HOST=mysql-db
ENV DB_PORT=3306
ENV DB_NAME=imobiliaria
ENV DB_USER=root
ENV DB_PASS=Felipe123

CMD ["java", "-cp", ".:mysql-connector-java-8.0.30.jar", "MinhaApp"]
