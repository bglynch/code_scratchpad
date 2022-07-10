# VS Code

### Commands

**Command Palette** (⇧⌘P)
Quick Open (⌘P)

### Settings
##### Links
- https://code.visualstudio.com/docs/python/settings-reference#_predefined-variables

##### Locations
Two types of settings
- global settings
  - `code ~/Library/Application Support/Code/User/settings.json` or
  - ⇧⌘P -> type "settings"
- workspace settings (.vscode/settings.json), settings that are specific to that workspace

##### Useful Settings
```json
"editor.rulers": [88],

// view git files
"files.exclude": {"**/.git": false}

// manually add file to PATH
"python.analysis.extraPaths": ["/Users/brianlynch/Desktop/project/src/library"]
"python.formatting.provider":	"black"
```


## Debugging

#### Useful Links

- Debugging
  - https://code.visualstudio.com/docs/python/debugging
  - https://code.visualstudio.com/docs/remote/remote-overview

### Set Up

Either manually create file `touch /.vscode/launch.json` or use the UI on the debugging tab to create it.

### Basic outline

```json
{
    "version": "0.2.0",
    "configurations": [
      
        // list of configurations here  
      
    ]
}
```

#### Configurations

```json
// ===== Current file
{
  "name": "Python: Current File",
  "type": "python",
  "request": "launch",
  "program": "${file}",
  "env": {
    "FLASK_ENV": "development"
  }
},

// ===== Docker
{
  "name": "Python Attach",
  "type": "python",
  "request": "attach",
  "pathMappings": [
    {
      "localRoot": "${workspaceFolder}/python/src/",
      "remoteRoot": "/work"
    }
  ],
  "port": 5678,
  "host": "127.0.0.1"
},

// ===== Flask
{
  "name": "Python: Flask",
  "type": "python",
  "request": "launch",
  "module": "flask",
  "env": { "FLASK_APP": "app.py", "FLASK_ENV": "development" },
  "args": ["run", "--no-debugger"],
  "jinja": true,
  "justMyCode": true
},
```



## Change Colors

```json
/* .vscode/settings.json */
{
  // add color to activity bar
  // UI Interface component names: https://code.visualstudio.com/docs/getstarted/userinterface
  // https://code.visualstudio.com/api/references/theme-color#activity-bar
  "workbench.colorCustomizations": {
    "activityBar.background": "#195219",
    "statusBar.background": "#195219"
  },
}

```

