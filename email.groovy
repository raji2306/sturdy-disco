// emailConfig.groovy
def recipients = "rajeshsuresh154@gmail.com, rajeshsuresh230699@gmail.com"
def subject = "Build ${buildNumber} in ${jobName} - ${buildResult}"
def body = """
<p>Build Result: ${buildResult}</p>
<p>Project: ${jobName}</p>
<p>Build URL: ${buildUrl}</p>
"""

emailext(to: recipients, subject: subject, body: body)
