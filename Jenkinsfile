pipeline {
    agent any

    stages {

        stage('Fix Docker Path') {
            steps {
                bat 'docker --version'
            }
        }

        stage('Checkout Code') {
            steps {
                git 'https://github.com/vivin-03/docker-291.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t myimage .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                bat 'docker login -u USERNAME -p PASSWORD'
            }
        }

        stage('Push Image') {
            steps {
                bat 'docker tag myimage USERNAME/myimage'
                bat 'docker push USERNAME/myimage'
            }
        }
    }
}
