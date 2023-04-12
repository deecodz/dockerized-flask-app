pipeline {
    agent any

    stages {
       stage('Deploy') {
            steps {
                echo 'Running Playbook'
                ansiblePlaybook become: true, credentialsId: 'github', inventory: 'host.ini', playbook: 'flask-dep.yml'
            }
        }
    }
}
