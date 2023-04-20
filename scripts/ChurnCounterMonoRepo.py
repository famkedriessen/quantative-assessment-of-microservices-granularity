import fileinput
import os

serviceName = "metadata-rest-app"

with open(r"logfiles\metadata\refactor 2\overig\graphql-app_rest-app.log", 'r') as file:
    churn = 0
    for line in file:
        if serviceName in line:
            churn = churn + 1
    print("churn " + serviceName + " = " + str(churn))
