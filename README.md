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
4. disable CORS policy
5. Visit the website on localhost on native docker installation or on 192.168.99.100 on docker toolbox installation
