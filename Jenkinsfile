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
                bat 'echo "Building the project"'
                // Replace this with actual build commands, e.g., 'mvn clean install' for Maven
            }
        }
    }

    post {
        always {
            script {
                def buildNumber = currentBuild.number.toString()
                echo "Build Number: $buildNumber"

                def jobName = env.JOB_NAME
                def buildResult = currentBuild.resultIsBetterOrEqualTo(Result.SUCCESS) ? "SUCCESS" : "FAILURE"
                def buildUrl = env.BUILD_URL

                // Load the emailConfig.groovy script in the same scope
                load 'email.groovy', buildNumber: buildNumber, jobName: jobName, buildResult: buildResult, buildUrl: buildUrl
            }
        }
    }
}
