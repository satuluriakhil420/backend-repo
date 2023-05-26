FROM ubuntu
MAINTAINER vamsi

RUN apt-get update
RUN apt-get install -y openjdk-8-jdk

WORKDIR /app
COPY max.jar /app/
EXPOSE 8080

CMD ["java", "-jar", "max.jar"]
