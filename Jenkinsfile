
pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -v'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                sh 'python monitor.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'drift_report.html',
                             allowEmptyArchive: true
        }
    }
}
