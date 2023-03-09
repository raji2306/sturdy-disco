@Library("shared-library") _
pipeline {
    parameters { 
        string(name: 'machine', defaultValue: 'linux', description: 'Choose the Machine that you wants to run the build') 
        string(name: 'branch', defaultValue: 'master', description: 'Choose the branch that you wants to checkout')
    }
    environment {
//         machine = ${params.machine}
        GIT_BRANCH = ${params.branch}
    }
    tools {
        java "java"
        maven "maven"
    }
    agent any 
//     agent {
//         label $machine
//     }
    stages {
        stage ("Git Checkout Stage"){
            steps {
                git branch: $GIT_BRANCH ,
                credentialsId: 'git_cred',
                url: 'git@github.com:raji2306/sturdy-disco.git'
            }
            triggers{
                cron : 'H */4 * * *' 
            }
        }
        stage ("Run Shared Library to verify the Changes"){  
            steps {
                helloBuddy("rajesh", $date)
            }
            post {
                failure {
                    echo "Fine! The stage completed successfully"
                }
            }
        }
        stage ("Running Build and Packaging Stage"){
            When{
                GIT_BRANCH = "master"
            }
            steps {
                sh "mvn package"
                script {
                    if( currentBuild.currentResult == success ){
                        echo "Build Stage is successful"
                    }
                    else {
                        echo "Build Stage is unsuccessful"
                    }
                }
            }
            
        }
//         stage ("Uploading Generated War file to JFrog Repository"){
//             steps {
//                 timeout(time: 30, unit: 'MINUTES') {
//                 rtServer(
//                     id : "jfrog",
//                     url : "",
//                     credentialsId : "jfrog-cred",
//                     bypassProxy : true
//                 )
//                 }
//                 rtUpload(
//                     serverId :"jfrog",
//                     spec : '''{
//                         "files" : [
//                             {
//                                 "pattern" : "*.war",
//                                 "target" : "jenkins-repo/",
//                                 "props" : "retention.days=11"
//                             }
//                         ]
//                     }'''
//                     "failNoOp": true
//                 )
//             }
//         }
//         stage ("Downloading Important Records from Artifactory Repo"){
//             steps {
//                 rtDownload {
//                     serverId : "jfrog",
//                     spec : '''{
//                         files : [
//                             "pattern" : "jenkins-repo/*"
//                             "target" : "home/"
//                         ]
//                     }'''
//                 }
//                 cleanWs()
//             }
//         }
    }
}
