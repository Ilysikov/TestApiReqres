pipeline {
    agent any //{
//         dockerfile {
//             label 'docker'
//             }
//         }
    stages {
//         stage('Checkout') {
//             steps {
//                 echo 'Checking out the code...'
//                 git branch: 'Ex', url: 'https://github.com/Ilysikov/TestApiReqres.git'
//             }
//         }
        stage('Checkout') {
            steps {
                script {
                    sh 'git clone -b Ex https://github.com/Ilysikov/TestApiReqres.git'
                }
            }
        }
//         stage('Initialize') {
//             steps {
//                 script {
//                     def dockerHome = tool 'docker'
//                     env.PATH = "${dockerHome}/bin:${env.PATH}"
//                 }
//             }
//         }
//         stage('Check Docker Version') {
//             steps {
//                 script {
//                     // Выполнение команды для проверки версии Docker
//                     def dockerVersion = sh(script: 'docker --version', returnStdout: true).trim()
//                     echo "Docker version: ${dockerVersion}"
//                 }
//             }
//         }
        stage('Build') {
            steps {
                script {
                    sh 'poetry install'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    sh 'poetry run'
                }
            }
        }

        stage('Deploy') {
             steps {
                script {
                        sh 'python3 app.py'
                        }
                    }
                }

        }
    }