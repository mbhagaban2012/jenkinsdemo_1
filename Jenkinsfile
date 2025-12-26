pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Program Files\\Python314\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat "\"%PYTHON%\" --version"
                // bat 'python --version'
            }

        }

        stage('Extract') {
            steps {
                bat '\"%PYTHON%\" extract.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}


