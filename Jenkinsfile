pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                git branch: 'Ex', url: 'https://github.com/Ilysikov/TestApiReqres.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    def myDocker = docker // Используйте переменную для доступа к Docker
                    myDocker.build('my-app-image')
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    def myDocker = docker // Используйте переменную для доступа к Docker
                    myDocker.image('my-app-image').run('-p 8080:8080')
                }
            }
        }
    }
}
