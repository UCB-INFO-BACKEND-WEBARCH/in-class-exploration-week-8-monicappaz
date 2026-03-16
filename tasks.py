from rq.decorators import job
from redis import Redis
import os
import time # For sleep func

redis_conn = Redis.from_url(
    os.getenv("REDIS_URL", "redis://localhost:6379/0")
    )

@job('notifications', connection = redis_conn)
def send_notification(notification_id, email, message):
    # Print message when starting
    print(f"Sending notification {notification_id} to {email}: {message}")

    # Sleep for 3 seconds (to sim slow email API)
    time.sleep(3)

    # Print message when done
    print(f"Notification {notification_id} sent to {email}")
    
    # Return dict with notif_id, email, status, and sent_at
    return {
        "notification_id": notification_id,
        "email": email,
        "status": "sent",
        "sent_at": time.time()
    }