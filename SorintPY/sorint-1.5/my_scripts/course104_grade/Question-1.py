import subprocess

# Define the services to check
services = ['nginx', 'httpd', 'mysqld']

# Function to check the status of a service
def check_service_status(service):
    try:
        # Run the command and capture output
        result = subprocess.run(['systemctl', 'is-active', service], 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE, 
                                 text=True)

        # Check the result and print the appropriate message
        if result.stdout.strip() == 'active':
            print(f"\033[92m{service} is successfully activated.\033[0m")  # Green text
        else:
            print(f"\033[91m{service} is not activated. Please check the logs again.\033[0m")  # Red text

    except Exception as e:
        print(f"An error occurred while checking {service}: {e}")

# Check each service
# for service in services:
#     check_service_status(service)

def grade():
    for service in services:
        check_service_status(service)

if __name__ == "__main__":
    grade()