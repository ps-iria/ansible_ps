pipeline {
    agent {
      label 'ansible'
    }
    stages{
        stage('Git checkout') {
            steps {
                sh 'mkdir -p gitproject'
                sh 'cd gitproject'
                git credentialsId: '27c0218d-ab30-4d22-8726-4c1f3e44ea6e', url: 'git@github.com:ps-iria/vector-role.git'
                }
        }
        stage('Install molecule') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run molecule') {
            steps {
                sh 'molecule test'
            }
        }
    }
}