pipeline {
    agent any
    
    stages {
        stage("Git rep") {
            steps {
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/DairymilkJagan/Task'
            }
        }
    }
}