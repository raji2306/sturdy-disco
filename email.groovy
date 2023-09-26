// emailConfig.groovy
def call(Map config) {
    def recipients = "rajeshsuresh154@gmail.com, rajeshsuresh230699@gmail.com"
    def subject = "Build ${config.buildNumber} in ${config.jobName} - ${config.buildResult}"
    def body = """
    <p>Build Result: ${config.buildResult}</p>
    <p>Project: ${config.jobName}</p>
    <p>Build URL: ${config.buildUrl}</p>
    """

    emailext(to: recipients, subject: subject, body: body)
}
