import requests
import logging
import time
from datetime import datetime
import os
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# API endpoints to check
ENDPOINTS = [
    {
        'name': 'User Service',
        'url': os.getenv('USER_SERVICE_URL', 'http://localhost:8000'),
        'endpoints': [
            '/',
            '/users/',
            '/ask',
            '/users/1'
        ]
    }
]

def check_endpoint(base_url, endpoint):
    """Check a single endpoint and return the result."""
    url = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"
    try:
        start_time = time.time()
        response = requests.get(url) if endpoint != '/ask' else requests.post(
            url,
            json={'question': 'What is the current time?'}
        )
        response_time = time.time() - start_time
        
        return {
            'status': 'success' if response.status_code == 200 else 'failure',
            'status_code': response.status_code,
            'response_time': response_time,
            'timestamp': datetime.now().isoformat()
        }
    except Exception as e:
        return {
            'status': 'error',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }

def run_health_checks():
    """Run health checks for all configured endpoints."""
    results = []
    
    for service in ENDPOINTS:
        service_results = {
            'service': service['name'],
            'base_url': service['url'],
            'checks': []
        }
        
        for endpoint in service['endpoints']:
            # Run 5 checks for each endpoint
            for i in range(5):
                result = check_endpoint(service['url'], endpoint)
                result['endpoint'] = endpoint
                result['check_number'] = i + 1
                service_results['checks'].append(result)
                
                # Log the result
                if result['status'] == 'success':
                    logger.info(f"Check {i+1} for {endpoint}: Success (Status: {result['status_code']}, Response Time: {result['response_time']:.2f}s)")
                else:
                    logger.error(f"Check {i+1} for {endpoint}: Failed - {result['error']}, Status code: {result['status_code']}")
                
                # Wait 1 second between checks
                time.sleep(1)
        
        results.append(service_results)
    
    return results

def main():
    """
    Main function that will be called by Choreo's scheduled task.
    This is the entry point for the scheduled task.
    """
    try:
        logger.info("Starting health checks...")
        results = run_health_checks()
        logger.info("Health checks completed successfully.")
        return {
            "status": "success",
            "message": "Health checks completed successfully",
            "results": results
        }
    except Exception as e:
        logger.error(f"Error during health checks: {str(e)}")
        return {
            "status": "error",
            "message": f"Error during health checks: {str(e)}"
        }

if __name__ == "__main__":
    main() 