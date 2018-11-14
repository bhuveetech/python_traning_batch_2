cd "C:\Program Files\Docker Toolbox" & docker build -t sample_webapp C:\Users\Naresh\PycharmProjects\python_traning_batch_2\devops & docker image ls & docker run --name web_application -p 5000:8080 -d  sample_webapp

