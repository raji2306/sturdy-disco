@Library("shared-library") _
pipeline {
    parameters { 
        string(name: 'machine', defaultValue: 'linux', description: 'Choose the Machine that you wants to run the build') 
        string(name: 'branch', defaultValue: 'master', description: 'Choose the branch that you wants to checkout')
    }
    environment {
           my_branch = "${params.branch}"
    }
    tools {
        jdk  "java"
        maven "maven"
        jfrog "jfrog-cli"
    }
    agent any 
     triggers{
        cron('*/20 * * * *' )
       }
    stages {
        stage ("Git Checkout Stage"){
            steps {
                git branch: "${env.my_branch}" ,
                credentialsId: 'git_cred',
                url: 'git@github.com:raji2306/sturdy-disco.git'
            }
        }
        stage ("Run Shared Library to verify the Changes"){  
            steps {
                helloBuddy("rajesh", "23-0")
            }
            post {
                success {
                    echo "Fine! The stage completed successfully"
                }
            }
        }
        stage ("Running Build and Packaging Stage"){
            when{
                expression {
                    env.GIT_BRANCH == "master"
                }
            }
            steps {
                sh "mvn package"
                script {
                    if( currentBuild.currentResult == "SUCCESS" ){
                        echo "Build Stage is successful"
                    }
                    else {
                        echo "Build Stage is unsuccessful"
                    }
                }
            }
            
        }
        stage ("Uploading Generated War file to JFrog Repository"){
            steps {
//                 timeout(time: 30, unit: 'MINUTES') 
                rtServer(
                    id : "jfrog",
                    url : 'http://3.110.42.20:8082/artifactory',
                    credentialsId : 'jfrog-cred',
                    bypassProxy : true,
                    timeout: 300
                )
                rtUpload(
                    serverId :"jfrog",
//                     failNoOp: true,
                    spec : '''{
                        "files" : [
                            {
                                "pattern" : "*.war",
                                "target" : "jenkins-repo/",
                                "props" : "retention.days=11"
                            }
                        ]
                    }'''
                )
            }
//             stash name: 'jfrog', includes: 'jfrog, url, credentialsId'
        }
        stage ("Downloading Important Records from Artifactory Repo"){
            steps {
//                 unstash 'jfrog'
                rtDownload (
                    serverId : 'jfrog',
                    spec : '''{
                        "files" : [
                        {
                            "pattern" : "*-SNAPSHOT.war",
                            "target" : "mywar/"
                            }
                        ]
                    }'''
                )
                cleanWs()
            }
        }
    }
}
