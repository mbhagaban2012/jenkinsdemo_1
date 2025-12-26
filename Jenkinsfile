pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Program Files\\Python314'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat "\"%PYTHON%\\python.exe\" --version"
                bat 'python --version'
            }

        }

        stage('Extract') {
            steps {
                bat "${env.PYTHON} extract.py"
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}


