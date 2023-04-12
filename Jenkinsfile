pipeline {
    agent any
    
    environment {
        ANSIBLE_HOST_KEY_CHECKING = "False"
    }

    stages {
       stage('Deploy') {
            steps {
                echo 'Running Playbook'
                ansiblePlaybook become: true, credentialsId: 'github', inventory: 'host.ini', playbook: 'flask-dep.yml'
            }
        }
    }
}
