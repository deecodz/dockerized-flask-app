pipeline {
    agent any

    stages {
       stage('Deploy') {
            steps {
                echo 'Running Playbook'
                ansiblePlaybook become: true, credentialsId: 'github', inventory: '/home/ubuntu/assignment/host.ini', playbook: '/home/ubuntu/assignment/flask-dep.yml'
            }
        }
    }
}
