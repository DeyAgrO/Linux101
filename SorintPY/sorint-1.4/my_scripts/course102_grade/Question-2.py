import subprocess

def check_is_enabled(service):
    try:
        result = subprocess.run(['systemctl', 'is-enabled', service], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode().strip() == 'enabled'
    except subprocess.CalledProcessError:
        return False

def check_is_disabled(service):
    try:
        result = subprocess.run(['systemctl', 'is-enabled', service], check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode().strip() == 'disabled'
    except subprocess.CalledProcessError:
        return False

def check_is_inactive(service):
    try:
        result = subprocess.run(['systemctl', 'is-active', service], check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode().strip() == 'inactive'
    except subprocess.CalledProcessError:
        return False

def grade():
    sshd_enabled = check_is_enabled('sshd.service')
    chronyd_disabled = check_is_disabled('chronyd.service')
    httpd_stopped = check_is_inactive('httpd.service')

    if sshd_enabled:
        print("\033[92msshd.service is enabled.\033[0m")
    else:
        print("\033[91msshd.service is not enabled\033[0m")

    if chronyd_disabled:
        print("\033[92mchronyd.service is disabled.\033[0m")
    else:
        print("\033[91mchronyd.service is not disabled\033[0m")

    if httpd_stopped:
        print("\033[92mhttpd.service is stopped.\033[0m")
    else:
        print("\033[91mhttpd.service is not stopped\033[0m")

if __name__ == "__main__":
    grade()
