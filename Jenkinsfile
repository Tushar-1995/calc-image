pipeline {
    agent {
        docker {
            image 'calculator-app:latest'
        }
    }
    triggers {
        pollSCM ('H/2 * * * *')
    }
    stages {
        stage ('Build') {
            steps {
                sh '''
                echo "building the calcultor image"
                '''
            }   
        }stage ('Test') {
            steps {
                sh '''
                cd calculator-app
                python3 calculator.py
                '''
            }
            
        }stage ('Deploy') {
            steps {
                sh '''
                cd calculator-app
                echo "starting flask server in the container"
                python3 calulator.py &
                echo "waiting for server to initialize"
                sleep 20
                '''
            }
        }
    }post {
        always {
            archiveArtifacts artifacts: 'calculator-app/*', allowEmptyArchive: true
        }
        failure {
            echo 'Build failed due to script or file issues.'
        }
        success {
            echo 'Build completed successfully!'
        }
    }
}