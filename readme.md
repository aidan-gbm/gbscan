# Gingerbread Scanner (gbscan)
Created and (hopefully) maintained by theGingerbreadMan.

## Usage
Clone the repository, make a separate directory for your project, and run the application.

```
user@host:~$ python3 app.py <Project Directory>
```

## TODO
* [ ] Graphical network depiction
* [ ] Implement installer for cmd in path (?)
* [ ] Move to deployment? ([documentation](https://flask.palletsprojects.com/en/1.1.x/deploying/))
* Update database
    * [x] Targets table (name/ip/notes)
    * [ ] Credentials table (user/service/password)
    * [ ] Services table (tgt_name/port/service)
* Store command line history
    * [ ] Categorize by type (eg. web, ssh, smb, etc.)
    * [ ] Store in sqlite3 db
    * [ ] Clean display for transparency & learning purposes
* Update display
    * [ ] Alerts/notifications ([bootstrap](https://getbootstrap.com/docs/4.5/components/alerts/))
    * [ ] Better buttons
* Services
    * [ ] gobuster module
    * [ ] sql module
    * [ ] smb module
    * [ ] smtp module
    * [ ] ldap module
    * [ ] kerberos module
