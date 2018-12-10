# Event Registration   

A Web Application which keeps track of an organization's event and its participants.

---

### Features:  
* Account Registration (For Administrator and Standard Account)  
* Login Account  
* Administrator gain several privileges:
  * Admin can view events and its participants
  * Admin can update event details
  * Admin can create and delete events
  * Admin can add and delete participants in event
* Standard account privileges
  * Standard users can view event details
  * Standard users can check whether they are a participant of an event

---
### Developed by:  
CAADYANG, Mark Noe Christian P.  
CARLOS, John Thomas  
CUARESMA, Dexter James L.  
ORTIZ, Ralph Christian A.  

---
### Installation Instructions:
1. Clone the repository using the following command git clone https://github.com/ThomCarlos0913/WebTechnologies.Project.git
2. Go to cloned folder using docker and run the containers using command ``` docker-compose up -d --build  ```. Wait for containers to run. Wait a few minutes for database service to initialize.
3. Initialize database by running command ``` docker-compose exec backend python app.py init_db ```
4. disable CORS policy (Reverse Proxy not added)
5. Visit the website on localhost on native docker installation or on 192.168.99.100 on docker toolbox installation

---
### Access Admin Page:
1. Login one of the following accounts:
 * Username- ThomCarlos, Password- thom123
 * Username- MarkCaadyang, Password- pogiako123
 * Username- DexterCuaresma, Password- dexter123
 * Username- RalphOrtiz, Password- ralph123
2. Click the 'EventMania' Logo on the upper left of the page
3. Welcome to the admin page

Note: Admin page page can only be accessed by the following users. Ordinary users will not be granted admin access.

---
### Known Bugs:
1. Database not starting up.
 * Somehow database is not running/initializing. Solution: run command ``` docker-compose up ``` again.
