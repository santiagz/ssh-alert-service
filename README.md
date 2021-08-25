# ssh-alert-service
![Supported Python versions](https://img.shields.io/badge/python-3.9-green.svg)
 
### Change the following values before installing:

- ```conf.py``` change: `CHAT_ID` `BOT_API` `CAR_NAME`

- `checker_who.service` change: `WorkingDirectory` and `ExecStart`
***
  
### Make .py file as service
edit this file: ```checker_who.service``` and copy to: `/etc/systemd/system/`
it is also possible to create a file at the final path with permission

example:  
```nano /etc/systemd/system/YOUR_SERVICE.service```

don't forget: `systemctl enable YOUR_SERVICE.service`
and: `systemctl start YOUR_SERVICE.service`
