# Created by houssem at 03/12/2020
Feature: Docker test
  This feature allow to build docker images
  and run docker. It allows to automate images.


  Scenario: Build docker image from dockerfile path
    Given I have a dockerfile path.
    Then I should build an image with the docker file.