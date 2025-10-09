# === Stage 1: Build ===
FROM eclipse-temurin:17-jdk-alpine AS builder

WORKDIR /app

# Copia o código-fonte Maven
COPY pom.xml .
COPY src ./src

# Build do projeto com Maven (gera .jar)
RUN ./mvnw clean package -DskipTests

# === Stage 2: Runtime ===
FROM eclipse-temurin:17-jre-alpine

WORKDIR /app

# Copia o jar gerado
COPY --from=builder /app/target/imobiliaria-0.0.1-SNAPSHOT.jar app.jar

# Variáveis de ambiente para conexão com o MySQL
ENV DB_HOST=mysql-db
ENV DB_PORT=3306
ENV DB_NAME=imobiliaria
ENV DB_USER=nicolas
ENV DB_PASS=123456

ENV USER_ADMIN=ADMIN
ENV USER_CLIENTE=CLIENTE
ENV USER_CORRETOR=CORRETOR

# Executa a aplicação
CMD ["java", "-jar", "app.jar"]
