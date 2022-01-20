# aws-cli

docker container for execute aws cli

## setup
copy env file
```
$ cp conf/.env.example conf/.env
```
add your aws credential
```
$ vi conf/.env
```

## starting
run aws-cli container
```
$ docker-compose up -d
```
MFA login to aws
```
$ docker-compose exec aws-cli python login-aws.py
Enter your token code: <MFA Token>
```
entry aws-cli container
```
$ docker-compose exec aws-cli bash
```

## tips
Decode Command
```
$ aws sts decode-authorization-message --encoded-message file://example
```
- If an error message of `AWS_ACTION_NAME with an explicit deny` is displayed when executing the command, temporarily detach `IAM_MUST_MFA` from `InfraEngineer-Write` and execute it again.
- After successful decoding, return to the current policy by attaching `IAM_MUST_MFA` of` InfraEngineer-Write`.

Mounting files
* If you place the source code under the src directory, it will be mounted in the container
```
cp -r {mount target directory}/* ./src
```