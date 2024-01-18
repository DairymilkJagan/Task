pipeline {
    agent any
    
    stages {
        stage('create_dir') {
            steps {
                script {
                    bat 'if not exist jagan_dir mkdir jagan_dir'
                }
            }
        }
        
        stage('Add_file') {
            steps {
                script {
                    bat 'echo "This is a file" > jagan_dir/file.txt'
                }
            }
        }
        
        stage('add_content') {
            steps {
                script {
                    bat 'echo "append" >> jagan_dir/file.txt'
                }
            }
        }
        
        stage('display') {
            steps {
                script {
                    bat 'if exist jagan_dir\\file.txt (Type jagan_dir\\file.txt) else (echo "File not found")'
                }
            }
        }
    }
}