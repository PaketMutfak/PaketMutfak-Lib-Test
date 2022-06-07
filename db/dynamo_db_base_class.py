import boto3
import os


class PmDynamoDb:
    def __init__(self, region_name):
        try:
            aws_access_key_id = os.environ.get("aws_access_key_id")
            aws_secret_access_key = os.environ.get("aws_secret_access_key")
            self.dynamodb = boto3.resource('dynamodb',
                                           region_name=region_name,
                                           aws_access_key_id=aws_access_key_id,
                                           aws_secret_access_key=aws_secret_access_key
                                           )

            self.serializer = boto3.dynamodb.types.TypeSerializer()
            self.deserializer = boto3.dynamodb.types.TypeDeserializer()

            self.client = boto3.client('dynamodb',
                                       region_name=region_name,
                                       aws_access_key_id=aws_access_key_id,
                                       aws_secret_access_key=aws_secret_access_key)
        except ConnectionError as err:
            print(err)

        except Exception as ex:
            print(ex)

    def transaction_put(self, item, table_name, condition_expression, return_value):

        dict_put = {
            'Put': {
                'Item': item,
                'TableName': table_name,
                'ConditionExpression': condition_expression,
                'ReturnValuesOnConditionCheckFailure': return_value
            }
        }

        return dict_put

    def transaction_delete(self, key, table_name, condition_expression, return_value):

        dict_delete = {
            'Delete': {
                'Key': key,
                'TableName': table_name,
                'ConditionExpression': condition_expression,
                'ReturnValuesOnConditionCheckFailure': return_value
            }
        }

        return dict_delete

    def transaction_update(self, key, update_expression, table_name, condition_expression, expression_attribute_names,
                           expression_attribute_values, return_value):

        dict_update = {
            'Update': {
                'Key': key,
                'UpdateExpression': update_expression,
                'TableName': table_name,
                'ConditionExpression': condition_expression,
                'ExpressionAttributeNames': expression_attribute_names,
                'ExpressionAttributeValues': expression_attribute_values,
                'ReturnValuesOnConditionCheckFailure': return_value
            }
        }

        return dict_update

    def transaction_get(self, key, table_name, condition_expression):

        dict_get = {
            'Get': {
                'Key': key,
                'TableName': table_name,
                'ConditionExpression': condition_expression
            }
        }
        # 'ProjectionExpression': 'string',
        # 'ExpressionAttributeNames': {
        #     'string': 'string'
        # }

        return dict_get