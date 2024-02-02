# FlyteFabric

A template for the recommended layout of a Flyte enabled repository for code written in python using [flytekit](https://docs.flyte.org/projects/flytekit/en/latest/).

## Usage

To get up and running with your Flyte project, we recommend following the
[Flyte getting started guide](https://docs.flyte.org/en/latest/getting_started.html).

We recommend using a git repository to version this project, so that you can
use the git sha to version your Flyte workflows.

## Dependency Installation

This project uses poetry. Please use the below commands to setup the poetry project.

```bash
conda create -n flytefabric python=3.9
conda activate flytefabric
pip install poetry==1.6.1
poetry install
```

## Build and Deploy on Flyte

Please follow the below instructions to build the docker and push it to your AWS public repo.

Make sure you have 

- Flyte installed
- Docker installed
- AWS account
    - AWS access key 
    - AWS secret key 
    - S3 bucket and 
    - Athena table in AWS. 


Once all the requirements are met update the workflow you want to run and build. 

``` bash
- [ ] docker build -t flytetest:latest .  
- [ ] docker images
- [ ] docker image tag flytetest:latest public.ecr.aws/<publicrepo>/flyte:latest 
- [ ] docker image push public.ecr.aws/<publicrepo>/flyte:latest 


- [ ] pyflyte --pkgs workflows package --image public.ecr.aws/<publicrepo>/flyte:latest -f
- [ ] aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/<publicrepo>
- [ ] git rev-parse HEAD 
- [ ] export FLYTECTL_CONFIG=/Users/zlak/.flyte/config-sandbox.yaml 
- [ ] flytectl register files --project my-project  --domain development  --archive flyte-package.tgz --version "${git rev-parse HEAD}"

```