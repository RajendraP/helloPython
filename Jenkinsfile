@Library('test@master') _

node {
    stage('Checkout'){

          checkout scm
       }

    stage('Build') {
        echoVar 'Build'
        //
    }
    // node('Master'){
    stage('Test') {
        echoVar 'Test'
        sh "mkdir -p test-results"
        sh "./functional-tests"
        finally {
            archiveArtifacts artifacts: '*.log'
            junit 'test-results/*.xml'
        }
        //
    }
    // }
    stage('Deploy') { 
        echoVar 'Deploy'
        // 
    }
}
