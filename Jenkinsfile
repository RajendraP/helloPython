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
        sh "./functional-tests"
        //
    }
    // }
    stage('Deploy') { 
        echoVar 'Deploy'
        // 
    }
}
