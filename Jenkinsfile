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