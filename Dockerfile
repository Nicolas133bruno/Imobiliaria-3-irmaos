FROM eclipse-temurin:17-jdk-alpine AS builder

WORKDIR /app

COPY MinhaApp.java .
COPY mysql-connector-java-8.0.30.jar .

RUN javac -cp mysql-connector-java-8.0.30.jar MinhaApp.java

FROM eclipse-temurin:17-jre-alpine

WORKDIR /app

COPY --from=builder /app/mysql-connector-java-8.0.30.jar .
COPY --from=builder /app/MinhaApp.class .

CMD ["java", "-cp", ".:mysql-connector-java-8.0.30.jar", "MinhaApp"]
