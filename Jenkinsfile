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
                python -m pip install --only-binary=:all: -r requirements.txt
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
        stage('Deliver') {
            steps {
                echo "deliver phase"
                powershell '''
                cd calculator-app
                Write-Output "Starting Flask server in the background..."
                Start-Process python -ArgumentList "calculator.py" -WindowStyle Hidden -PassThru | Out-Null
                Write-Output "Server started. Allowing 10 seconds for initialization..."
                Start-Sleep -Seconds 10
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