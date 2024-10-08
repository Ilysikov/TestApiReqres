pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                git branch: 'Ex', url: 'https://github.com/Ilysikov/TestApiReqres.git'
            }
        }

        stage('Check Docker Version') {
            steps {
                script {
                    sh 'docker --version'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'sudo docker build -t docker/my-app-image .'
                }
            }
        }

        stage('Deploy') {
             steps {
                script {
                        sh 'docker run -d -p 2375:2375 docker/my-app-image'
                        }
                    }
                }

        }
    }