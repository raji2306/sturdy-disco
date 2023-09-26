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
        script {
            def recipients = "rajeshsuresh154@gmail.com, rajeshsuresh230699@gmail.com"
            def buildNumber = env.BUILD_NUMBER
            def jobName = env.JOB_NAME
            def buildResult = currentBuild.resultIsBetterOrEqualTo('SUCCESS') ? 'SUCCESS' : 'FAILURE'
            def buildUrl = env.BUILD_URL

            // Debug statements to verify variable values
            echo "Sending email to: ${recipients}"
            echo "Build Number: ${buildNumber}"
            echo "Job Name: ${jobName}"
            echo "Build Result: ${buildResult}"
            echo "Build URL: ${buildUrl}"

            // Call the email.groovy script with named arguments
            load 'email.groovy', buildNumber: buildNumber, jobName: jobName, buildResult: buildResult, buildUrl: buildUrl
        }
        }
    }
}
