docker build -t sample_webapp .
docker image ls
docker run --name web_application -p 5000:8080 -d  sample_webapp

