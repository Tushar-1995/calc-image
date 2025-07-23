pipeline {
    agent any
    triggers {
        pollSCM('*/2 * * * *')
    }
    stages{
        stage ('Build') {
            steps {
                echo "Build phase"
                powershell '''
                cd calculator-app
                python -m pip install -r requirements.txt
                '''
            }
            
        }
        stage ('Test') {
            steps {
                echo "Test phase"
                powershell '''
                cd calculator-app
                python calculator.py --test 99 1
                '''
            }
        }
        stage ('Deliver') {
            steps {
                echo "Deliver phase"
                powershell '''
                cd calculator-app
                Start-Process -NoNewWindow python -ArgumentList "calculator.py"
                '''
        }
    }
    }

    post {
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