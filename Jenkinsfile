pipeline {
    agent {
        dockerContainer {
            image 'calculator-app:latest'
            // Removed 'args' since it's not supported
        }
    }
    triggers {
        pollSCM('H/2 * * * *')  // Poll SCM every 2 minutes
    }
    stages {
        stage('Build') {
            steps {
                sh '''
                    set -x
                    echo "Building the calculator image"
                    cd calculator-app && docker build -t calculator-app:latest .
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    set -x
                    cd calculator-app
                    python calculator.py --test 5 3
                '''
            }
        }
        stage('Deploy') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    sh '''
                        set -x
                        echo "Starting Flask server in a detached Docker container on the host"
                        /c/Program\\ Files/Docker/Docker/resources/bin/docker.exe run -d -p 5000:5000 --name calculator-server calculator-app:latest
                        echo "Waiting for server to initialize"
                        sleep 20
                    '''
                }
            }
        }
    }
    post {
        always {
            sh '/c/Program\\ Files/Docker/Docker/resources/bin/docker.exe stop calculator-server || true && /c/Program\\ Files/Docker/Docker/resources/bin/docker.exe rm calculator-server || true'
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