import json

def lambda_handler(event, context):
    try:
        # Extract numbers from event payload
        numbers = event.get("numbers", [])
        
        # Validate input
        if not isinstance(numbers, list) or not all(isinstance(num, int) for num in numbers):
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid input. Provide a list of integers."})
            }
        
        # Calculate sum of even numbers
        even_sum = sum(num for num in numbers if num % 2 == 0)
        Print(event_sum)
        return {
            "statusCode": 200,
            "body": json.dumps({"even_sum": even_sum})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
