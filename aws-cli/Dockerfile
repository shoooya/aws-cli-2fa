# AWS ドキュメント - AWS CLI のインストール
# https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/cli-chap-install.html

FROM python:3.6

ARG pip_installer="https://bootstrap.pypa.io/get-pip.py"

# install command.
RUN apt-get update && apt-get install -y less vim groff docker.io

# create local bin directory
RUN mkdir -p /root/.local/bin
ENV PATH $PATH:/root/.local/bin

# install aws-cli
RUN pip install --upgrade awscli

# install sam
RUN pip install --upgrade aws-sam-cli

RUN pip3 install --upgrade boto3

WORKDIR /root
