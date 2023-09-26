def recipients = "rajeshsuresh154@gmail.com, rajeshsuresh230699@gmail.com"
def buildNumber = env.BUILD_NUMBER
def jobName = env.JOB_NAME
def buildResult = currentBuild.resultIsBetterOrEqualTo('SUCCESS') ? 'SUCCESS' : 'FAILURE'
def buildUrl = env.BUILD_URL

emailScript(buildNumber: buildNumber, jobName: jobName, buildResult: buildResult, buildUrl: buildUrl)

// Define a separate stage or step for the email sending logic if needed.
