pipeline {
    agent any
    
    stages {
        stage('Print Text') {
            steps {
                echo 'Hi ! I am JAGAN, From Namakkal.'
            }
        }
    }
}