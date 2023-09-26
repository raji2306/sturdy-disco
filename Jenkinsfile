import groovy.io.FileType
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
            // Define and pass the necessary environment variables
        always {
            // Define and pass the necessary environment variables within the same scope
            script {
                def recipients = "rajeshsuresh154@gmail.com, rajeshsuresh230699@gmail.com"
                def buildNumber = env.BUILD_NUMBER
                def jobName = env.JOB_NAME
                def buildResult = currentBuild.resultIsBetterOrEqualTo('SUCCESS') ? 'SUCCESS' : 'FAILURE'
                def buildUrl = env.BUILD_URL

                // Load the emailConfig.groovy script in the same scope
                load 'path/to/emailConfig.groovy'
            }
        }
    }
}
