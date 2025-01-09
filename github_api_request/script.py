import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from argparse import ArgumentParser

#Get response data with Github API
def get_activity(username):
    try:
        url = f"https://api.github.com/users/{username}/events"
        request = Request(url)
        with urlopen(request) as response:
            return json.loads(response.read().decode())
    except HTTPError as error:
        if error.code == 404:
            print("User not found.")
        else:
            print(f"HTTP error {error.code}: {error.reason}")
    except URLError as error:
        print(f"URL error: {error.reason}")
    except Exception as error:
        print(f"Error: {error}")

    return None

#Parse the response data and make it readable
def parse_activities(activities):
    if not activities:
        return "No activities found."
    user_activities = []
    for activity in activities:
        repo = activity["repo"]["name"]

        if activity["type"] == "PushEvent":
            user_activities.append(f"- Pushed {activity["payload"]["size"]} commit(s) to {repo}.")
        elif activity["type"] == "CreateEvent":
            user_activities.append(f"- Created {repo} repository.")
        elif activity["type"] == "DeleteEvent":
            user_activities.append(f"- Deleted {repo} repository.")
        elif activity["type"] == "ForkEvent":
            user_activities.append(f"- Forked {repo} repository.")
        elif activity["type"] == "IssueEvent":
            user_activities.append(f"- {activity["payload"]["action"].capitalize()} an issue on {repo}.")
        elif activity["type"] == "IssueCommentEvent":
            user_activities.append(f"- {activity["payload"]["action"].capitalize()} a comment on {repo}.")
        elif activity["type"] == "PullRequestEvent":
            user_activities.append(f"- {activity["payload"]["action"].capitalize()} a request on {repo}.")
        elif activity["type"] == "WatchEvent":
            user_activities.append(f"- Starred {repo}.")
        else:
            user_activities.append(f"- Did something on {repo}.")

    return user_activities

#Parse user's command from the CLI and run the script
def main():
    parser = ArgumentParser(description="A CLI tool that fetches a github user's activity.")
    sub_parser = parser.add_subparsers(dest="command", required=True)
    
    cmd_parser = sub_parser.add_parser("github-activity", help="Get a user's recent activities list.")
    cmd_parser = cmd_parser.add_argument("username", help="Github username.")

    argument = parser.parse_args()

    if argument.command == "github-activity":
        activities_list = get_activity(argument.username)
        if not activities_list:
            return
        user_parsed_activities = parse_activities(activities_list)
        print("Output:")
        print("\n".join(user_parsed_activities))

if __name__ == "__main__":
    main()
