pipeline {
    agent any

    environment {
        PYTHONPATH = '.'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'master', url: 'https://github.com/Sherif-Youssef/Cloud-Computing-Task-4.git'
            }
        }

        stage('Set Up Python') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install pytest'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'pytest tests/'
            }
        }
    }

    post {
        success {
            echo 'All tests passed.'
        }

        failure {
            echo 'Tests failed.'
        }
    }
}