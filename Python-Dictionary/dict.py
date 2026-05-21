'''
Case Study 1: The API Log Aggregator

Difficulty: Medium Nested Dicts Frequency Maps

Problem Statement

You are analyzing raw logs from an API gateway. The logs are provided as a list of
dictionaries, where each dictionary represents a single API request. Your task is to
build a nested dictionary that aggregates the count of HTTP status codes returned
for each endpoint.

Write a function that takes this list and returns a dictionary where the keys are the
endpoint strings, and the values are dictionaries mapping the status_code to its
occurrence count.

Sample Input
logs = [
 {"endpoint": "/api/users", "status": 200},
 {"endpoint": "/api/users", "status": 200},
 {"endpoint": "/api/payments", "status": 500},
 {"endpoint": "/api/users", "status": 404},
 {"endpoint": "/api/payments", "status": 200},
 {"endpoint": "/api/payments", "status": 500}
]

'''
def count_status_codes(logs):
    result = {}

    for log in logs:
        endpoint = log["endpoint"]
        status = log["status_code"]

        if endpoint not in result:
            result[endpoint] = {}

        if status not in result[endpoint]:
            result[endpoint][status] = 0

        result[endpoint][status] += 1

    return result