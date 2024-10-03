pipeline {
    agent any
//     stages {
//         stage('Checkout') {
//             steps {
//                 echo 'Checking out the code...'
//                 // Clone the repository
//                 git branch: 'Ex', url: 'https://github.com/Ilysikov/TestApiReqres.git'
//             }
//         }
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
