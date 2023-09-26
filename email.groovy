def recipients = "rajeshsuresh154@gmail.com, rajeshsuresh230699@gmail.com"
def subject = "Build ${BUILD_NUMBER} in ${JOB_NAME}"
def body = """
<p>Build Result: ${BUILD_RESULT}</p>
<p>Project: ${PROJECT_NAME}</p>
<p>Build URL: ${BUILD_URL}</p>
"""

emailext(to: recipients, subject: subject, body: body)
