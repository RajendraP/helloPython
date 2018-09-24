@Library('test@master') _

node {  
    stage('Build') { 
        echoVar 'Build'
        // 
    }
    stage('Test') { 
        echoVar 'Test'
        sh 'pytest /src/test/'
        // 
    }
    stage('Deploy') { 
        echoVar 'Deploy'
        // 
    }
}
