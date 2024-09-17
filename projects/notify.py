from plyer import notification
title="Notification"
message="This is a simple notification"
notification.notify(
    title=title,
    message=message,
    app_name="Python",
    timeout=5
)