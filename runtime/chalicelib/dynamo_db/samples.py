def auto_incre():
    resp = client.update_item(
        TableName="GitHubTable",
        Key={
            "PK": {"S": "REPO#alexdebrie#dynamodb-book"},
            "SK": {"S": "REPO#alexdebrie#dynamodb-book"},
        },
        UpdateExpression="SET #count = #count + :incr",
        ExpressionAttributeNames={
            "#count": "IssuesAndPullRequestCount",
        },
        ExpressionAttributeValues={":incr": {"N": "1"}},
        ReturnValues="UPDATED_NEW",
    )
    current_count = resp["Attributes"]["IssuesAndPullRequestCount"]["N"]
    resp = client.put_item(
        TableName="GitHubTable",
        Item={
            "PK": {"S": "REPO#alexdebrie#dynamodb-book"},
            "SK": {"S": f"ISSUE#{current_count}"},
            "RepoName": {"S": "dynamodb-book"},
        },
    )


def scan_and_update():
    last_evaluated = ""
    while True:
        params = {
            "TableName": "GithubModel",
            "FilterExpression": "#type IN (:user, :org)",
            "ExpressionAttributeNames": {"#type": "Type"},
            "ExpressionAttributeValues": {
                ":user": {"S": "User"},
                ":org": {"S": "Organization"},
            },
        }
        if last_evaluated:
            params["ExclusiveStartKey"] = last_evaluated
            results = client.scan(**params)
        for item in results["Items"]:
            client.update_item(
                TableName="GitHubModel",
                Key={"PK": item["PK"], "SK": item["SK"]},
                UpdateExpression="SET #gsi1pk = :gsi1pk, #gsi1sk = :gsi1sk",
                ExpressionAttributeNames={"#gsi1pk": "GSI1PK", "#gsi1sk": "GSI1SK"},
                ExpressionAttributeValues={
                    ":gsi1pk": item["PK"],
                    ":gsi1sk": item["SK"],
                },
            )
            if not results["LastEvaluatedKey"]:
                break
            last_evaluated = results["LastEvaluatedKey"]
