pipeline {
    agent {
        dockerContainer {
            image 'calculator-app:latest'
            // Consider adding a 'pull: true' here if you want to ensure the latest image
            // Always ensure the image is built and pushed to a registry before using it here.
        }
    }
    triggers {
        pollSCM ('H/2 * * * *')
    }
    stages {
        stage ('Build') {
            steps {
                sh '''
                    echo "building the calculator image"
                    // Add actual build steps for your Python app here, e.g.:
                    // pip install -r requirements.txt
                    // python setup.py build
                    // If you build a NEW Docker image here, ensure it's tagged and used appropriately.
                    // For example, if 'calculator-app:latest' is built here, it should be done in this stage.
                '''
            }
        }
        stage ('Test') {
            steps {
                sh '''
                    cd calculator-app
                    // Assuming this runs actual tests and exits, not starts a server.
                    python calculator.py
                    // Consider using pytest or unittest for structured tests:
                    // python -m pytest
                '''
            }
        }
        stage ('Deploy') {
            steps {
                sh '''
                    cd calculator-app
                    echo "Starting Flask server in background for TEMPORARY check/test if needed."
                    # Use 'nohup' and capture PID if you want it to truly run in detached mode *within the container lifecycle*
                    # BUT THIS IS STILL NOT FOR LONG-TERM DEPLOYMENT.
                    # For a real deployment, you would push this image to a registry
                    # and then deploy it to a separate environment (e.g., Kubernetes, Azure App Service)

                    # Option A: If you need to start it *briefly* for an integration test within the container
                    # and then kill it:
                    python calculator.py &
                    SERVER_PID=$!
                    echo "Server started with PID: $SERVER_PID"
                    echo "Waiting for server to initialize..."
                    sleep 20 # Give it time to start up

                    # Add actual test commands here against localhost:
                    # Example: curl -f http://localhost:5000/some_endpoint || { echo "Server test failed"; exit 1; }

                    echo "Stopping the temporary Flask server..."
                    kill $SERVER_PID || true # '|| true' makes sure the step doesn't fail if the process already died
                    echo "Server stopped."

                    # Option B: (Recommended for actual deployment)
                    # Instead of running the server here, you would typically:
                    # 1. Build and tag the Docker image (if not done in 'Build' stage)
                    # docker build -t your_repo/calculator-app:$BUILD_NUMBER .
                    # 2. Push the Docker image to a registry (e.g., Docker Hub, Azure Container Registry)
                    # docker push your_repo/calculator-app:$BUILD_NUMBER
                    # 3. Deploy the image to your target environment (e.g., Kubernetes cluster, Azure App Service)
                    # kubectl apply -f kubernetes_deployment.yaml
                    # az webapp deploy ...
                '''
            }
        }
    }
    post {
        always {
            // Ensure the artifact path is correct relative to the workspace.
            // If calculator-app is the root of your repo clone in the workspace:
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