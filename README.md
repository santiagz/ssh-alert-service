# ssh-alert-service
 
### Before install edit next:

- ```conf.py``` change: `CHAT_ID` `BOT_API` `CAR_NAME`

- `checker_who.service` change: `WorkingDirectory` and `ExecStart`
***
  
### Make .py file as service
edit this file: ```checker_who.service``` and copy to: `/etc/systemd/system/`
it is also possible to create a file at the final path with permission

example:  
```nano /etc/systemd/system/YOUR_SERVICE.service```
