pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Clone the repository
                git 'https://github.com/yourusername/your-python-repo.git'
            }
        }
    stages {
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
                    docker.image('my-app-image').run('-p 8080:8080')
                }
            }
        }
    }
}
