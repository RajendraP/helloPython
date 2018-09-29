def jiraprojectName = 'IPF'
def jiraComponent = 'bs35'

@Library('test@master') _

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
            //archiveArtifacts artifacts: '*.log'
            junit 'test-results/*.xml'
            //jira jiraprojectName, jiraComponent, resultsfilePath
        }
        //jira jiraprojectName, jiraComponent, resultsfilePath
        //
    }
    stage('Deploy') { 
        echoVar 'Deploy'
        // 
    }
}
