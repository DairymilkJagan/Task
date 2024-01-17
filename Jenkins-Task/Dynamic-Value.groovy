pipeline {
    agent any
    
    parameters {
        string (defaultValue: 'Hello World', description: 'choose your Name', name:'name')
    }

    stages {
        stage('Param Demo') {
            steps {
                script {
                    echo "Hi ${name}, Welcome"
                }
            }
        }
    }
}