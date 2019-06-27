
@Library('test@add_jiraId') _

node {
    def workspace = pwd();
    def resultsfilePath = "${workspace}/test-results/TestResults.xml"
    stage('git checkout'){

         // checkout scm
         //git url: 'https://github.com/RajendraP/helloPython.git'
         checkout scm: [$class: 'GitSCM',
         branches: [[name: '*/master']],
         userRemoteConfigs: [[url: 'https://github.com/RajendraP/helloPython.git']]]
      }
    stage('Build') {
        echoVar 'Build'
        //
        //input 'Ready to go?'
    }

    stage('Test') {
        echoVar 'Test'
        try{
            sh "mkdir -p test-results"
            sh "./functional-tests"
        }
        finally {
            archiveArtifacts artifacts: '*.log, test-results/*.xml'
            junit 'test-results/*.xml'

        }
    }
    stage('Deploy') {
        echoVar 'Deploy'
        //
    }
}
