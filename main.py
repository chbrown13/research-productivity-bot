import github
import datetime

def _send_email():
    pass

def report(user, day):
    words = 0
    lines = 0
    for repo in user.get_repos():
        commits = repo.get_commits(since=day)
        print(commits.totalCount)
   
def main():
    git = github.Github("auth_token")
    user = git.get_user()
    today = datetime.datetime(datetime.datetime.today().year, 
        datetime.datetime.today().month, 
        datetime.datetime.today().day)
    report(user, today)



if __name__ == "__main__":
    main()
