NOTE: 
* this repo was deployed to Fly. However:
  * to continue working on this project, it was forked to: https://github.com/Ms-KL/she-codes-crowdfunding-api-project-Ms-KL
  * improvements have since been made to this project using the above new [fork](https://github.com/Ms-KL/she-codes-crowdfunding-api-project-Ms-KL)
  * the new [fork](https://github.com/Ms-KL/she-codes-crowdfunding-api-project-Ms-KL) has since been redeployed to fly with the changes
* as a result, this repo will not match the final deployed project in fly. Please see [fork](https://github.com/Ms-KL/she-codes-crowdfunding-api-project-Ms-KL) for up-to-date repo that matches the deployed version.


# {{ Communitree: DRF Crowdfunding Project }}

Welcome to Communitree, where tree-huggers gather to make a real impact on the urban forest of their community. Local Governments, schools and environmental organisations can create projects to raise funds for community busy bees and planting days/events. Supporters can pledge resources to help these projects. 

<br>

---
## **TL:DR Links**
---

### **MVP Submission:**
  - [Submission Document (Canva)](https://www.canva.com/design/DAFXgSq-5YI/VoGjxBH0387phr6s29IV1A/view?utm_content=DAFXgSq-5YI&utm_campaign=designshare&utm_medium=link&utm_source=publishshare)
  - [User Flow-Chart (Figma)](https://www.figma.com/file/TTOAG3ee2VSnR9JWF2aG6l/Crowdfunding-Project?node-id=0%3A1&t=wOw8Y89TyRAGQ2p3-0)
  - [GitHub MVP Submission Folder](https://github.com/SheCodesAus/she-codes-crowdfunding-api-project-Ms-KL/tree/main/project_submission/MVP%20Submission)
  
### **Part A Submission:** 
  - [Deployed Project (Fly)](https://icy-dew-540.fly.dev/)
  - [Submission Document (Canva)](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)
  - [Insomnia Screenshots (Canva)](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#5)
  - [GitHub Part A Submission Folder](https://github.com/SheCodesAus/she-codes-crowdfunding-api-project-Ms-KL/tree/readme/project_submission/Part%20A%20Submission)

---
## **Features**
---
See Also: [Project Requirements Checklist](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#2)
### **User Accounts**

- [X] Username
- [X] Email Address
- [X] Password

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
  - [ ] Destroy -> *not required*
    - user can make themselves inactive. delete not activated to keep db integrity. Admin can still delete through admin portal.

### **Implement suitable permissions**

*Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Limit who can create
  - [ ] Limit who can retrieve -> *not required*
  - [X] Limit who can update
  - [X] Limit who can delete
- Pledge
  - [X] Limit who can create
  - [ ] Limit who can retrieve -> *not required*
  - [X] Limit who can update -> *can only edit non-amount fields*
  - [X] Limit who can delete
- User
  - [ ] Limit who can retrieve -> *not required*
  - [X] Limit who can update
  - [X] Limit who can delete

### **Implement relevant status codes**

- [X] Get returns 200
- [X] Create returns 201
- [X] Not found returns 404

### **Handle failed requests gracefully** 

- [X] 404 response returns JSON rather than text
  - Note: navigation to an unexpected page (eg: pledges/abc/) will return a custom text error message. However expected pages with no data to return yet (eg: pledges/100/) will return JSON

### **Use token authentication**

- [X] implement /api-token-auth/

---
## Additional features
---
See Also [MVP Submission - Features Page](https://www.canva.com/design/DAFXgSq-5YI/VoGjxBH0387phr6s29IV1A/view?utm_content=DAFXgSq-5YI&utm_campaign=designshare&utm_medium=link&utm_source=publishshare#11) | [Part A Submission - Features Page](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#10)
### **User Experience:**

- [X] { Filter Pledges and Projects }

{{ Filter pledges by supporter and project. Filter projects by is_open and owner. }}

- [X] { User Fields and History }

{{ First Name, Last Name, Bio and Avatar added. User Comments, Pledges and Projects history listed in Custom User Detail }}

- [X] { Change Password }

{{ Change password functionality added }}

- [X] { Comments }

{{ Comments feature added for users to interact with project }}

- [X] { Pledge and Comment History }

{{ Pledge and Comment List displayed in Project Detail }}

- [X] { Custom API Root }

{{ As per Ben's suggestion 02/02/23 }}

### **System Features:**

- [X] { Unique field value restrictions }

{{ project.title , user.email, user.username restricted; must be unique: throws integrity error with re-entry trigger if not unique }}

- [X] { Properties added }

{{ sum_pledge, goal_balance & funding_status added in Project Detail }}

### **External libraries used:**

* [X] django-filter

---
## Part A Submission
---


### **Links & Screenshots:**

- [X] A [link](https://icy-dew-540.fly.dev/) to the deployed project
- [X] A [screenshot](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#5) of Insomnia, demonstrating a successful GET method for any endpoint
- [X] A [screenshot](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#5) of Insomnia, demonstrating a successful POST method for any endpoint
- [X] A [screenshot](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#5) of Insomnia, demonstrating a token being returned 
- [X] Your refined [API Specification (2 pages)](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#8) and [Database Schema](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#7).

### **Documentation:**

*Step by step [instructions](https://www.canva.com/design/DAFYscsU8w8/eiO7sj6_0qJGhFXIMqWkKQ/view?utm_content=DAFYscsU8w8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#6) for how to register a new user and create a new project (i.e. endpoints and body data).*

1. Create User

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

2. Sign in User

```shell
    curl --request POST \
    --url https://icy-dew-540.fly.dev/api-token-auth/ \
    --header 'Content-Type: application/json' \
    --data '{
        "username": "<insert_unique_username>",
        "password": "<insert_password>"
    }'
```

3. Create Project

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
