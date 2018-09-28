def jiraprojectName = 'IPF'
def jiraComponent = 'bs35'

@Library('test@master') _

node {
    def workspace = pwd();
    def resultsfilePath = '${workspace}/test-results/TestResults.xml'
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
