def call(Map config) {
    def recipients = "rajeshsuresh154@gmail.com, rajeshsuresh230699@gmail.com"
    def subject = "Build ${config.buildNumber} in ${config.jobName} - ${config.buildResult}"
    def body = """
    Build Result: ${config.buildResult}
    Project: ${config.jobName}
    Build URL: ${config.buildUrl}
    """

    // Use the mail step to send the email
    mail(
        to: recipients,
        subject: subject,
        body: body
    )
}
