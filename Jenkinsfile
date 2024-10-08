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
                    sh 'docker build -t jenkins/my-app-image .'
                }
            }
        }

        stage('Deploy') {
             steps {
                script {
                        sh 'docker run -d -name runtest -p 2375:2375 jenkins/my-app-image'
                        }
                    }
                }


        stage('delete') {
             steps {
                script {
                        sh 'docker stop runtest'
                        sh 'docker rm runtest'
                        }
                    }
                }


        }
    }