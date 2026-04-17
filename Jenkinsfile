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
                git branch: 'main', url: 'https://github.com/vivin-03/docker-291.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t myimage .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-cred', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    bat 'echo %PASS% | docker login -u %USER% --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                bat 'docker tag myimage vivin0905/myimage'
                bat 'docker push vivin0905/myimage'
            }
        }
    }
}
