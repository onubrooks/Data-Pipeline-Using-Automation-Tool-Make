import json
import ETL

def lambda_handler(event, context):
    try:
        # Get the POST body data
        body = event['body']
    
        # Parse the JSON data
        data = json.loads(body)
        numeric_cols = ['coverage_estimate', 'population_sample_size']
        result = ETL.etl(data, numeric_cols)
        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }
    except KeyError as e:
        # Handle missing keys in the JSON data
        return {
            'statusCode': 400,
            'body': json.dumps(f'Missing key: {e.args[0]}')
        }
    except ValueError as e:
        # Handle invalid JSON data
        return {
            'statusCode': 400,
            'body': json.dumps(f'Invalid JSON data: {e}')
        }
    except Exception as e:
        # Handle other unexpected errors
        return {
            'statusCode': 500,
            'body': json.dumps(f'Internal server error: {e}')
        }