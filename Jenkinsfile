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


        }
    }
}
