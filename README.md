# Communitree: DRF Crowdfunding Project


Communitree is a <insert here>

<br>

---
## **TL:DR Links**
---
<br>

### **MVP Submission:**
  - Submission Document (Canva): https://tinyurl.com/kg-drf-mvp-submission
  - User Flow-Chart (Figma): https://tinyurl.com/kg-drf-mvp-userflow
  
### **Part A Submission:** 
  - Deployed Project (Fly): https://icy-dew-540.fly.dev/projects/
  - Submission Document (Canva): https://tinyurl.com/kg-drf-part-a-submission
  - Insomnia Export (Canva): <insert>
  - Insomnia Screenshots (Canva): https://tinyurl.com/kg-drf-insomnia-screenshots
  - Insomnia Walk-through (Loom video):
  - Browsable API Walk-through (Loom video):

<br>

---
## **Features**
---
<br>

### **User Accounts**

- [X] Username
- [X] Email Address
- [X] Password

<br>

### **Project**

- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Target Amount to Fundraise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
- [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge

<br>

### <b>Implement suitable update delete</b>

*Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy
- Pledge
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy
- User
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy

<br>

### **Implement suitable permissions**

*Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Limit who can create
  - [*not required*] Limit who can retrieve
  - [X] Limit who can update
  - [X] Limit who can delete
- Pledge
  - [X] Limit who can create
  - [*not required*] Limit who can retrieve
  - [X] Limit who can update
  - [X] Limit who can delete
- User
  - [*not required*] Limit who can retrieve
  - [X] Limit who can update
  - [X] Limit who can delete

<br>

### **Implement relevant status codes**

- [X] Get returns 200
- [X] Create returns 201
- [X] Not found returns 404

<br>

### **Handle failed requests gracefully** 

- [X] 404 response returns JSON rather than text

<br>

### **Use token authentication**

- [X] implement /api-token-auth/

<br>

---
## Additional features
---
<br>

### **User Interaction:**
* [X] Filter Pledges and Projects
  - Filter pledges by supporter and project. 
  - Filter projects by is_open and owner.
* [X] Fields added to User
  - First Name, Last Name, Bio and Avatar added
* [X] Change Password
  - Change password functionality added

### **System Features:**
* [X] Unique field value restrictions
  - project.title , user.email, user.username restricted; must be unique
  - throws integrity error with re-entry trigger if not unique
* [X] Properties added
  - sum_pledges & goal_vs_pledges added in projects.serializers

### **External libraries used:**

* [X] django-filter

<br>

---
## Part A Submission
---

<br>

### **Links & Screenshots:**

- [X] A link to the deployed project: 
  - https://icy-dew-540.fly.dev/users/
- [ ] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint: 
  - https://tinyurl.com/kg-drf-insomnia-screenshots
- [ ] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
  - https://tinyurl.com/kg-drf-insomnia-screenshots
- [ ] A screenshot of Insomnia, demonstrating a token being returned.
  - https://tinyurl.com/kg-drf-insomnia-screenshots
- [ ] Your refined API specification and Database Schema.

<br>

### **Documentation:**

*Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).*

<br>

#### 1. Create User

```shell
    curl --request POST \
    --url https://icy-dew-540.fly.dev/users/ \
    --header 'Content-Type: application/json' \
    --data '{
        "username": "<insert_unique_username>",
        "email": "<insert_unique_email>",
        "password":"<insert_password>",
        "bio":"<insert_bio>",
        "avatar":"<insert_url_to_image>"
    }'
```

#### 2. Sign in User

```shell
    curl --request POST \
    --url https://icy-dew-540.fly.dev/api-token-auth/ \
    --header 'Content-Type: application/json' \
    --data '{
        "username": "<insert_unique_username>",
        "password": "<insert_password>"
    }'
```

#### 3. Create Project

```shell
    curl --request POST \
    --url https://icy-dew-540.fly.dev/projects/ \
    --header 'Content-Type: application/json' \
    --data '{
        "title": "<unique_title>",
        "description": "<project_description>",
        "goal": <integer>,
        "image": "<image_url>",
        "is_open": <boolean>,
        "date_created": "<auto_filled as today>"
    }'
```
