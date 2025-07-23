pipeline {
    agent any
    triggers {
        pollSCM('* 2 * * * *')
    }
    stages{
        stage ('Build') {
            steps{
                echo "Build phase"
            }
            
        }
        stage ('Test') {
            steps {
                echo "Test phase"
            }
        }
        stage ('Deliver') {
            steps {
            echo "Deliver phase"
        }
    }
}

    post {
        always {
            echo "This will always run"
        }
        success {
            echo "This will run only if the pipeline is successful"
        }
        failure {
            echo "This will run only if the pipeline fails"
        }
    }
}