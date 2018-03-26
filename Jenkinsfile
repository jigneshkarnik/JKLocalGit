node {
    try {
        stage('Build') {        
            echo pwd
            sh "cd JKLocalGit"
            sh "sudo git pull origin master"
            echo 'Dev Good'
        }
       stage('Deploy To Test') {
           sh "sshpass -p mininet scp JKMiniTopo.py mininet@192.168.242.131:./mininet/examples/test/"  
           echo 'Deploy!'
        }
        stage('Test'){
            sh "sshpass -p mininet ssh -o 'StrictHostKeyChecking=no' mininet@192.168.242.131 \"sudo ./mininet/examples/test/JKMiniWrap.py\""
            echo 'good test!'
        }
        echo 'This will run only if successful'
    } catch (e) {
        echo 'This will run only if failed'

        // Since we're catching the exception in order to report on it,
        // we need to re-throw it, to ensure that the build is marked as failed
        throw e
    } finally {
        def currentResult = currentBuild.result ?: 'SUCCESS'
        if (currentResult == 'UNSTABLE') {
            echo 'This will run only if the run was marked as unstable'
        }

        def previousResult = currentBuild.previousBuild?.result
        if (previousResult != null && previousResult != currentResult) {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }

        echo 'This will always run'
    }
}
