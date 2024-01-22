# MTANK
> *Group 5 get to grips with Git* 💪 <br>
Please note this README covers points in both Q1 and Q2, so do read to end! 😊

Group members 
----------------------------------------

- Anu Panday 
  - Fun fact: I'm a huge fan of Harry Potter and love watching K-Dramas
- Maya Welford
   - Fun fact: I recently got two kittens and a puppy!
- Narmeen Mohammed
  - Fun fact: I have a pet snake called Mitsuki!
- Tang Ng
   - Fun fact: I learnt some Irish dancing as a child!
- Nakita Hancock
  - Fun fact: I have 3 Ladybirds as pets.

<br> 

### Our favourite foods/cuisines are:

- **Maya:** *Japanese food!*
- **Tang:** *Noodles!*
- **Anu:** *Dumplings!*
- **Narmeen:** *Korean BBQ!*
- **Nakita:** *Stir fry!*
<br>

### Would you rather have the ability to fly or the ability to teleport?
| Fly                                                 | Teleport | 
|-----------------------------------------------------|:--------:| 
| Tang `(but teleporting would also be super handy!)` |  Maya    |
| Anu                                                 |  Narmeen |
|                                                     |  Nakita  |

 
<br>

### Favourite song lyric/quote/line from a movie/poem?
1. From The Help, 2011 (Tang)
   > “You is kind. You is smart. You is important.”
2. From Finding Nemo, 2003 (Anu)
   > "Just keep swimming" 🐠
3. From Chernobyl(the series) (Narmeen)
   >"“The real danger is that if we hear enough lies, then we no longer recognise the truth at all.”
4. Groundhog Day, 1993 (Nakita)
   >"Watch out for that first step. It's a doozy!"
5. Toy Story (Maya)
   > “You got a friend in me.”
<br>

Question 1 - further points
----------------------------------------

#### Demonstrating how to work as a team on GitHub

<img width="1238" alt="Screenshot 2023-10-21 at 17 01 12" src="https://github.com/anupanday/group-5/assets/75754430/249554ea-ab4b-4f50-a88a-77aab8c260be"> <br>

#### Git Workflow
Below images show: git checkout -b, git add, git commit -m, git push, opening a pull request, Anu reviews, close pull request
![image (2)](https://github.com/anupanday/group-5/assets/75754430/fa3ab9b9-da0e-443e-a466-fcb5302263f2)
![image (3)](https://github.com/anupanday/group-5/assets/75754430/6090a143-b71e-4855-b0db-3738861d8822)
![image (4)](https://github.com/anupanday/group-5/assets/75754430/3c16f9bf-afc1-44ac-9764-a18b77d48329)
![image (5)](https://github.com/anupanday/group-5/assets/75754430/17db60dd-3795-4cbb-b357-ebf326cb6350)
<img width="1419" alt="Screenshot 2023-10-23 at 21 43 21" src="https://github.com/anupanday/group-5/assets/75754430/4b60c0b6-7fa2-4ae9-9e48-a655b3c0ade7">
<img width="1420" alt="Screenshot 2023-10-24 at 00 00 40" src="https://github.com/anupanday/group-5/assets/75754430/c3b97eee-a5d0-4ca4-a4fe-9cf1db7250d5">
![image (7)](https://github.com/anupanday/group-5/assets/75754430/af3044c2-cd1c-43bd-8e05-301c41f88810)
![image (8)](https://github.com/anupanday/group-5/assets/75754430/bc7d6ea2-ac8c-4f17-9fa5-832b378b3caf)

#### Create branches for each member or feature and using meaningful naming

<img width="1266" alt="Screenshot 2023-10-24 at 08 23 23" src="https://github.com/anupanday/group-5/assets/75754430/393bd385-3cf9-4a34-ac60-d205da805977">

#### Create .gitignore and requirements.txt and briefly explain what they are for
 - .gitignore is used to tell Git which files it should ignore. The purpose is to ensure that certain files not tracked 
by Git continue to be untracked. An example of when we would use is this would be for our config file as it has our MySQL password.
 - The requirements.txt file includes a list of all of a project's dependencies. 
It specifies which libraries are required and any version requirements for them.
.gitignore and requirements.txt files included in this project.

Question 2 
----------------------------------------
Finally here is a link back to the project:
[Group-5 Project :)](https://github.com/anupanday/group-5 "Group-5 Project!")

How to Use Our API 
----------------------------------------
1. Please make sure to import the following packages before running our API or read the requirements.txt file:
   - flask
   - requests
   - mysql.connector
  These might be standard:
   - json
   - random
   - datetime
2. Please make sure to include your MySQL password in the config file.
3. Click the run() in the main.py file to interact with the API.
  Things to bear in mind:
+ Staff password: Staff123#
+ Valid dates are between 2023-10-23 and 2023-10-27 inclusive.
+ The database starts out with no appointments booked, so all slots are available.

What Should Happen
----------------------------------------
1. Select whether you a staff or patient.
2. If you are a staff member e.g. receptionist, this allows you to see which appointments are still available (e.g. for phone bookings)
   1. The staff password is : Staff123#
4. If you are a patient, you will have the option of:
   1. Adding your details if you are a new patient
   2. Either cancelling or adding an appointment using the patient DOB and surname.

Hope you enjoy!
