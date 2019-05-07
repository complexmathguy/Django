pipeline {
    agent { docker { image 'python:3.7' } }
        
    stages {
        stage('install') {
            steps {
                sh 'pip install pipenv'
                sh 'pipenv install'
                sh 'pipenv install Django'
                sh 'pipenv install pytest-django'
            }
        }
        stage('test') {
            steps {
                sh 'pipenv run pytest --junitxml=test-results/junit.xml djangodemo/tests'
            }
        }
    }
}