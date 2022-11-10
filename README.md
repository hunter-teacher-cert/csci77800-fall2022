# csci77800-fall2022
Main working repo for Ethics and CS -- Fall 2022

# CSCI 77800 - Ethics and Computer Science

## Discussion
- standing zoom session: <https://us02web.zoom.us/j/82948211667?pwd=YXVlL09tb3pXcFFnWktsNHFGSkdOZz09> 
- slack: <https://hunterteacher-vyz6159.slack.com/>
  - real-time chat during live sessions (__Use instead of zoomchat!__)
  - asynchronous communication between sessions
  - prior cohort members may contribute to discussion.
  - `#ethics` - real-time chat during live sessions and between sessions
  - `#ethics-async` - general async discussion area
  - `#ethics-we` - dedicated space for Weekly Ethicacy discussion (including its async component)
  - `#ethics-Q-queue` - for lining up questions to be addressed during in-class time (instead of zoom-hand raising)
  - `#python-fu` - for troubleshooting, pro-tip sharing, shop-talking, resource sharing
  - `#general` - everybody, including prior cohorts
- syllabus: <https://github.com/hunter-teacher-cert/csci77800-fall2022/blob/main/syllabus.md>

## Ethi:CS -- The Weekly Ethicacy
At the beginning of each session, a designated duo will present on a topic of interest to them (and hopefully all of us!).

### Deliverables:
- PDF in each partner's **ethicacy** folder in your work repo, subject to these guidelines:
  - hyperlink(s) to primary source(s) included
  - summary of issue or newsworthy development
  - single page
- Other supporting files may be added to ethicacy folder. Each partners' folder must contain all files.

### Presentation
* _GOAL: Each partner takes a side (of an at-least-2-sided issue), and audience gets to hear each argument._
  - ~3-5min per side.
    - (shorter: topic not rich enough)
    - (longer: topic not distilled enough)
  - solicit questions/comments/concerns
* Weekly Ethicacy will take place in two breakout rooms, at the beginning of each week's live session.

### Asynchronous Component
* Within a week of the live session during which a Weekly Ethicacy is delivered, each participant will post to the corresponding thread in the `ethics-we` channel a response:
  - clearly indicating chosen side
  - supporting their choice with supporting documentation, by referencing personal experience, and/or by expanding upon comments from live presentation or preceding channel discussion.

### Presentation Order / Teams
* Duo 1 will present to room 1, Duo 2 will present to room2.
* CSV of randomized pairings: https://github.com/hunter-teacher-cert/csci77800-fall2022/blob/main/ethicacy_duos.csv
* _Participants are expected to establish communications with their partner as soon as possible, and collaborate to maximize presentation quality._


* * * 

## Weekly Progression

### Week 1
#### Sync
* What comprises Ethical CS?
* Course overview
  - syllabus
  - grading
  - Github Assignment Repo setup
  - Weekly Ethicacy
  - How async will work (vs assignments and homework)
* **Ground rules for discussions:** _We will grow/learn the most if we..._
  - respect one another's positions.
  - separate person (and their worth) from their opinions/stance.
  - listen for understanding.
  - step into others' shoes.
  - sometimes play "Devil's advocate" to suss out unfamilar/distasteful/problematic positions.

#### Async
* Due 9/14 9:00pm 
* Review pre-reading (ThinkPython Ch.1-4) and additional chapters as necessary, utilize `#python-fu` channel as necessary to discuss.
* Bookmark Ch.9-10 for reference now and later in the term.
* Consult your summer java codebase as necessary, and re-write in python 
  - Game of Nim
  - Game of Life
  - Binary Search : iterative or recursive version
* DELIVERABLE:
```
your-ethics-work-repo/py/nim.py
your-ethics-work-repo/py/gol.py
your-ethics-work-repo/py/binsearch.py
```
  - for each sourcecode file you submit, include a heading comment block in this format:
  ```python
  # FILENAME
  # First Last
  # CSCI 77800 Fall 2022
  # collaborators: 
  # consulted: 
  ```

- - -

### Week 2 - 9/8
#### Sync
* No Sync Class
#### Async
- set up work repos
- Python assignment


---

### Week 3 - 9/15
##### Topic: Data Privacy
#### Sync
* Ethicacy
* Breakouts : admin policy / tooling choice
* Breakouts : data privacy


#### Async
* Due 9/21 9:00pm
* First look over the references on this page:
   - https://aboutmyinfo.org/identity/about
* Next, select two services: They could be domain-specific (like an education platform); generic (say, Gmail); or could even be two competitors (like two email providers).
* Read their privacy policies.
* Post the products you are reviewing and comment on one thing for each policy (what it is, why it's good or bad or what raises flags, in your opinion).
* If someone posts re: your chosen product before you do, comment on their thread rather than creating a new one.
* TASK: Write up a short summary comparing and contrasting. Include an overview of what data is collected and maintained and how they may or may not use it.
* If another class member is working on the same two products you can work with them on the writeup. Make sure to include both names and make sure the file is uploaded to both of your repos.
* Save write-up in: `week03/privacy_terms.pdf`

---

### Week 4 and 5 (9/22 or 9/29)
##### Topic: REGEX
#### Sync
* Ethicacy Breakouts


Room 1 presenters (9/22)
-----------------
- Ethicacy Breakout 1 - Grant-Knight	Taylor
- Ethicacy Breakout 1 - Prado	Ada


Room 2 presenters (9/22)
-----------------
- Ethicacy Breakout 2 - Marra	Christine
- Ethicacy Breakout 2 - Yearwood	Maxwell

Room 1 presenters (9/29)
-----------------
- Ethicacy Breakout 1 - Park Jihae
- Ethicacy Breakout 1 - Tobias Wayne

Room 2 presenters (9/29)
-----------------
- Ethicacy Breakout 2 - Fung Harrison
- Ethicacy Breakout 2 - Wardally Tanya


* REGEX
  - What are regular expressions and how can we use them in Python


#### Async
##### Folder: week04
##### Due: Wed 9/28 at 9:00pm for 9/22 students
##### Due: Wed 10/5 at 9:00pm for 9/29 students

##### Instructions

1. Create a plaintext file in your week04 folder named names.txt. This file should contain lines of text where some of the lines have one or more names. Names can be formatted in different ways. For example "John Smith" would be a name, as would "Mrs. Chen" and "Dr. S. Howard." Names can be formatted in many more ways as well. Try to include as many different ways of representing names as you can.
1. Download the regex.py program from the code section of the main web site. Modify the program so that it will read names.txt. Your program should print out all the names it can identify in names.txt.

##### Goal: 
When the program is run, it should just run, read names.txt and print out the names it finds. You do not have to format the output in any special way; you can just print out the results of your calls to re.find() and/or any other functions you use to identify the names.

Useful reference material:
- online regex builder / tester site: https://regexr.com/
- Python regex reference:
  - https://www.w3schools.com/python/python_regex.asp
  - https://www.tutorialspoint.com/python/python_reg_expressions.htm
  - https://www.geeksforgeeks.org/python-regex-cheat-sheet/
- General Regex tutorial:
  - https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285
- Python regex video
  -https://www.youtube.com/watch?v=K8L6KVGG-7o&list=WL&index=107&t=322s

##### Ethicacy Reminder
Ethicacy presenters are expected to post their one-pager in #ethics-we early in the week and upload it to your repo.

Everyone else is required to comment on one of the weekly ethicacy posts or previous comments.


---

### Week 6

Room 1 presenters (10/5)
-----------------
- Ethicacy Breakout 1 - Rachel
- Ethicacy Breakout 1 - Vanessa

Room 2 presenters (10/5)
-----------------
- Ethicacy Breakout 2 - Marieka
- Ethicacy Breakout 2 - Jessica


#### Async
##### Folder: n/a since responses on Slack
##### Due: Wed 10/12 9:00pm

##### Instructions

###### Part 1
Read these pieces:

- https://www.theverge.com/2021/9/6/22659225/automated-hiring-software-rejecting-viable-candidates-harvard-business-school
- https://www.reuters.com/article/us-amazon-com-jobs-automation-insight-idUSKCN1MK08G
- https://montrealethics.ai/why-was-your-job-application-rejected-bias-in-recruitment-algorithms-part-1/
- https://montrealethics.ai/why-was-your-job-application-rejected-bias-in-recruitment-algorithms-part-2/

In the week06 async thread comment on at least one of the following questions and respond to at least classmates comment. Some of these questions are only tangentially related to the automated scanning issues.

Should companies scan social media accounts of either potential employees or current employees or should they be sacrosanct? Should it be different for potential vs current employees?

Do you find a professional benefit to using social media and what and if so what are they? On the flip side, what might be the professional dangers?

What are your thoughts on connecting with students on social media?

If you were to design an automated job portal, how would you structure it so that employers could optimally use it while also protecting applicants in terms of both privacy as well as from any biases employers may have?

###### Part 2
Set up a repo in preparation for creating a web page.

Go to GitHub
- Click on “new” to create a new repo (button on the upper left usually)
- type in a name for the repo
- Make sure you select public for access (not private)
- Make sure you select “create a readme file”
- Once the repo is created go to settings
- Select the “pages” tab from left side tab list
- Select “main” as the branch and save (leave the / (root) thing alone)

### Week 7
##### Topic: Build a web page

Folder: week07

Due: 10/19 9:00pm

Filename: `websites.md`

For this site you will make a web site and host it on GitHub. The site could be for class page, a personal site, or anything else. The site must include a form (although the form won’t actually do anything) and at least one image but can include anything and everything else.

You can and are encouraged to work with a partner - if so, both repos should contain the same information and it should be clear on the site who worked on it.

Not all of you are at the same level of experience with HTML and/or so we expect something comensurate with your knowledge. Not in terms of size but in terms of what you use. That is, brand new people will have much more bare bones sites and that’s fine. I would love for you to take the week to stretch yourself a bit - try something new.

We do not expect any javascript for this assignment, just HTML and CSS.

You are to make the web site in a GitHub repository. In the file websites.md put links to:

The repo that’s holding the web site code (and location if it’s not the only thing there).
A link to the live website.
The name of your partner if you’re working with one.
Here are four videos to get you started. The first covers setting up the GitHub repo, the second basic HTML, then CSS, then more advanced CSS.

- setup: https://www.youtube.com/watch?v=4Do0NXfiaX4&list=PL9KxKa8NpFxL2CpZG0Q6YpOJya8v788wx&index=10
- basic html: https://www.youtube.com/watch?v=PackQ6dgUIY&list=PL9KxKa8NpFxL2CpZG0Q6YpOJya8v788wx&index=9
- basic css: https://www.youtube.com/watch?v=48UJRMk15i8&list=PL9KxKa8NpFxL2CpZG0Q6YpOJya8v788wx&index=8
- more css (grid): https://www.youtube.com/watch?v=Hh0ac_djkWM&list=PL9KxKa8NpFxL2CpZG0Q6YpOJya8v788wx&index=7
- Here are some tutorial sites:

HTML tutorials
- https://www.w3schools.com/html/
- https://www.tutorialspoint.com/html/index.htm

CSS Tutorials
- https://www.w3schools.com/Css/
- https://www.tutorialspoint.com/css/index.htm
- https://developer.mozilla.org/en-US/docs/Web/CSS/Tutorials

Grid and Flexbox tutorials
- https://www.quackit.com/css/flexbox/examples/

And some reference sites:

HTML references
* https://www.w3schools.com/tags/default.asp
* https://developer.mozilla.org/en-US/docs/Web/HTML/Reference
* https://htmlreference.io/

CSS references
* https://developer.mozilla.org/en-US/docs/Web/CSS/Reference
* https://cssreference.io/
* https://www.w3schools.com/cssref/

Grid examples
* https://gridbyexample.com/examples/
* https://webkit.org/demos/css-grid/



### Week 8
##### Topic: web and accessibility
#### Sync
  - Ethicacy
  - Overview: https://www.w3.org/WAI/fundamentals/accessibility-intro/
  - Guidelines: https://www.w3.org/TR/WCAG/
  - Automated accessibility checkers:
    - https://accessibilitytest.org/
    - https://www.webaccessibility.com/
  - article with link to tools: https://accessibility.blog.gov.uk/2017/02/24/what-we-found-when-we-tested-tools-on-the-worlds-least-accessible-webpage/
  - Editor themes:
    - emacs: https://protesilaos.com/emacs/modus-themes
    - emacs: https://github.com/protesilaos/modus-themes
  - Screen readers
    - linux:
      - https://wiki.gnome.org/Projects/Orca
      - https://help.gnome.org/users/orca/stable/
    - MS:
      - https://www.microsoft.com/en-us/accessibility/microsoft-365?activetab=pivot_1%3aprimaryr2
      - https://support.microsoft.com/en-us/windows/use-a-screen-reader-to-explore-and-navigate-settings-in-windows-114e0fa0-42d6-4dba-8afe-374b70e2a5c8
    - Apple:
      - https://www.apple.com/accessibility/vision/
    - google:
      - https://support.google.com/docs/answer/6282736?hl=en&co=GENIE.Platform%3DDesktop
      - https://support.google.com/docs/answer/6282736?hl=en&co=GENIE.Platform%3DDesktop
  - Magnifiers


#### Async
Folder: No folder for this week. Submissions on Slack and final form

- Download the program `plane_seating.py` from the code folder on our 
  web site. Run and read through the program and work to understand
  specifically how it works. The program overall simulates the
  purchase of seats for a plane but look at the file for comments and
  then study the code.
- Read:
  - https://medium.com/salesforce-ux/7-things-every-designer-needs-to-know-about-accessibility-64f105f0881b
  - https://www.bootstrapworld.org/blog/accessibility/User-Interface-REPL.shtml
  - https://www.bootstrapworld.org/blog/accessibility/Describing-Images-Screenreaders.shtml
  - https://www.bootstrapworld.org/blog/accessibility/Text-Navigation.shtml
  - https://www.bootstrapworld.org/blog/accessibility/User-Testing.shtml
  - https://accessibility.blog.gov.uk/2017/02/24/what-we-found-when-we-tested-tools-on-the-worlds-least-accessible-webpage/
- Here are some more references to look over on accessibility 
  - Overview: https://www.w3.org/WAI/fundamentals/accessibility-intro/
   - Guidelines here:https://www.w3.org/TR/WCAG/
- Fill out final proposal (see finals.org on main page)
- Post to async channel which HTML accessibility features you could most easily incorporate into student assigments.


---

### Week 9
##### Topic: Start airplane seating assignment
#### Sync
* Ethicacy
* Review the `plane_seating` code
* Breakouts - add the `seat_economy` parts
* Groups
  -tk
* Analysis
 - look at code
 - ethical issues
* Articles
  -tk

#### Async
Folder: week09_seating

Here are some articles on the airplane issue. Look over them:

- https://www.independent.co.uk/travel/news-and-advice/airline-flights-pay-extra-sit-together-split-family-algorithm-minister-a8640771.html
 - https://thepointsguy.com/news/airlines-purposely-splitting-up-families-make-more-money/
 - https://www.marketwatch.com/story/do-airlines-split-up-families-so-they-pay-extra-for-seat-allocation-2018-02-05

Assignment: 
Folder: week09_seating
- Design an algorithm that would seat people more equitably. 
- Write up a description of your algorithm and save it as
  `week09_seating/seating.pdf` (or week09_seating/seating.md). Make
  sure this description states how it should improve equity and also
  how it might affect other concerns.
- NO CODE IS NEEDED OR EXPECTED HERE -- just a description -- but make a note of
  implementation issues that might make your algorithm more practical
  or more difficult to implement
- In class next week you will share your ideas and algorithms and ultimately decide on what to
  recommend to the airlines.
- find another example where optimization of one thing has ethical
  ramifications and unintended consequences. bonus points if it's an
  ethical optimization (that is, they optimize for a good ethical
  reason but it has a negative unintended consequence). Post article
  link or reference to this to #ethics-async
- make a file `week09_seating/consequences.md` with link to article 


### Week 10
##### Topic: Continue airplane seating
#### Sync
* Ethicacy
* discussion of better algorithms - together
* lab (sync and async): implement new algorithm

#### Async Week 10 - DUE 11/16 (2 weeks) 9:00pm
* Repo directory: week09_seating (yes, the same directory as last week)
* Note: This assignment should be done in teams of 2 or 3.
* Write up a description of the algorithm you will implement as a text, pdf or md file and store it
  in the folder under the name algorithm.txt, algorithm.pdf or algorithm.md
* Make a copy of the provided plane_seating.py in the folder
  and implement as much of your algorithm as you can.
  If you can't implement it fully, describe in the comments what
  you couldn't do due to either time or complexity.
* If you want to start with a new plane base rather than work from the
  provided code (even in another language), that's fine but make sure the filename for your
  implementation is still plane_seating.py or plane_seathing.whatever where whatever is the appropriate language extension 

---

### Week 11
##### Ethicacy catchup
#### Sync
* Ethicacy
* Ethicacy Presenters:
* Session 1:
 - Room 1: awade, jhiggens  
 - Room 2: slojacono, kherr

* Session 2:
 - Room 1: arobinson, ssabaugh
 - Room 2: lboland, dciolino-volano

* Session 3:
 - Room 1: sadams, ssecccafico 
 - Room 2: dmoste, alee

* Session 4:
 - Room 1: jxue, twilliams
 - Room 2: ylevels, ysears


#### Async
 - Fill out this form with your movie preferences: https://forms.gle/hv8W5cRvBqwwGoNi6
 - Fill out this form at least 3 times to recommend at least 3 movies: https://forms.gle/TdzfHLqeow411Qhg6
 - Finish previous week’s assignment (plane seating implementation)

---

### Week 12 - 11/17
##### Topic: 

#### Async
* -tk

---

### Week 13 - 12/1
##### Topic: 
#### Sync
* Ethicacy
* -tk

#### Async
* -tk

---

### Week 14 12/8
##### Topic: Ethicacy and final presentations
#### Sync
* Ethicacy
* -tk

#### Async
* -tk

---

### Week 15
##### Topic: Ethicacy and final presentations
#### Sync
* Ethicacy
* -tk

#### Async
* -tk

---



* * *

## Our work repos
(Dont' have one yet? Follow this link to initialize yours:  <https://classroom.github.com/a/-iW8TBoR>)

- [Seth](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-Mr-Adams)
- [usman](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-usman0527)
- [Joel](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-JABianchi)
- [Latoya](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-BolandTech)
- [Alise](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-AliseBraick)
- [Aasine](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-acassara13)
- [Dave](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-dcv86)
- [Nicole](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-msCOJUANGCO)
- [Christopher](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-cdesilva2)
- [adam](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-awdriggs)
- [Benjamin](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-beckley1)
- [Patricia "Patti"](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-pelfers21)
- [Harrison](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-hfung8)
- [stacy](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-sgoldstein11)
- [Taylor](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-tgrantknight)
- [Ed](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-ehawkins18)
- [Shana Elizabeth](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-mathiskey)
- [Kiana](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-herrkm)
- [Joshua](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-Mr-Higgins)
- [Rachel](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-rkaufman8)
- [William](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-mrlamorie)
- [Erwin](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-elara711)
- [Amanda](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-AmaneWei)
- [Yeidy](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-YLevels)
- [Jiamin "Jenna"](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-jenna0704)
- [Samuel David "Sam"](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-sdl5384)
- [Christine](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-chrismarra21)
- [Kirk](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-Kirk-Martin)
- [Katherine "Kate"](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-Kmaschm)
- [Sarah](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-sarahkmccoy)
- [Parmanand](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-ParmanandM1)
- [David](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-dmoste)
- [Saranii](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-saraniim)
- [Jessica](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-jnovillo)
- [Jihae](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-jpark-29)
- [Moo Joon "Mike"](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-michaelpark677)
- [Richard](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-richparker718)
- [Adam](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-AJP713)
- [Michael](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-mikeinawall)
- [Elizabeth](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-DrydenArt)
- [Alana](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-AlanaY11)
- [Stephen "Steve"](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-SAYbaw)
- [Yanique](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-ysears)
- [SueAnn "Suzie"](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-ssecc001)
- [Marisa](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-Mshuman8)
- [Jerusha](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-jmtheo8)
- [Marieke](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-marieke-thomas)
- [Wayne](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-WayneTobias)
- [Ashley](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-A-Ufret)
- [Alicia](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-awade05)
- [Tanya](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-twardally)
- [Théa](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-theawilliams19)
- [Jing](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-jingxue8303)
- [Maxwell](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-Maxwoodi)
- [Yenmin](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-yenminyoung)
- [Qianhui Vanessa](https://github.com/hunter-teacher-cert/fall-2022-ethics-work-qvzou)
