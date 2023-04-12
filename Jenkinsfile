pipeline {
    agent any

    stages {
       stage('Deploy') {
            steps {
                echo 'Running Playbook'
                ansiblePlaybook become: true, credentialsId: 'github', inventory: '~/assignment/host.ini', playbook: '~/assignment/flask-dep.yml'
            }
        }
    }
}
