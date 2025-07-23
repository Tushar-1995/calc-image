pipeline {
    agent any
    triggers {
        pollSCM('* 2 * * * *')
    }
    stages{
        stage ('Build') {
            echo "Build phase"
        }
        stage ('Test') {
            echo "test phase"
        }
        stage ('Deliver') {
            echo "Deliver phase"
        }
    }
}