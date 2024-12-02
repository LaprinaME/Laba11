pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q --junitxml=report.xml'
            }
        }

        stage('Archive Test Results') {
            steps {
                archiveArtifacts artifacts: 'report.xml', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            junit 'report.xml'
        }
    }
}
