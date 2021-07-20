# ssh-alert-service
 
### Before install edit next:

- ```conf.py``` change: `CHAT_ID` `BOT_API` `CAR_NAME`

- `checker_who.service` change: `WorkingDirectory` and `ExecStart`
***
  
### Make .py file as service
create file or copy edited ```checker_who.service```: 

example:  
```nano /etc/systemd/system/YOUR_SERVICE.service```
