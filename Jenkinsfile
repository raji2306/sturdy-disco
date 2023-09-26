pipeline {
    agent any // Use any available agent/node to run the pipeline

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                url: 'https://github.com/raji2306/sturdy-disco.git'
            }
        }

        stage('Build') {
            steps {
                // Build your project here
                bat 'echo "Building the project"'
                // Replace this with actual build commands, e.g., 'mvn clean install' for Maven
            }
        }
    }

    post {
        always {
            // Import and execute the email configuration from the shared Groovy script
            script {
                load 'email.groovy'
            }
        }
    }
}
