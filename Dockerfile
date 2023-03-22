# You can pull this base image from Docker hub ( Simple html page - Default port 80 )
FROM raji2306/mynginximage:23

# Important updates and setting Open-SSH server of auth purpose
RUN apt-get upgrade -y && \
    apt-get update -y && \
    apt-get install -qy openssh-server && \
    sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd && \
    mkdir -p /var/run/sshd && \
    useradd  -p "" jenkins && \
    echo "jenkins:password" | chpasswd && \
    mkdir /home/jenkins/ && \
    mkdir /home/jenkins/.ssh

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

copy authorized_keys /home/jenkins/.ssh/

RUN chown -R jenkins:jenkins /home/jenkins/.ssh/

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]


