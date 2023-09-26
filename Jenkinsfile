pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Define your build steps here
                sh 'echo "Building..."'
            }
        }
        stage('Deploy') {
            steps {
                // Define your deployment steps here
                sh 'echo "Deploying..."'
            }
        }
    }

    post {
        always {
            // Load and execute the email.groovy script
            script {
                load 'email.groovy'
            }
        }
    }
}
