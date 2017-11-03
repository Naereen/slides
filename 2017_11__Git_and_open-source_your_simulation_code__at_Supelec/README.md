# 2nd 2017/18 GouTP @ SCEE

- *About:*
    + Version control with git
    + Share your simulation code for reproductibility
    + Open-source your code with git

- *Date:* 9th of November 2017

- *Who:* Lilian Besson

---

# What's a *"GouTP"* ?

- **Internal monthly technical training session** :date:
- Usually: *Thursday 3pm :clock3: - 3:30pm* :clock330:
- With :coffee: coffee and :cookie: sweets : we relax while training !

  > Initiative of Quentin and Vincent :clap: in last January...
  > Continued by Rémi, Rami, Muhammad and Lilian :ok_hand: !

## Not only @ SCEE ?
- 2nd and 3rd GouTP will be open to the *FAST team*
  → If success, next ones will be open to other research teams @ Supelec Rennes

---

# Agenda for today [30 min]

1. Concept of version control with `git` (demo) [10 min]

2. Research collaboration on code or articles with `git`
   (examples, good practice) [5 min]

3. Why we should all share our simulation code online, and under an open-source licence (and even the LaTeX code!) [10 min]

4. Example of open-sourcing the MATLAB code and LaTeX code from a recent article [5 min]

---

# Why Git ?

## Version control :wrench: ...
- Veru useful to:
   + Never lose your code :sob:
   + Keep track of progress, revert changes when needed :back:
   + Collaborate easily and asynchronously :muscle:
- Git is used everywhere :earth_africa::earth_americas::earth_asia:, easy to learn and powerful
- :cloud: Free online hosting: Bitbucket, GitHub, GitLab etc...

## Tutorial online :cloud: !
- Try this please → https://Try.GitHub.io

---

## Quick *live demo* of Git

### Meta demo ?
- :angel: I store all my slides on GitHub...
- ... Including the source code for this one :pencil:
- :eyes: Let see together !
  → *live demo* of local use of `git`
   + basic commands for a use in a terminal
   + or in a graphical interface (e.g., inside your IDE)

  → *live demo* of the online repository (on GitHub)

---

# Research collaboration with git :yum:

## Why ?
- Easiest way to collaborate on code :wrench: or article :notebook:
- No email :e-mail:, no painful Dropbox/Drive synchronization :arrows_clockwise: ...
- Full control on your files' history and the synchronization !

## How ?
1. Create a (*private*) repository that your colleagues can access
2. Where? *Example*: Bitbucket, GitHub (with student pack), GForge @ Inria, OverLeaf (for LaTeX)...
3. Start collaborating with no sweat ! :sunglasses:

---

# Share your simulation code online :tada:

## Why ?
- Everyone can (hopefully) reproduce your code and results
- Show to the world that you do *serious reproducible* science !!

## How ?
1. Clean up your source code, and add a few comments
2. Write a small `README.md` file to explain: how to run your code, for which article it was used, conditions of usage etc
3. Maybe add an example, or figures / screenshots
4. Ex: https://Bitbucket.org/SCEE_IETR/Testbed_Monitor for an internal tool, or https://Bitbucket.org/SCEE_IETR/RL_Slotted_IoT_Networks for an article

---

# Join the open-source community !

- :hammer: https://ChooseALicense.com to pick a license suiting your needs
- :ok_hand: By default HAL uses a **Creative Commons** license (with various flavors). Example : HAL.Inria.fr/HAL-01575419
- :warning: But arXiv does not specify the license (on document and source) : that's bad ! No one can use your code if you do not specify any copyright or usage conditions...

### My advice :smiley: ?
- I suggest the **MIT License** for simulation code (short & well-known) and **Creative Commons** for documents and LaTeX

---

## Example of sharing on Bitbucket the simulation code from an article

It takes 10 minutes:

1. Clean up the MATLAB files :art:
2. Add a few comments in the tricky parts :see_no_evil:
3. Add a header to the files stating the copyright :pencil:
4. Choose a license and add a `LICENSE` file :hammer:
5. Write a `README.md` file in the folder :file_folder:
6. Create the repository :wrench:, `git add` all the files
7. :airplane: `git push`, check the result, and relax :sunglasses: !

→ https://Bitbucket.org/SCEE_IETR/RL_Slotted_IoT_Networks

---

## And open-sourcing the LaTeX code?

> Note: this is *not* against the copyright policies of conferences/journals if you do not share the PDF... :wink:

- :v: Not so useful for articles with basic templates, but why not?
- :gift: Can help your colleagues if you use a nice template for posters or slides
- :gift: Can also help when writing your thesis, you can copy-paste equations from your colleagues' articles instead of re-writing...
- Example: https://Bitbucket.org/LBesson/Multi-Armed-Bandit-Learning-in-IoT-Networks-Learning-Helps

---

# Conclusion
- I hope you got an overview of how to use `git`
- Why it can be a good idea to share your simulation code
- And why choosing an open-source license is smart !

### Your mission, if you accept it... :boom:
- *Padawan level:* Train yourself on git → https://Try.GitHub.io
- *Jedi level:* Release some simulation code online !
- *Master level:* Release *all* your code (and LaTeX) online !!

> *Thanks for joining :clap: !* *Contact us if you want to do a GouTP!*