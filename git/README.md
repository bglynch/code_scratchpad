# Git Basics
### Commit Messages
Commit: Single  message
```
$ git commit -m "your commit message"
```
Commit: Title and description
```
$ git commit -m "Your Title" -m "your commit message"
```
Commit: Title and description split into seperate lines using ```$'\n'```
```
$ git commit -m "Your Title" -m "message first line"$'\n'"message second line"
```


### Add changes to a previous commit
1. First add the modified file(s)
```
$ git add .
```
2. Ammend the changed files to the previous commit
```
git commit --amend
```
or
```
git commit --amend --no-edit
```



### Squashing

> ```bash
> # view commits since branch cut
> git log --oneline master..CTP-2594-deprecate-global-api
> 
> # get number of commits between current branch and master
> git rev-list --count master..current_branch
> >> 12
> 
> # reset to the branch cut of the current branch
> git reset --soft HEAD~12
> 
> ...stage commits
> 
> git commit -m "commit for all the changes"
> git push origin current_branch --force
> ```

