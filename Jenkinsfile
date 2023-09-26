pipeline {
    agent any

    environment {
        RECIPIENTS = "rajeshsuresh154@gmail.com, rajeshsuresh230699@gmail.com"
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    def scmCheckout = checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/raji2306/sturdy-disco.git']]])
                }
            }
        }

        stage('Build') {
            steps {
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
                def buildResult = currentBuild.resultIsBetterOrEqualTo("SUCCESS") ? "SUCCESS" : "FAILURE"
                echo "Build Result: $buildResult"

                def jobName = env.JOB_NAME
                def buildUrl = env.BUILD_URL

                load 'email.groovy', buildNumber: buildNumber, jobName: jobName, buildResult: buildResult, buildUrl: buildUrl
            }
        }
    }
}
