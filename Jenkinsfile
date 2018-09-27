def jiraprojectName = 'IPF'
def jiraComponent = 'bs35'
def resultsfilePath = 'test-results/TestResults.xml'

@Library('test@master') _

node {
    stage('Checkout'){

          checkout scm
       }

    stage('Build') {
        echoVar 'Build'
        //
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
            jira jiraprojectName, jiraComponent, resultsfilePath
        }
        //jira jiraprojectName, jiraComponent, resultsfilePath
        //
    }
    stage('Deploy') { 
        echoVar 'Deploy'
        // 
    }
}
