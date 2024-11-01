# Project Evaluation

|Notes|Score (262)|Evidence|
|-----|------|---------|
|Video1|3|[Link](https://drive.google.com/file/d/1lpd1DkfZUA-zm9XgBw17NZk618qh3YuW/view?usp=share_link), New features: Decoupled routes and rides in the old application for better UX; Cab price prediction using a machine learning model in "View Ride" page; Added a forum for every ride where users can discuss logistics; Two-way ride request/confirmation feature between riders and owners; Rides have dynamic availability based on riders who have been accepted to travel; Owners can delete rides and users can cancel ride requests; Auto-complete feature for location (soure and destination) while creating a new ride; Ride route, distance and ETA is shown in the "View Ride" page; Emails are sent to ride owners when a ride capacity is reached; Fixed existing bugs in authentication - password is now hashed and stored instead of plaintext, multiple user accounts could have same usernames, password was visible while being typed, incorrect username/password prompts an error; Improved code quality by removing stale code and setting up a comprehensive CI/CD pipeline.|
|Bonus: Xfold improvement|3|1. Performance: Shifted to use Google APIs in Search Ride -> View Ride page. We removed the existing use of Selenium on client-side to render routes between a source and a destination. This improves client performance because no memory overheads are there to render a new browser tab. 2. Lessen developer time: We cleaned code for better maintenance and improved readability for new developers - removed stale methods, unused imports etc. We fixed nearly 300 issues identified by pylint and codacy static analysis reports; Added plenty testcases to cover code coverage for existing functionality. 3. Scalability: We identified an [architecture](https://github.com/VSangarya/PackTravel#-scaling-packtravel) to easily scale PackTravel to reduce latency and support more users.|
|Docs: what: point descriptions of each class/function (in isolation)|3|All modules, Files, Classes, Methods have doc-strings|
|Use of style checkers|3|Configured [pylintrc](https://github.com/VSangarya/PackTravel/blob/main/pylintrc) with Google's Python style-guide|
|Use of code formatters.|3|.vscode [dir](https://github.com/VSangarya/PackTravel/blob/main/.vscode/settings.json) with formatter settings used by every dev|
|Use of syntax checkers.|3| pylint runs on every pull request to check this.|
|Use of code coverage |3|Coverage reports are generated in [build](https://github.com/VSangarya/PackTravel/blob/main/.github/workflows/build.yml) GitHub Action|
|Other automated analysis tools|3|[Codacy](https://app.codacy.com/gh/VSangarya/PackTravel/dashboard?utm_source=github.com&utm_medium=referral&utm_content=VSangarya/PackTravel&utm_campaign=Badge_Grade) for static code analysis|
|Workload is spread over the whole team (one team member is often Xtimes more productive than the others...but nevertheless, here is a track record that everyone is contributing a lot)|3|[GitHub](https://github.com/VSangarya/PackTravel/graphs/contributors)|
|Number of commits|3|[GitHub](https://github.com/VSangarya/PackTravel/pulse)|
|Number of commits: by different people|3|[GitHub](https://github.com/VSangarya/PackTravel/pulse)|
|Issues reports: there are **many**|3|[GitHub](https://github.com/VSangarya/PackTravel/issues?q=is%3Aissue+is%3Aopen%2Cclosed)|
|Issues are being closed|3|[GitHub](https://github.com/VSangarya/PackTravel/issues?q=is%3Aissue+is%3Aclosed)|
|DOI badge: exists|3|[README.md](https://github.com/VSangarya/PackTravel#-PackTravel)|
|Docs: doco generated, format not ugly|3|generated in docs directory - using sphinx, runs on every push to main branch|
|Docs: how: for common use cases X,Y,Z mini-tutorials showing worked examples on how to do X,Y,Z|3|[Video](https://drive.google.com/file/d/1lpd1DkfZUA-zm9XgBw17NZk618qh3YuW/view?usp=share_link)|
|Docs: why: docs tell a story, motivate the whole thing, deliver a punchline that makes you want to rush out and use the thing|3|[README.md](https://github.com/VSangarya/PackTravel#-PackTravel)|
|Docs: short video, animated, hosted on your repo. That convinces people why they want to work on your code.|0|N/A|
|Use of version control tools|3|Git Version Control|
|Test cases exist|3|Tests cases testing urls and views for each django app. They are written using Django Tests and under the "test" folder of each app|
|Test cases are routinely executed|3|Tests are run every pull request by GitHub Actions in [build.yml](https://github.com/VSangarya/PackTravel/blob/main/.github/workflows/build.yml) GitHub action|
|The files CONTRIBUTING.md lists coding standards and lots of tips on how to extend the system without screwing things up|3|Info on style guide, branching strategies, how to raise a PR etc.|
|Issues are discussed before they are closed|3|Discussed on GitHub Issues and PR comments, WhatsApp|
|Chat channel: exists|3|[WhatsApp](../images/chat-channel.png)|
|Test cases: a large proportion of the issues related to handling failing cases.|3|Bugs reported: Issues 2,3,4,6|
|Evidence that the whole team is using the same tools: everyone can get to all tools and files|3|[dev environment setup](https://github.com/VSangarya/PackTravel/blob/main/INSTALL.md#--developer-environment-setup), .vscode [dir](https://github.com/VSangarya/PackTravel/blob/main/.vscode/settings.json) for style configuration|
|Evidence that the whole team is using the same tools (e.g. config files in the repo, updated by lots of different people)|2|Tools/Style and Style checkers were setup as the first commit. All devs pulled these settings. Hence, no further changes were made.|
|Evidence that the whole team is using the same tools (e.g. tutor can ask anyone to share screen, they demonstrate the system running on their computer)|3|Code is deployed on every developer's PC|
|Evidence that the members of the team are working across multiple places in the code base|3|Every dev has worked on writing code, tests, documentation. Evidence in commits.|
|Short release cycles (hard to see in short projects) project members are committing often enough so that everyone can get your work|3|[Git branching strategy](https://github.com/VSangarya/PackTravel/blob/main/CONTRIBUTING.md#branching-strategy) and frequent [pull-requests](https://github.com/VSangarya/PackTravel/pulls?q=is%3Apr+is%3Aclosed)|
|Does your website and documentation provide a clear, high-level overview of your software?|3|[README.md](https://github.com/VSangarya/PackTravel/blob/main/README.md)|
|Does your website and documentation clearly describe the type of user who should use your software?|3| [README.md](https://github.com/VSangarya/PackTravel/blob/main/README.md) Yes, any user looking to carpool, ride together can use our application |
|Do you publish case studies to show how your software has been used by yourself and others?|1|Have shown the use cases, how it can be setup and how it can be improved|
|Is the name of your project/software unique?|3|Yes, no other GitHub projects or other software with the same name exist|
|Is your project/software name free from trademark violations?|3|Yes, no prior software, product, business, design or corporation with the name PackTravel exsists. Verified using Trademark Electronic Search System (TESS).|
|Is your software available as a package that can be deployed without building it?|N/A|It's a web-server application. It needs to be deployed, database needs to be setup.|
|Is your software available for free?|3|Yes, the software is available for free|
|Is your source code publicly available to download, either as a downloadable bundle or via access to a source code repository?|3|Can be downloaded or cloned through Github |
|Is your software hosted in an established, third-party repository likeGitHub (https://github.com), BitBucket (https://bitbucket.org),LaunchPad (https://launchpad.net) orSourceForge (https://sourceforge.net)?|3|Yes, it is hosted on GitHub|
|Is your documentation clearly available on your website or within your software?|3|All required documentation set up via the repositories readme, installation guides and setup steps, auto-generated through sphinx.|
|Does your documentation include a "quick start" guide, that provides a short overview of how to use your software with some basic examples of use?|3|[README.md](https://github.com/VSangarya/PackTravel/blob/main/README.md)|
|If you provide more extensive documentation, does this provide clear, step-by-step instructions on how to deploy and use your software?|2|No additonal documentation present. Installation and set up instructions provide all required details.|
|Do you provide a comprehensive guide to all your software’s commands, functions and options?|2|All functions are described in code. Classes and methods in source code give an overview of the code functionality.|
|Do you provide troubleshooting information that describes the symptoms and step-by-step solutions for problems and error messages?|1|Debugging resources, issues and e-mail information present to assist with troubleshooting.|
|If your software can be used as a library, package or service by other software, do you provide comprehensive API documentation?|N/A|The software does not provide API documentation and cannot be used a package for other software at present|
|Do you store your documentation under revision control with your source code?|3|[Github releases](https://github.com/VSangarya/PackTravel/releases)|
|Do you publish your release history e.g. release data, version numbers, key features of each release etc. on your web site or in your documentation?|3|[Github releases](https://github.com/VSangarya/PackTravel/releases)|
|Does your software describe how a user can get help with using your software?|3|[Github](https://github.com/VSangarya/PackTravel#readme) and [Issues](https://github.com/VSangarya/PackTravel/issues): E-mail address for contact is provided for help regarding the software. Installation and setup guides assist users in setting up and using the software as well|
|Does your website and documentation describe what support, if any, you provide to users and developers?|3|[Github](https://github.com/VSangarya/PackTravel#readme):  E-mail address for contact is provided. Issues tab can used for potential questions and help which will be addressed by one of the project developers|
|Does your project have an e-mail address or forum that is solely for supporting users?|3|[Github](https://github.com/VSangarya/PackTravel#readme) and [Issues](https://github.com/VSangarya/PackTravel/issues): Issues tab on the repository can be used for help regarding the software.|
Are e-mails to your support e-mail address received by more than one person?|3 |Yes all members have access to respective support emails|
Does your project have a ticketing system to manage bug reports and feature requests?|3|Yes ([Issues](https://github.com/VSangarya/PackTravel/issues)  section in GitHub)|
Is your project's ticketing system publicly visible to your users, so they can view bug reports and feature requests?|3|	Yes, it is publicly available|
Software’s architecture and design is modular | 3 | Yes - There are many seperate modules for different functionality in our repository - user, publish, search, request (these are separate django apps)| 
Software uses an accepted coding standard or convention | 3 | Yes, coding standards are followed [Codacy](https://app.codacy.com/gh/VSangarya/PackTravel/dashboard?utm_source=github.com&utm_medium=referral&utm_content=VSangarya/PackTravel&utm_campaign=Badge_Grade)| 
Software allows data to be imported and exported using open data formats | 3 | Data can be imported and exported using json | 
Software allows communications using open communications protocols | 3 | Yes, our website uses HTTP to communicate. | 
Software cross-platform compatible | 3 | Yes - Works on Windows, Mac, Ubuntu | 
Software adhere to appropriate accessibility conventions or standards | 3 | Yes, we followed w3.org standards. | 
Documentation adheres to appropriate accessibility conventions or standards | 3 | yes, added detailed documents for each step  | 
Each source code releases a snapshot of the repository | 3 | Snapshot of latest release is available | 
Releases are tagged in the repository | 3 | Yes, releases are tagged | 
There is a branch of the repository that is always stable | 3 | Main branch is always stable | 
Back-up your repository | 3 | Yes, using git - distributed VCS!!| 
Provide publicly available instructions for building the software from the source code | 3 | Setup instructions [README.md](https://github.com/VSangarya/PackTravel#-PackTravel) | 
Build, or package, the software using an automated tool | N/A | Web-application - needs to be setup | 
Provide publicly-available instructions for deploying the software | 3 | [README.md](https://github.com/VSangarya/PackTravel#-PackTravel) | 
Documentation list all third-party dependencies | 3 | [requirements.txt](https://github.com/VSangarya/PackTravel/blob/main/requirements.txt) | 
Documentation lists the version number for all third-party dependencies | 3 | [requirements.txt](https://github.com/VSangarya/PackTravel/blob/main/requirements.txt)| 
Software list the web address, and licences for all third-party dependencies and say whether the dependencies are mandatory or optional | 3 | All can be downloaded using pip | 
Download dependencies using a dependency management tool or package manager | 3 | All can be downloaded using pip | 
Tests that can be run after your software has been built or deployed to show whether the build or deployment has been successful | 3 | Yes, can be seen in [Github Workflows](https://github.com/VSangarya/PackTravel/blob/main/.github/workflows/build.yml) |
Automated test suite for your software | 3 | [Github Workflows](https://github.com/VSangarya/PackTravel/blob/main/.github/workflows/build.yml) | 
Framework to periodically (e.g. nightly) run your tests on the latest version of the source code | 3 | We run tests when a branch is being merged to main | 
Using continuous integration, automatically running tests whenever changes are made to your source code | 3 | [Build](https://github.com/VSangarya/PackTravel/blob/main/.github/workflows/build.yml)| 
Test results publicly visible | 3 | Yes, the GitHub Actions for build has logs for test-case results. We have a badge for test code-coverage in README.md | 
Manually-run tests documented | N/A | N/A | 
Project has resources (e.g. blog, Twitter, RSS feed, Facebook page, wiki, mailing list) that are regularly updated with information about your software | 3 | All updates on the readme [README.md](https://github.com/VSangarya/PackTravel#-PackTravel) | 
Documentation states how many projects and users are associated with your project | 3 | All users are mentioned in [README.md](https://github.com/VSangarya/PackTravel#-PackTravel) | 
Provide success stories on your website | 0 | Software not yet used publicly | 
Listing the important partners and collaborators in your website | 3 | Github | 
Listing the project's publications on our website or link to a resource where these are available | 0 | No publications | 
Listing third-party publications that refer to the software on our website or link to a resource where these are available | 0 | No publications | 
Users can subscribe to notifications to changes to your source code repository | 3 | Software is on Github | 
Since the software is developed as an open source project (and, not just a project developing open source software), do you have a governance model | 3 | 2 approvers required to merge into main - [pr](https://github.com/VSangarya/PackTravel/pull/14) | 
Do you accept contributions (e.g. bug fixes, enhancements, documentation updates, tutorials) from people who are not part of your project? | 3 | Software is open source, other collaborators can create a pull request for a change | 
Do you have a contributions policy | 3 | [CONTRIBUTING.md](../CONTRIBUTING.md) | 
Is your contributions' policy publicly available? | 3 | [CONTRIBUTING.md](../CONTRIBUTING.md) | 
Do contributors keep the copyright/IP of their contributions | 3 | Commits are public | 
Website and documentation clearly states the copyright owners of your software and documentation | 3 | [README.md](https://github.com/VSangarya/PackTravel#-PackTravel) | 
Does each of your source code files include a copyright statement |  |  | 
The website and documentation clearly state the licence of your software | 3 | [LICENSE](../LICENSE) | 
Software released under an open source licence | 3 | [LICENSE](../LICENSE) | 
Software released under an OSI-approved open-source licence | 3 | [LICENSE](../LICENSE) | 
Source code files include a licence header |  |  | 
Do you have a recommended citation for your software | 3 | Zenodo Badge in [README](https://github.com/VSangarya/PackTravel#-PackTravel) | 
Documentation includes a project roadmap (a list of project and development milestones for the next 3, 6 months) | 3 | Enhancements in [README](https://github.com/VSangarya/PackTravel#-enhancements) | 
Documentation describe how the project is funded, and the period over which funding is guaranteed? | 3 | We used free tools hence no funding required | 
Do you make timely announcements of the deprecation of components, APIs, etc. | 3 | All updates are mentioned in [README](https://github.com/VSangarya/PackTravel#-PackTravel) | 
