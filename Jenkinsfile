node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}
pipeline{
    agent any
      environment {
        GIT_URL = 'https://github.com/suniljmaldiya/cvproject.git'
        GIT_BRANCH = 'main'
        //GITHUB_CREDENTIALS = 'gitgit'
        }
    stages{
        stage("code"){
            steps{
                echo "Pull code from suniljmaldiya github account"
                git url:"${GIT_URL}",branch:"${GIT_BRANCH}"//, credentialsId:"${GITHUB_CREDENTIALS}"
            }
        }
        stage("Build"){
            steps{
                echo "Building the code"
                sh "docker-compose build --build-arg CONTAINER_NAME=cvapp"
            }
        }
        stage("Deploy"){
            steps{
                echo "Deploy the code"
                sh "docker-compose down && docker-compose up -d"
            }
        }
    }
}
