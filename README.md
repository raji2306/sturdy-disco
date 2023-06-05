# Kubernetes Step by step process to use the manifest files

Step 1 : Install the AWS CLI and then configure it using Secret and Access Key { Verify the IAM user with "aws iam list-users" command }

Step 2 : Install and configure Kubectl { Ref : https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html }

Step 3 : Install eksctl { ref : https://eksctl.io/ }

Commands :

sudo curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | sudo tar xz -C /tmp

sudo mv /tmp/eksctl /usr/local/bin

eksctl version

Step 4 : Install AWS IAM Authenticator { Ref : https://docs.aws.amazon.com/eks/latest/userguide/install-aws-iam-authenticator.html }

Step 5 : Run below command to create Cluster 

eksctl create cluster -f file_name

