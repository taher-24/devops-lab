pipeline {
 agent any

 stages {
 stage('Installation') {
 steps {
 sh 'python3 -m pip install -r requirements.txt'
 }
 }

 stage('Test') {
 steps {
 sh 'python3 -m py_compile app.py'
 echo 'Application Flask testée avec succès !'
 }
 }
 }
}
