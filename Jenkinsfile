pipeline {
    agent any

    environment {
        DOCKER_USER = "vivin0905"
        IMAGE_NAME = "docker-fat-app"
        TAG = "latest"
    }

    stages {

        stage('Fix Docker Path') {
            steps {
                sh '''
                export PATH=$PATH:/usr/local/bin:/opt/homebrew/bin
                which docker
                docker --version
                '''
            }
        }

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/vivin-03/docker-291.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                export PATH=$PATH:/usr/local/bin:/opt/homebrew/bin
                docker build -t $DOCKER_USER/$IMAGE_NAME:$TAG .
                '''
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-cred',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh '''
                    export PATH=$PATH:/usr/local/bin:/opt/homebrew/bin
                    echo $PASS | docker login -u $USER --password-stdin
                    '''
                }
            }
        }

        stage('Push Image') {
            steps {
                sh '''
                export PATH=$PATH:/usr/local/bin:/opt/homebrew/bin
                docker push $DOCKER_USER/$IMAGE_NAME:$TAG
                '''
            }
        }

    }
}
