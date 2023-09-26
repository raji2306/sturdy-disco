pipeline {
    agent any // Use any available agent/node to run the pipeline

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                url: 'https://github.com/raji2306/sturdy-disco.git'
            }
        } // Corrected placement of closing brace for the "Checkout" stage

        stage('Build') {
     steps {
        bat 'echo "Building the project"'
        // Replace this with your actual Windows batch commands
    }
        }
    }

    post {
        always {
            // Send an email notification if the build is successful
            emailext subject: "Build Success: \${BUILD_NUMBER} in \${JOB_NAME}",
                      body: """<p>Build Result: \${BUILD_RESULT}</p>
                               <p>Project: \${PROJECT_NAME}</p>
                               <p>Build URL: \${BUILD_URL}</p>""",
                      to: 'rajeshsuresh154@gmail.com' // Replace with the recipient's email address
        }
    }
}
