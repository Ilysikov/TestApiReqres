pipeline {
    agent any
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
                    sudo systemctl start docker
                    sudo docker.build('my-app-image')
                }
            }
        }

        stage('Deploy') {
             steps {
                script {
                        // Stop and remove the existing container
                        sh 'docker stop myapp || true'
                        sh 'docker rm myapp || true'

                        // Build a new Docker image
                        sh 'docker build -t myapp:latest .'

                        // Run the new container
                        sh 'docker run -d --name myapp -p 80:80 myapp:latest'
                        }
                    }
                }

        }
    }
