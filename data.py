def aditis_video():
    name = "Aditi Akella"
    grade = "11th grade"
    about = "Hello! I am Aditi and I am a Junior at Del Norte. I love animals, travel, and science. This is my first year in Mr. M's class and I am learning so much about Python and html files! I look forward to learning more about computers and programming."
    contributions = "Contribution to the Flask Portfolio project: I created the about us page and formatted it. Along with Carter, I created a Navbar and added all the links. I also formatted the home page and added all the links to the projects, repl.its and resources."
    embed = "https://python-hello-series.jmort1021.repl.run"
    info = {"name": name, "grade": grade, "about": about, "contributions": contributions, "embed": embed}
    return info

def carters_video():
    name = "Carter Quartararo"
    grade = "11th grade"
    about = "Whats up! I'm Carter and this is a little about me. I'm a junior at Del Norte that loves to go surfing, hangout with friends. At Del Norte I play water polo which I love. I also love math and science, and now computer science with Mr.M. I am starting to learn a lot and I am becoming excited to code. I can't wait to learn so much more in the future."
    contributions = "Contribution to the Flask Portfolio project: I worked on the navbar and the app routes for the different links within our html project. At first this seemed like a tough task but with some help I was able to complete it."
    embed = "https://python-hello-series.jmort1021.repl.run"
    info = {"name": name, "grade": grade, "about": about, "contributions": contributions, "embed": embed}
    return info

def isais_video():
    name = "Yazhisai Rajaraman"
    grade = "11th grade"
    about = "Hello! I am Isai and I am an eleventh grader at Del Norte. I love reading, watching tv, and dance. This is my first time learning anything regarding Computer Science and it has been a very fun experience. I have learned different types of coding from basic Python fundamentals to .html. I hope to further improve from here."
    contributions = "Contribution to the Flask Portfolio project: I experimented a lot with how to add backgrounds. At first, I thought we could use ascii art for the background. However, I realized that .html tries to conserve as much space as possible so this wasn't a viable option. I inserted an image at the top of the website that fitted the aesthetics of the website and sized it to fit correctly. I also added a file Contents of Our Website that outlines everything in the website for users."
    embed = "https://python-hello-series.jmort1021.repl.run"
    info = {"name": name, "grade": grade, "about": about, "contributions": contributions, "embed": embed}
    return info

def mustafas_video():
    name = "Mustafa Sharaf"
    grade = "11th grade"
    about = "Hello everyone! My name is Mustafa Sharaf, I'm in 11th grade, and I go to Del Norte High School! This is my first time taking a coding class, besides taking coding classes in boot camps. I love learning about new types of code that makes code run faster. My favorite project has been the Rap Name Generator, it was fun to experiment with different types of code in order to display the options in the sub menus."
    contributions = "Contribution to the Flask Portfolio project:I have created and finished a new README.md file for the project,I have organized and cut down the code, and I will work on the comments in the code for users to get a better understanding of code."
    embed = "https://python-hello-series.jmort1021.repl.run"
    info = {"name": name, "grade": grade, "about": about, "contributions": contributions, "embed": embed}
    return info

def sophies_video():
    name = "Sophie Bulkin"
    grade = "11th grade"
    about = "Hi! My name is Sophie Bulkin and I'm a junior at Del Norte High School! In these past two years, I have been in Mr.M's class learning about computer science and I can confidently say that I have learned a lot. I am so excited for the future of this class and the upcoming projects that we will work on! My favorite project so far has been the rap game project becasue I feel like we had a lot of freedom to choose what we did with our code in this project."
    contributions = "Contribution to the Flask Portfolio project: My main contribution was the about us page. i figured out how to add pictures and organize this aspect of our project. I also helped with the main file and fugring out what to do when our dropdown button werent working."


def alldata():
    return [aditis_video(), carters_video(), isais_video(), mustafas_video(), sophies_video()]

#Data "setup" for Projects
#next step would be to extract project data from a database
def setup():
    #Source Data
    name = "Nighthawk Coding"
    github = "https://github.com/nighthawkcoders"
    linkedin = "https://www.linkedin.com/in/john-mortensen-1021/"
    youtube = "https://www.youtube.com/channel/UClIKOsDS5dsfzFA3zveDT3Q?view_as=subscriber"
    twitter = "https://twitter.com/NighthawkCoding"
    source = {"name": name, "github": github, "linkedin": linkedin, "youtube": youtube, "twitter": twitter}
    #Project Data
    project1 =  "Hello Series"
    projlinks1 = [
        Link("Project Plan", "http://nighthawkcoders.cf/courses/python/"),
        Link("Repl", "https://repl.it/@jmort1021/Python-Hello-Series#README.md"),
        Link("Resources", "https://padlet.com/jmortensen7/csp2021")
    ]
    project2 =  "Flask Project"
    projlinks2 = [
        Link("Project Plan", "http://nighthawkcoders.cf/courses/python/"),
        Link("Repl", "https://repl.it/@jmort1021/Python-Web-Portfolio-Series?__cf_chl_jschl_tk__=cff72504752e89d50dea999ce10f859a17ecc294-1603026111-0-AdBP5FO-3nyUc_KVdPlNwvXM4MwUXy1HXHmbiJui1YBnUTPJZ8X4UBZVeYUXrnwRBJVvku9NftGYDWtp8lp4KovKX55R8S4twedzHpa2snwLwoAWaxuc4rgAa2l9J_rWqnNvUNcjJ8-p1V1RuTWV3lIy149lptozqAQdJnGj7PlcJxnu3YH22EXK-jl7bmdQmW9r_9fE1xp8J7sOFS3I1PMgmtoExcDIQSBBTnx1zQsyQGNS6wnuX72MAPnS_x3ZL1ETNRgFbVKpLsFJiR9ED1ErU54wyZYrUxEbZ_txHd7qY1T_s_lE6Ll8jYWHx-GulQ#main.py"),
        Link("Resources", "https://padlet.com/jmortensen7/csptime1_2")
    ]
    #Project Objects
    proj1 = Project(project1, projlinks1)
    proj2 = Project(project2, projlinks2)
    #HTML Data
    projects = Projects(source, [proj1, proj2])
    return projects

#Link class contains button (label) and hypertext reference (href)
class Link():
    #link data with button and href (url)
    def __init__(self, btn, href):
        self.btn = btn
        self.href = href
    def get_btn(self):
        return self.btn
    def get_href(self):
        return self.href

#Project data class contain project name and links (Link class objects)
class Project():
    #project data with name and links
    def __init__(self, name, links):
        self.name = name
        self.links = links
    def get_name(self):
        return self.name
    def get_links(self):
        return self.links

#Projects class contains person (owner) and multiple projects (Project class objects)
class Projects():
    #HTML data with source and projects
    def __init__(self, source, projects):
        self.source = source
        self.projects = projects
    #source data getter
    def get_source(self):
        return self.source
    #project data getter
    def get_projects(self):
        return self.projects