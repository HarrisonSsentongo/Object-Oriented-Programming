# pylint: disable=all

class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        # Attributes
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

#Introducing myself
    def introduce(self):
        print(f"Hi, I’m {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}.")
        print(f"Fun fact about me: {self.fun_fact}")

#Showing my tech stack:
    def show_stack(self):
        print("\nMy Tech Stack includes the following:")
        for tool in self.tech_stack:
            print(f" - {tool}")

#Returning my GitHub profile link:
    def github_link(self):
        return f"https://github.com/{self.github_username}"


#Script execution:
if __name__ == "__main__":
    # Creating an instance of Profile:
    my_profile = Profile(
        name="Ssentongo Mark Harrison",
        favorite_language="Python",
        hobby="Bike riding",
        tech_stack=["Python", "Git", "JavaScript", "React"],
        github_username="HarrisonSsentongo",
        fun_fact="I can trade forex while sipping coffee."
    )

#Calling back the methods:
    my_profile.introduce()
    my_profile.show_stack()
    print("\nGitHub Profile:", my_profile.github_link())
