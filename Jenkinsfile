@Library('test@master') _

node {  
    stage('Build') { 
        echoVar 'Build'
        // 
    }
    stage('Test') { 
        echoVar 'Test'
        sh 'python3 -m pytest src/test/'
        // 
    }
    stage('Deploy') { 
        echoVar 'Deploy'
        // 
    }
}
