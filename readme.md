# Gingerbread Scanner (gbscan)
Created and (hopefully) maintained by theGingerbreadMan.

## TODO
* [x] Flask main web app
* [x] Implement simple webshell for testing
* [ ] Implement installer for cmd in path (?)
* Organize file structure
    * [x] command line arg for project directory
    * [x] `.gbscan` directory in project folder (root)
    * [x] Subdirs: `nmap`, `gobuster`, etc.
* Store command line history
    * [ ] Categorize by type (eg. web, ssh, smb, etc.)
    * [ ] Store in sqlite3 db
    * [ ] Clean displayh for transparency & learning purposes
* nmap
    * [ ] standardize commands (`-F`, `-sC -sV`, `-p-`)
    * [ ] prettify output
    * [ ] parse output
* Services
    * [ ] Organize results by port
    * [ ] Offer port labels/suggestions
* [ ] Store Users & Creds (sqlite3)