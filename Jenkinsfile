pipeline {
    agent {
        dockerfile {
            label 'docker'
            }
        }
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                git branch: 'Ex', url: 'https://github.com/Ilysikov/TestApiReqres.git'
            }
        }
        stage('Initialize') {
            steps {
                script {
                    def dockerHome = tool 'docker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                }
            }
        }
        stage('Check Docker Version') {
            steps {
                script {
                    // Выполнение команды для проверки версии Docker
                    def dockerVersion = sh(script: 'docker --version', returnStdout: true).trim()
                    echo "Docker version: ${dockerVersion}"
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build('my-app-image')
                }
            }
        }

        stage('Deploy') {
             steps {
                script {
                        sh 'docker run -d --name myapp -p 2375:2375 my-app-image'
                        }
                    }
                }

        }
    }