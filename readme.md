# Gingerbread Scanner (gbscan)
Created and (hopefully) maintained by theGingerbreadMan.

## TODO
* Flask (?) main web app
* Implement simple command line control from web
* Implement installer for cmd in path (?)
* Organize file structure
    * command line arg for project directory?
    * specify project directory from web (maybe store in class?)
    * `.gbscan` directory in project folder (root)
    * Subdirs: `nmap`, `gobuster`, `nikto` (dep?)
* Store command line history
    * Categorize by type (eg. web, ssh, smb, etc.)
    * Store in sqlite3 db
    * Clean displayh for transparency & learning purposes
* nmap
    * standardize commands (`-F`, `-sC -sV`, `-p-`)
    * prettify output
    * parse output
* Services
    * Organize results by port
    * Offer port labels/suggestions
* Store Users & Creds (sqlite3)