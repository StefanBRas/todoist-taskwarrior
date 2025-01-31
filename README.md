# Important

**THIS HAS NOT BEEN TESTED VERY MUCH! USE ON YOUR OWN RISK** - Yes, it could potentially delete tasks so make backups.

This is a fork of [webmeisterei](https://git.webmeisterei.com/webmeisterei/todoist-taskwarrior). All credits for good things should go there and to [matt-snider](https://github.com/matt-snider/todoist-taskwarrior) who initially made the tool.

If it breaks or throws errors you can safely assume that it's because of my code - not theirs.

I THINK this fork will allow you to map labels in todoist with tags in taskwarrior with the --map-tag argument.
Also MAYBE updates done in taskwarrior are corrected synced to Todoist. However i have only done small tests and it might break 
at any time.

As of now, it should only be used for small projects or have one dedicated Todoist <-> Taskwarrior project.

My current use case is to sync a single project with simple tasks from Taskwarrior to Todoist, so I can view and complete them in Todoist's Wear Os app.

At some point I might try to make it more stable. You're free to create issues or make pull requests, but i most likely won't be that active.

### Known bugs

- `Due` dates only works for tasks synced from Todoist to Taskwarrior. It will remove `due` dates from tasks created or modified in taskwarrior
- When syncing at task modified in Taskwarrior or adding one, it will sometimes crash when trying to update `todoist_sync`. This can duplicate tasks as the task will correctly be added in Todoist. 
- You can sync Taskwarrior tasks without a project, but a project will then be added.

### Misc


The rest of the README is directly forked "as is".

# todoist-taskwarrior

A tool for syncing Todoist tasks with Taskwarrior.

## Installation

```bash
git clone https://git.webmeisterei.com/webmeisterei/todoist-taskwarrior.git
cd todoist-taskwarrior/
```

- To install in Virtualenv:

```bash
virtualenv -p /usr/bin/python3 venv
venv/bin/pip install -r requirements.txt
venv/bin/python setup.py install
```

- To install global:

```bash
sudo pip3 install -r requirements.txt
sudo python3 setup.py install
```

## Configure

First optain a Todoist API key from the [Todoist Integrations Settings](https://todoist.com/prefs/integrations).

Now you can configure `titwsync` with (replace `./venv/bin/titwsync` with `titwsync` if you use todoist_taskwarrior without a virtualenv):

```sh
./venv/bin/titwsync configure --map-project Inbox= --map-project Company=work --map-project Company.SubProject=work.subproject --map-tag books=reading <TODOIST_API_KEY>
```

`titwsync configure` writes the configuration to `~/.titwsyncrc.yaml`, with the key: `taskwarrior.project_sync.PROJECT_NAME` you can enable or disable the sync of a whole project!

## Usage

Running the tool requires that your Todoist API key is available from the
environment under the name `TODOIST_API_KEY`. The key can be found or created in
the ).

The main task is `sync` which will sync all tasks. Since Todoist's internal
ID is saved with the task, subsequent runs will detect and skip duplicates:

Replace `./venv/bin/titwsync` with `titwsync` if you use todoist_taskwarrior without a virtualenv.

```sh
./venv/bin/titwsync sync
```

## Development

### Testing

```sh
python -m pytest tests
```

## License

Licensed under the MIT license.

## Authors

- 2018-2019 [matt-snider](https://github.com/matt-snider/todoist-taskwarrior)
- 2019-     [webmeisterei](https://git.webmeisterei.com/webmeisterei/todoist-taskwarrior)
