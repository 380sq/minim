import os

from pytest_bdd import scenario, given, when, then

from lib.runner.docker_job import build_docker_image


@given("I have a dockerfile path.")
def step_impl():
    build_docker_image(os.path.join(os.getcwd(), 'Dockerfile'), {}, 'mini-ci')


@then("I should build an image with the docker file.")
def step_impl():
    raise NotImplementedError(u'STEP: Then I should build an image with the docker file.')