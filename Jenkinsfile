pipeline {
    agent any // Use any available agent/node to run the pipeline

    environment {
        // Define environment variables that you want to use throughout the pipeline
        RECIPIENTS = "rajeshsuresh154@gmail.com, rajeshsuresh230699@gmail.com"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from the Git repository
                script {
                    def scmCheckout = checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/raji2306/sturdy-disco.git']]])
                }
            }
        }

        stage('Build') {
            steps {
                // Build your project here
                sh 'echo "Building the project"'
                // Replace this with actual build commands, e.g., 'mvn clean install' for Maven
            }
        }
    }

    post {
        always {
            // Define and pass the necessary environment variables
        script {
            def buildNumber = currentBuild.number.toString()
            def jobName = env.JOB_NAME
            def buildResult = currentBuild.resultIsBetterOrEqualTo('SUCCESS') ? 'SUCCESS' : 'FAILURE'
            def buildUrl = env.BUILD_URL

            // Load the emailConfig.groovy script in the same scope
            load 'path/to/emailConfig.groovy'

            // Replace the 'nohup' command with a Windows-friendly command using 'bat'
            bat """
                echo Sending email notification...
                groovy path/to/emailConfig.groovy
            """
        }
        }
    }
}
