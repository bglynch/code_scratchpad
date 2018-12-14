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
