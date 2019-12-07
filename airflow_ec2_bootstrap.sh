sudo yum update -y

sudo yum install git -y

sudo yum install docker -y

sudo service docker start

sudo gpasswd -a $USER docker

# scp credentials up


aws ecr get-login --region us-east-2

git clone https://github.com/nrvedder/airflow-trim.git

sudo yum install mysql mysql-server -y


# Install docker-compose
# https://acloudxpert.com/how-to-install-docker-compose-on-amazon-linux-ami/
sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null


# Start docker compose
docker-compose -f docker-compose.yml up -d


# Change RDS database in airflow.cfg, airflow.cpzddhbjekdf.us-east-2.rds.amazonaws.com. Change docker image in docker-compose.yml