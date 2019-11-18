pipeline {
    agent any
    environment {
        BUILD_ID = 'dontKillMe'
        DEPLOY_ID = 'dontKillMe'
        JENKINS_NODE_COOKIE = 'dontKillMe'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'pwd'
                sh 'sh -x ./stop.sh'
                sh 'sh -x ./start.sh'
            }
        }
    }
}