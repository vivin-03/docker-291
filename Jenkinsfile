pipeline {
    agent any

    environment {
        DOCKER_USER = "akbaraliiii"
        IMAGE_NAME = "docker-fat-app"
        TAG = "latest"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/akbarali2k6/Docker_FAT_Akbar0292.git'
            }
        }

        stage('Verify Docker') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_USER/$IMAGE_NAME:$TAG .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-cred',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKER_USER/$IMAGE_NAME:$TAG'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 $DOCKER_USER/$IMAGE_NAME:$TAG'
            }
        }
    }
}