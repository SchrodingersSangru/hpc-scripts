import psutil

def get_process_status(pid):
    try:
        process = psutil.Process(pid)
        return process.status()
    except psutil.NoSuchProcess:
        return "Process not found"
    except psutil.AccessDenied:
        return "Access denied"

def main():
    pid_to_check = 86830  # Replace with the PID of the process you want to check
    status = get_process_status(pid_to_check)
    
    print(f"Process with PID {pid_to_check} is {status}")

if __name__ == "__main__":
    main()
