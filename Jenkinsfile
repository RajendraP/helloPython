@Library('test@master') _

node {  
    stage('Build') { 
        echoVar 'Build'
        // 
    }
    stage('Test') { 
        echoVar 'Test'
        sh functional-tests
        // 
    }
    stage('Deploy') { 
        echoVar 'Deploy'
        // 
    }
}
