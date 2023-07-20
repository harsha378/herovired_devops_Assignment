import psutil
import time

def monitor_cpu(threshold):
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)

            if cpu_usage > threshold:
                print(f"Alert: CPU usage exceeded {threshold}% - Current CPU usage: {cpu_usage}%")

    except KeyboardInterrupt:
        print("Monitoring stopped by the user.")
    except psutil.Error as e:
        print(f"Error occurred: {e}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

if __name__ == "__main__":
    threshold = 80  # Change this value to set the desired threshold (e.g., 80%)
    monitor_cpu(threshold)
