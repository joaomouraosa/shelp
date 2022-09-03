INFO = {
    'crontab': {
        'Syntax': ['mm(0-59) hh(0-23) dd_month(1-31) mm(1-12) dd_week(1-7) script'],
        'Edit': [
            '$ crontab [-u user] -e',

        ],
        'List': ['$ crontab [-u user] -l'],
        'Logs': ['$ grep CRON /var/log/syslog'],
        'Stop': ['$ systemctl [status/restart/stop/start] cron'],
        'Example': [
            '# Run script.sh every day at 1pm)',
            '00 13 * * * cd /home/user/folder && bash script.sh'
        ]
    },
    'shebang': {
        'About': ['The hashbang or shebang tells the program loader how to interpret/run the file'],
        '#!/bin/bash': ['Tells the OS to use bash as the interpreter for parsing the remaining code'],
        '#!/usr/bin/python': ['Tells the shell to interpret the code as python code'],
        '#!/usr/bin/env python3': []
    },
    'permissions': {
        'See the ownership and permissions': [
            '$ ls -l FILE', '> [Permissions] [Owner] [Owner group] FILE'
        ],
        'Permissions': [
            'R W X | R - - | R - X',
            '(USER) (GROUP) (OTHER)',
            '',
            '(USER)   Owner of the file. By default, the person who created a file becomes its owner.',
            '(GROUP)  All users belonging to a group share the same permissions. Avoids having to manually assign the same permissions to each user.',
            '(OTHER)  Everybody else. Setting the permission for others is also referred as set permissions for the world.',
            'R: Allows to open and read the file',
            'W: Allows to open and modify the file',
            'X: Allows to open and run the file',
            '-: No permission',
        ],
        'Change the permissions': ['Refer to chmod ->'],
        'Change the ownership': ['Refer to chown ->', ],
        'Create a group': ['Refer to chgrp ->', ],

    },
    'which': {
        "About":    ["Searches the PATH for executable matching the name given as argument and returns the path."],
        "Syntax":   ["$ which [NAME]    (or)    $ which -a [NAME]"],
        "Flags":    ["-a     returns all matching paths"],
        "Examples": [
            "$ which python3",
            "> /usr/bin/python3", '',
            "$ which -a python3",
            "> /usr/bin/python3",
            "> /bin/python3",

        ],

    },
    'ln': {
        'About': [
            'A symbolic link is a file type that acts as an indirect pointer to a file, like a shortcut in Windows.',
            'Also known as symlink or soft link, it can point to a file or a directory on a different filesystem or partition.',
        ],
        'Create': ['$ ln -s SOURCE LINK',
                   '* ln creates a LINK file to the SOURCE file',
                   '* EG: ln -s /home/user/my_file /usr/bin/my_symlink'
                   ],
        'Overwrite': ['$ ln -s --force SOURCE LINK',
                      '* EG: ln -s /home/user/other_file /usr/bin/my_symlink'
                      ],
        'Remove': ['$ unlink LINK',
                   'Alternative: just remove it like a regular file ($ rm LINK)',
                   '* EG: unlink /usr/bin/my_symlink'
                   ],
    },
    'directories': {
        '/usr/bin\n/sbin\n/bin': [
            'Package-managed executables. Leave them alone.'
        ],
        '/usr/local/bin/': [
            'Use it to store scripts or executables. Already in the PATH.',
            'Available to everyone in the system'
        ],
        '$HOME/.local/bin': [
            'Use it to store scripts or executables. Only available to the user'
        ],
        'more...': ['todo'],
    },
    'webm': {
        'Flags': [
            "-crf [N] Constant rate factor. 0: lossless, 17: virtually lossless, 23: default, 51: worst.",
            "-l [N]   Size limit",
            "-vw [N]  Width size (in pixels)",
            "-vh [N]  Height size (in pixels)",
        ],
        'Examples': [
            '# Lossless encoding (overkill): $ webm -crf 0  -i INPUT.mp4 -an -o OUTPUT.webm -speed 0 ' ,
            '# Virtually lossless encoding:  $ webm -crf 17 -i INPUT.mp4 -an -o OUTPUT.webm -speed 0 ',
            '# Encode up to a size limit:    $ webm -l 3.05 -i INPUT.mp4 -an -o OUTPUT.webm -speed 0 ',
            '# Change the scale:             $ webm -vw 720 -i INPUT.mp4 -an -o OUTPUT.webm -speed 0 '
            '']
        ,
    },
    'xargs': {
        'About': [
            'Executes a command (default is echo) with args read from the STDIN (delimited by blanks or newlines)',
        ],
        'Syntax': [
            '$ [INPUT] | xargs [COMMAND]   (OR)   $ [INPUT] | xargs -I {} [COMMAND] {}', '',
            '# Run multiple commands',
            '$ [INPUT] | xargs -I {} bash -c \'[CMD1] && [CMD2]\' ', '',
            '# If and else logic',
            '$ [INPUT] | xargs -I {} bash -c \'if [CONDITION]; then [OPERATION]; fi\' ', '',
        ],
        'Other flags': [
            '-0 \t Takes care of inputs with blank spaces (eg file names). EG: $ find . -name "*.mp4" | xargs -0 [CMD]',
            '-n [N] \t Take at most N arguments each time. EG: $ [INPUT] | xargs -n [N] [CMD]',
            '\t $ echo 1 2 3 4 | xargs -n 2 echo',
            '\t > 1 2',
            '\t > 3 4',
        ],
        'Examples': [
            '$ echo 1 2 3 4 | xargs   (OR)   $ echo 1 2 3 4 | xargs echo',
            '> 1 2 3 4', '',
            '# Remove all .bak files in the current directory',
            '$ find . -name "*.bak" -type f | xargs /bin/rm -f',
            '',
            '# Converts files to webm and moves them to a folder',
            '$ find . -maxdepth 1 -name "*.mp4" | xargs -I {} sh -c \'webm -i {} -o "{}.webm" && mv "{}" ./converted\'',
            '',
            '# Converts files to webm if they are smaller than 5MB',
            '$ find . -maxdepth 1 -name "*.mp4" | xargs -I {} sh -c \'',
            '                if [ `du {} | cut -f1` -gt 5000 ]; then webm -i {} -o "{}.webm"; fi\''

        ],
    },
    'du': {
        'About': ['Summarize disk usage of the set of FILEs, recursively for directories.'],
        'Syntax': ['$ du [Flags] [FILES...]'],
        'Flags': [
            '--max-depth [N]    Max depth                                              ',
            '--all              Include files as well',
            '-h                 Print sizes in human readable format (e.g., 1K 234M 2G)',

        ],
        'Examples': [
            '# Specific file   ',
            '   $ du -h file.txt',
            '   > 20K file.txt',
            '# Folder          ',
            '   $ du folder',
            '   > 8	folder',
            '# Everything in a folder',
            '   $ du --all folder',
            '   > 4  folder/file.txt',
            '   > 4  folder/dir/file.txt',
            '   > 8  folder/dir',
            '   > 16 folder',
        ],

    },
    'find': {
        'About': [
            'Walks through a dir hierarchy to find files/dirs. Additionally, can perform operations on them (-exec).'
        ],
        'Syntax': ['$ find [WHERE] [WHAT] [OPTIONS] '],
        'Flags': [
            '-name [file]   Search for files that are specified by name.',
            '-type [TYPE]   Searches for files if TYPE==\'f\'. Directories if \'d\'.' ,
            '-maxdepth [N]  1: only searches in the current directory. 2: allows subdirs. 3: subsubdirs. And so on.',

            '-newer [file]  Search for files modified/created after [file].',
            '-user [name]   Search for files owned by [user] name',
            '-empty         Search for empty files and directories',
            '-size ([N] |+[N] |-[N] |[N]c)   Search for files with N/>N/<N blocks/chars',
        ],
        'Execute a command': [
            '-exec [CMD] \;   Execute a command',
            '-ok [CMD]   \;   Same as -exec, except the user is prompted first.',
        ],
        'Examples': [
            '# Search a specific file)      $ find ./folder -type f -name file.txt',
            '# Find and remove a file)      $ find ./folder -type f -name file.txt -exec rm -i {} \; ',
            '# Search with a pattern)       $ find ./folder -type f -name "*.txt"',
            '# Find text in multiple files) $ find ./folder -type f -name "*.txt" -exec grep \'test\' {} \; ',
        ]
    },
    'sort': {
        "Syntax": ["[INPUT] | sort [OPTIONS]   (or)   sort [Options] [INPUT]"],
        "Options": [
            "-r Sort in reverse order",
            "-n Numerically",
            "-k [N] sort by column [N]",
            "-c check if it's sorted or not",
            "-u remove duplicates"
        ],
        "Examples": [
            " $ cat file.txt",
            " > A B 2",
            " > B A 1",
            "# Sort by column 1)                $ cat file.txt | sort -k1",
            "                                   > A B 2",
            "                                   > B A 1",
            "# Sort numerically by column 3)    $ cat file.txt | sort -n -k3",
            "                                   > B A 1",
            "                                   > A B 2",
            "# Reverse sort)                    $ cat file.txt | sort -n -k3 -r",
            "                                   > A B 2",
            "                                   > B A 1",
        ]
    },
    'shell': {
        'Function': [
            'var=\'A\'',
            'fun() { ',
            '  var=\'B\'',
            '  local result="var=$var, arg=$1"',
            '  echo "$result"',
            '}',
            'result="$(fun "arg")"',
            'echo $result',
            '> var=B, arg=arg',
            'echo $var',
            '> A',
        ],
        'Loop': {
            'While': [
                'while true',
                'do',
                '  echo "Press [CTRL+C] to stop.."',
                'done',
            ]
        }
    },
    'cut': {
        'About': ['Cuts out sections from each line of FILES and returns them to STDOUT.'],
        'Syntax': ['cut [Flags...] [FILE...]'],
        'Flags':[
            '-b [N]                         Extracts the byte at index N ',
            '-c [N]                         Extracts the char at index N ',
            '-c [N1,N2]                     Chars at indices N1 and N2',
            '-c [N1-Nn]                     The range of chars from N1 to Nn',
            '-c [N-]                        The range of chars from N to the end of a line',
            '-c [-N]                        The range of chars from 1 to N', '',
            '-f [N] -d [DELIM]              Splits by DELIM and extracts the field N',
            '--complement                   Negates the output. Eg: $ echo "a b c" | cut -c 1   ~> " b c"',
            '--output-delimiter=\'%\'         Eg: $ echo "a b" | cut -c1 --output-delimiter=\'%\' ~> "a%b"'
        ],
        'Examples': [
            '# Select the 1st char)             $ echo "a b c" | cut -c 1',
            '                                   > b',
            '# Select the 1st and 2nd chars)    $ echo "a b c" | cut -c 1,3',
            '                                   > a b',
            '# Using a delimiter)               $ echo "a b c" | cut -f 1-2 -d " "',
            '                                   > a b',
            '# Changing the output delimiter)   $ echo "a b c" | cut -f 1-2 -d ' ' --output-delimiter=\',\'',
            '                                   > a,b',
            '# Negate the result)               $ echo "a b c" | cut -f 1-2 -d ' ' --output-delimiter=\',\' --negate',
            '                                   > c',
            '# Multiple spaces)                 $ echo "a  b c"| awk \'{ print $2 }\''
            '                                   > a',

        ],
    },
    'how-script': {
        "1 specify the interpreter": [
            '#!/bin/bash        Tells the OS to use Bash as the interpreter for parsing the remainder of the script',
            '#!/usr/bin/python  Same for Python',
            '- Other options:   #!/usr/bin/env python3    (...)'
        ],
        "2 make it executable for all users": [
            '$chmod +x [FILE]'
        ]
    },
    'ffmpeg': {
        "About": [],
        "Flags": [
            "-ss              start time, e.g. 00:01:23.000 or 83 (in seconds)",
            "-to              end time, e.g. 00:01:23.000",
            "-t               duration (e.g. 83)",
            "-c:v [CODEC]     Sets the codec to encode the video stream",
            "-c:a [CODEC]     sets the codec to encode the audio stream",
            "-c copy          Copies the video and audio streams from the input to the output without re-encoding them.",
            "-vf scale=[W:H]  Resizes the video to a specific size. ",
            "-vf scale=[W]:-1 Resizes the width keeping the aspect ratio. ",
            "-vf scale=-1:[H] Resizes the height and keeps the aspect ratio. ",
        ],
        "Examples": [
            "# cut (lossless):       $ ffmpeg -i [INPUT] -c copy [OUTPUT] -ss [START] -t [DURATION]",
            "# cut with re-encoding: $ ffmpeg -i [INPUT] -c:v [CODEC] -c:a [CODEC] -ss [START] -t [DURATION] [OUTPUT]",
            "# merge videos:         $ printf \"file \'/path/file1\'",
            "                                  file \'/path/file2\'\" > list.txt",
            "                        $ ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4",
            "# merge videos (alt)    $ mkvmerge -o output.mkv input1.mkv + input2.mkv",

        ],
    },
    'how-to-free-space': {
        'General': [
            'Find the biggest files:                    $ sudo find / -size +1G',
        ],
        'Root': [
            '# Remove downloaded deb files from cache:  $ sudo apt-get clean',
            '# Remove cached apt archives:              $ sudo apt autoclean',
            '# Remove unused packages and libs:         $ sudo apt autoremove',
        ],
        'Docker': [
            '# Find how much space can be reclaimed:    $ docker system df',
            '# Remove dangling images                   $ docker system prune',
            '# Deep clean (prune with force)            $ docker system prune -af --volumes',
        ],
        'Logs': [
            '# Check logs size:                         $ journalctl --disk-usage',
            '# Remove logs older than X days            $ sudo journalctl --vacuum-time=3d',
        ],
        'Thumbnails': [
            '# Check the thumbnail cache size:          $ du -sh ~/.cache/thumbnails',
            '# Remove the cached thumnails              $ rm -rf ~/.cache/thumbnails/*',
        ],
        'Duplicates': [
            '# Find and remove duplicates:              $ fdupes -rSd ~/folder',
        ]
    },
    'fdupes': {
        "About": ["Identifies duplicate files in a specific folder"],
        "Syntax": ["$ fdupes [Flags] [DIR]"],
        "Flags": [
            "-r             Searches in sub directories as well",
            "-S             Show the size of duplicate files",
            "--summarize    Summarize duplicated files info",
            "-d             Asks what file to keep and remove the duplicates"
        ],
        "Examples": [
            "# Find duplicates in a folder:                         $ fdupes ~/folder",
            "# Find duplicates in a folder and sub directories:     $ fdupes -r   ~/folder",
            "# Shows the size of duplicate files:                   $ fdupes -rS  ~/folder",
            "# Find and remove duplicates:                          $ fdupes -rSd ~/folder",
            "# Shows duplicates and how much space they are using:  $ fdupes -rS --summarize ~/folder",
        ],
    },
    'source': {},
    'export': {},
    'bashrc': {},
    'top': {},
    'awk': {},
    'git': {
        "Examples": [
            '# Cloning from a remote repo with SSH:      $ git clone git@gitlab.com:aa.git',
            '# Merge a remote branch into the local one: $ git pull origin master',
            '# Stage the local changes on file1:         $ git add file1',
            '# Make sure the changes are saved locally:  $ git commit -m "commit message"',
            '# Push the local branch to the remote:      $ git push -u origin master'
        ],
        "Other commands": [
            '$ git init     # Creates an empty repository. A .git folder is created ',
            '$ git checkout # Allows to switch branches',
            '$ git status   # Tells the current state of the repository',
            '$ git config   # Configures the user.name and user.email ',
        ],
        "Branch": [
            '* Branches are isolated development environments withing a repository',
            '# View branches:                              $ git branch ',
            '# Create a new branch:                        $ git branch <branch>',
            '# Removing a branch:                          $ git branch -d <branch> ',
            '# Push the new branch to the remote repo:     $ git push -u <remote> <branch>',
            '# Merge the staging branch to the stable one: $ git merge <branch> ',
        ],

        "Authentication": [
            '# 1) Paste your pub key in https://github.com/settings/ssh/new',
            '  $ ssh-keygen -t ed25519 -C [EMAIL] && ssh-add ~/.ssh/id_ed25519.pub',
            '# 2) Check if you are connected to github',
            '  $ ssh -T git@github.com',
            '# 3) Switch remote URLs from HTTPS to SSH',
            '  $ git remote set-url origin git@github.com:[USERNAME]/[REPO].git'
        ]
    },
    "python": {
        "Environment": [
            "# Create an environment:           $ python3 -m venv [PATH]",
            "# Activate an environment:         $ source [PATH]/bin/activate",
            "# Deactivate:                      $ deactivate",
        ],
        "Packages": [
            "# List installed packages:          $ pip list",
            "# Install a package:                $ pip install [PACKAGE]",
            "# Install from a requirements file: $ pip install -r requirements.txt",
            "# Save the env packages to a file:  $ pip freeze > requirements.txt",
        ]
    },
}

# create a token, use it in the password field of the git push -u origin master

# if [ ! -d "$DIR" ]; then echo "The path provided doesn't exist. Quitting..."; exit 1; fi

# 0A30-79AF