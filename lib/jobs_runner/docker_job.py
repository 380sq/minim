import docker

client = docker.DockerClient()


def build_docker_image(dockerfile, build_args, name=None):
    kwargs = {'dockerfile': dockerfile, 'build_args': build_args, 'name': name}
    client.images.build(**kwargs)


def docker_run_image(run_args, ports):
    # name
    # environment
    client.containers.run()
