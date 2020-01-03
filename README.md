# Github Committer (Dockerized)
Project with a purpose of auto-committing to your github projects to maintain activity level.

1. Pings App API via Jenkins CRON job with a JSON request:
```
{
 directory_name[str] : directory_address[str],
 etc...
}
```
2. App cycles through directories, uses `git init` and sets master branch upstream to connect to remote repository
3. App adds a simple and trivial update, commits, and pushes to master for each of the dirs
4. App waits for next API call


Credit:
Main committer code taken from https://github.com/alexbod/github-auto-committer
