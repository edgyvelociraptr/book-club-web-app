# Little Book App

**Roles**
- **Member:** a regular book club participant with an associated acount. 
- **Club Admin:** a member who manges the book club application for the group. 

## User Stories

### Log in
As a **user**, I want to **be able to login to my own profile** so that **my votes and reading progress are tied to me**.

**Acceptance Criteria**
- A registered user is able to login using their username and password.

### Propose the next book
As a **user**, I want to **search for a book and be able to propose it** so that **the group can consider it**.

**Acceptance Criteria**
- A logged-in user can propose a potential book pick by submitting the title, author, and page count. 
- The new proposal is shown in a list with other proposals as well as who submitted each one. 
- The form will not accept empty titles/author names and non-positive/numeric page counts. 

### Vote on the proposed books
As a **user**, I want to **see the current book and upcoming meeting details** so I can **know what to read and when/where I need to show up**.

**Acceptance Criteria**
- A member is able to vote on any book from the proposed list while voting is open
- Each member is only able to vote once

### RSVP for upcoming meetings
As a **user**, I want to **be able to RSVP to meetings** so that **the host will be asble to see how many people to expect**.

**Acceptance Criteria**
- The user can select a yes, no, or maybe option if they are able to attend the next meeting. They are also able to change their RSVP.
- Each member has one RSVP per each meeting
- The meeting page shows a current count of those who can, cannot, and might be able to attend.

### Spoiler-Safe Comments (potential feature)
As a **user**, I want to **record how much of the book I have read** so I can **only see discussion posts/conversations that won't spoil the book**.

**Acceptance Criteria**
- Each user will be able to save/enter their current page location for the active book
- Any comments are saved with a page number
- They can only see comments whose page number is less than or equal to their current page location, plus their own comments
- Any user without any saved progress would be unable to see any comments other than their own

## Admin Stories

### Close Voting
As a **admin**, I want to **close voting and declare a winning pick** so that **the club can get started on/pickup the next read**.

**Acceptance Criteria**
- The admin is able to close the voting on open proposals
- The proposed books with the highest number of votes becomes the new current read.
- Once the voting has ended no additional votes can be made on the proposed books.

### Schedule Meeting
As a **admin**, I want to **be able to create the nexct meeting with date/time/host information** so that **everyone has that information avaliable**.

**Acceptance Criteria**
- The admin is able to create a meeting with the date, location, host, and the selected book.
- The new meeting will be visible from the home page
- If the dates selected are in the past then the meeting date will be rejected

### Invite and Remove Members
As a **admin**, I want to **invite and remove members** so that **only active members will be able to access the app**.

**Acceptance Criteria**
- The admin will be able to create/invite new users to have access to the application.
- Any users who are no longer active can also be removed so they will be unable to access the application.

## Mis-User Stories

### Account Take Over / Brute-Force
As an **attacker** I want to **guess/brute-force user passwords** so that I can **take over their account and access the application as a member**

**Mitigation Criteria**
- Passwords should meet (or exceed) the password criteria (ex. minimum length, not common, contains a mix of alphanumeric characters)

### Voter Fraud
As a **dishonest member** I want to **be able to vote multiple times** so I can **force the book I want to win**

**Mitigation Criteria**
- The application will enforce only a single vote per member per voting period

### Account Escalation
As a **user** I want to **access the admin actions that pertain to voting & proposals** so I can **control, change, or disrupt the club's choices**

**Mitigation Criteria**
- Admin-only operations and buttons are hidden from non-admins.
- Non-admin accounts will receieve an error when trying to access admin controls

## Architecture Models

### System Context Diagram
<img width="715" height="413" alt="systemcontext drawio (2)" src="https://github.com/user-attachments/assets/59713368-c68b-4245-98dc-3dfe6ef5f2a8" />

### Containers
<img width="812" height="564" alt="container drawio" src="https://github.com/user-attachments/assets/58fec2cf-5947-4158-bd3f-16a497e0194b" />

### Components
<img width="1179" height="904" alt="componentdiagram drawio" src="https://github.com/user-attachments/assets/9af9eaec-1069-4a37-9a80-4cae5260aa3f" />


