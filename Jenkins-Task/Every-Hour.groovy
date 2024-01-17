pipeline {
    agent any
    triggers {
        cron('H * * * *')
    }
    
    stages {
        stage('Every Hour') {
            steps {
                script {
                    echo 'Hi, Every Hour'
                }
            }
        }
    }
}