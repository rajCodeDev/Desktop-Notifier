from plyer import notification
import time


if __name__ =='__main__':
        while True:    
            notification.notify(
                  title="***  Take Rest  ***",
                  message="Rest is very important i think u takr a rest ",
                  app_icon="C:/Users/DELL/Downloads/clock",timeout=5)
            time.sleep(10)

#             from plyer import notification
# import time

# if __name__ == '__main__':
#     interval_minutes = 30  # Set the interval between notifications (in minutes)
    
#     while True:
#         notification_title = "Take a Rest"
#         notification_message = "Rest is important! Take a break and relax."
#         notification_timeout = 10  # Display time for each notification (in seconds)

#         notification.notify(
#             title=notification_title,
#             message=notification_message,
#             timeout=notification_timeout
#         )
        
#         time.sleep(interval_minutes * 60)  # Sleep for specified interval in seconds
