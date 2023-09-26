pipeline {
    agent any

    stages {
        // Define your stages here
    }

    post {
        always {
            script {
                def buildNumber = currentBuild.number.toString()
                echo "Build Number: $buildNumber"

                // Define the arguments as a map
                def emailArgs = [
                    buildNumber: buildNumber,
                    jobName: env.JOB_NAME,
                    buildResult: currentBuild.result,
                    buildUrl: env.BUILD_URL
                ]

                // Load the emailConfig.groovy script and pass the arguments as a map
                load 'email.groovy', emailArgs

                // Replace the 'nohup' command with a Windows-friendly command using 'bat'
                bat """
                    echo Sending email notification...
                    groovy email.groovy
                """
            }
        }
    }
}
