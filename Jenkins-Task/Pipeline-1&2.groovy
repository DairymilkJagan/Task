pipeline {
    agent any
    
    stages {
        stage('Stage 1') {
            steps {
                script {
                    echo "Hi , I am Jagan"
                }
            }
        }
        
        stage('Trigger Pipeline-2') {
            steps {
                script {
                    Native= "Namakkal"
                    build job: 'Pipeline-2', parameters: [string(name: 'Value', value: Native)], wait: false
                }
            }
        }
    }
}

pipeline {
    agent any
    
    parameters {
        string(name: 'Value', defaultValue: '', description: 'Value from Pipeline1')
    }
    
    stages {
        stage('Pipeline 2 Stage 1') {
            steps {
                script {
                    echo "I am from  ${params.Value}"
                }
            }
        }
    }
}