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
}
