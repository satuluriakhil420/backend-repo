FROM ubuntu
MAINTAINER vamsi

RUN apt-get update
RUN apt-get install -y openjdk-8-jdk

WORKDIR /app
COPY max.jar /app/  # Updated COPY command to copy the JAR to the /app directory inside the container

EXPOSE 8080

CMD ["java", "-jar", "max.jar"]  # Updated the JAR filename in the CMD command
