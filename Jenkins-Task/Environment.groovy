pipeline {
    agent any
    
    environment {
        my_var = "Hello !, Task-2"
    }
    
    stages {
        stage("Print Environment Variable"){
            steps {
                script{
                    echo "${env.my_var}"
                }
            }
        }
    }
}