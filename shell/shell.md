# Shell Commands

[TOC]

## cURL

> ###### flags
>
> ```bash
> -i, --include               Include  the  HTTP  response  headers  in  the  output.
> -G, --get
> -v, --verbose               Makes curl verbose during the operation
> -d, --data <data>           Sends the specified data in a POST request to the HTTP server
> -X, --request <command>     (HTTP) Specifies a custom request method to use when communicating with the HTTP server
> -o, --output <file>         Write  output  to <file> instead of stdout.
> -u, --user <user:password>  Specify the user name and password to use for server authentication
> ```
>
> ###### examples
>
> ```bash
> curl https://www.baeldung.com/                                       # GET request
> curl -d "first=Brian&last=Lynch" https://www.baeldung.com/           # POST request
> curl -X PUT -d "first=Brian&last=Murray" https://www.baeldung.com/   # PUT request
> curl -X DELETE https://www.baeldung.com/                             # PUT request
> curl -u brian:password https://www.baeldung.com/                     # Add username and password
> curl -o test.txt https://www.baeldung.com/                           # Download response
> 
> -i: 
> --data, -d: 
> --output, -o:
> ```

## sed

> - **S**tream **Ed**itor
> - **Note: **Basic vs. extended regular expressions
>   **basic regular expressions**: metacharacters **?**, **+**, **{**, **|**, **(**, and **)** lose their special meaning; 
>   instead use the backslashed versions **\?**, **\+**, **\{**, **\|**, **\(**, and **\)**.
>   **GNU grep -E** attempts to support traditional usage by assuming that **{** is not special if it would be the start of an invalid interval specification. 
>   For example, the command **grep -E '{1'** searches for the two-character string **{1** instead of reporting a syntax error in the regular expression
>
> ###### flags
>
> ```bash
> -E                Interpret regular expressions as extended regular expressions 
> -r                Same as -E for compatibility with GNU sed.
> -i <extension>    Edit files in-place similarly to -I, but treat each file independently from other files.
> ```
>
> ###### regex 
>
> ```bash
> \d does not work for sed, use [0-9] or [[:digit:]]
> ```
>
> ###### regex: get group 
>
> ```bash
> # extract group
> echo employee_id=1234 | sed -E 's/employee_id=([0-9]+)/\1/'
> 	# >>> 1234
> ```
>
> ###### regex: replacement
>
> ```bash
> # replace employee with emp
> echo employee_id=1234 | sed 's/employee/emp/'
> 	# >>> "emp_id=1234"
> 
> # replace 'bar' with 'baz'
> echo "An alternate word, like bar, is sometimes used in examples." | sed 's/bar/baz/'
> 
> # Replace all occurances of `foo' with `bar' in the file test.txt, without creating a backup of the file
>   sed -i '' -e 's/foo/bar/g' test.txt
> 
> # Regex Replce with group and color
> sed -E 's/\[(ERROR)/'$'[\033[91m\\1\033[0m/'
> 
> # Add 'g' to end to replace multiple occurances
> sed -E 's/\[(200 OK)\]/'$'\033[32m[\\1]\033[0m/g'
> ```
>
> ###### different seperator
>
> ```bash
> # Using backlashes can sometimes be hard to read and follow
>   echo "/home/example" | sed  's/\/home\/example/\/usr\/local\/example/'
> # Using a DIFFERENT SEPERATOR can be handy when working with paths
>   echo "/home/example" | sed 's#/home/example#/usr/local/example#'
> ```

## grep 

> - **G**lobal **R**egular **E**xpression **P**rint
> - line-by-line search utility
>
> ###### flags
>
> ```bash
> -A num, --after-context=num  Print num lines of trailing context after each match
> -B num, --before-context=num Print num lines of leading context before each match
> -C num, --context=num        Print num lines of leading and trailing context surrounding each match. Default is 2, is equivalent to -A 2 -B 2
> 
> -e pattern, --regexp=pattern
> -E, --extended-regexp     Interpret pattern as an extended regular expression (force grep to behave as egrep)
> -i, --ignore-case         case insensitive matching   
> -l, --files-with-matches  give the file name of matching files.
> -n, --line-number         Each output line is preceded by its relative line number in the file
> -o, --only-matching       Prints only the matching part of the lines
> -R, -r, --recursive       Recursively search subdirectories listed   
> -v, --invert-match        Selected lines are those not matching any of the specified patterns
> -w, --word-regexp         match the whole word.
> --context[=num]           Print num lines of leading and trailing context.  The default is 2.
> 
> --exclude         excludes files matching the given filename pattern from the search
> --include         only files matching the given filename pattern are searched (--exclude take priority)
> --exclude-dir     if -R specified, excludes directories matching given filename pattern from the search
> --include-dir     if -R specified, only directories matching the given filename pattern are searched
> --line-buffered   Force output to be line buffered
> ```
>
> ###### examples
>
> ```bash
> # To find all occurrences of the word `patricia' in a file
> grep 'patricia' myfile
> 
> # find all occurrences of the pattern `.Pp' at the beginning of a line
> grep '^\.Pp' myfile
> 
> # To find all lines in a file which do not contain the words `foo' or `bar'
> grep -v -e 'foo' -e 'bar' myfile
> 
> # find all files containing specific text
> grep -rnw '/path/to/somewhere/' -e 'pattern'
> 
> echo employee_id=1234 | grep employee       
>   ' -> employee_id=1234                   '
> echo employee_id=1234 | grep -o employee    
>   ' -> employee                           '
> 
> # get files that match the word "test_log_audit_data_success"
> grep -rnw src/tests -e test_log_audit_data_success 
>   ' -> Binary file src/tests/helpers_tests/__pycache__/test_queue_events.cpython-38-pytest-7.1.2.pyc matches                                     '
>   ' -> Binary file src/tests/helpers_tests/__pycache__/test_queue_events.cpython-38-pytest-6.2.5.pyc matches                                     '
>   ' -> src/tests/helpers_tests/test_queue_events.py:145:    def test_log_audit_data_success(                                                     '
>   ' -> src/tests/.pytest_cache/v/cache/nodeids:74:  "helpers_tests/test_queue_events.py::TestQueueEvents::test_log_audit_data_success",          '
>   ' -> src/tests/.pytest_cache/v/cache/lastfailed:2:  "helpers_tests/test_queue_events.py::TestQueueEvents::test_log_audit_data_success": true   '
> 
> # only get .py files
> grep -rnw src/tests --include=\*.py -e test_log_audit_data_success   
>   ' -> src/tests/helpers_tests/test_queue_events.py:145:    def test_log_audit_data_success(   '
> 
> # get filename only
> grep -rwl src/tests --include=\*.py  -e test_log_audit_data_success
>   ' -> src/tests/helpers_tests/test_queue_events.py                                         '
> ```

## head

> - read the file from the beginning

## tail

> - displays the contents of file or, by default, its standard input, to the standard output.
>
> ###### flags
>
> ```bash
> -f, --follow    doesnt stop when end of file reached, 
> 								waits for additional data to be appended to the input
> -n, --lines     Prints the last ‘num’ lines instead of default(last 10 lines)
> -v, --verbose
> ```
>
> ###### examples
>
> ```bash
> tail myfile.txt
> 
> # Outputs the last 100 lines of the file myfile.txt.
> tail -n 100 myfile.txt
> 
> # Outputs the last 10 lines of myfile.txt, and monitors myfile.txt for updates;
> tail -f myfile.txt
> ```

## tree

> reads a file, and outputs the last part of it (the "tail")
>
> ###### Flags
>
> ```bash
> -d             List directories only
> -l             Follows symbolic links if they point to directories
> -C             Turn colorization on always
> 
> -I <pattern>   Do not list those files that match the wild-card pattern
> -P <pattern>   List only those files that match the wild-card pattern
> -L <level>     Max display depth of the directory tree
> ```
>
> ###### examples
>
> ```bash
> tree -L 2
> 
> # Displays a tree without anything beginning with example or containing 'bin' or 'lib'
> tree -I 'example*|bin|lib'
> 
> # displays a tree only containing directories/files beginning with t
> tree -P 't*'
> ```

## ssh - OpenSSH SSH client (remote login program)

> - Useful Links
>   - https://www.youtube.com/watch?v=vpk_1gldOAE&t=698s&ab_channel=CoreySchafer
>   - https://code.visualstudio.com/docs/remote/remote-overview
>   
>
> ```bash
> # enter the shell of a remote machine
> ssh <user>:<host ip address>
> 
> # create ssh key
> ssh-keygen -t rsa -b 4096 -C "{YOUR_EMAIL}"
> 
> # add local key to remote machine
> ssh-copy-id -i ~/.ssh/id_rsa.pub <user>:<host ip address>
> ```

## scp

> - **Secure Copy**
> - allows you to securely copy files and directories between two locations.
>
> ###### Flags
>
> ```bash
> -p         Preserves files modification and access times
> -q         Use this option if you want to suppress the progress meter and non-error messages
> -C         forces scp to compresses the data as it is sent to the destination machine.
> -r         Recursively copy entire directories
> -P <port>  Specifies port to connect to on the remote host
> ```
>
> ###### Examples
>
> ```bash
> # copy file basic
> scp file.txt remote_username@10.10.0.2:/remote/directory
> 
> # copy file and use different name
> scp file.txt remote_username@10.10.0.2:/remote/directory/newfilename.txt
> 
> # recursivly copy a directory
> scp -r /local/directory remote_username@10.10.0.2:/remote/directory
> 
> # copy remote file to local 
> scp remote_username@10.10.0.2:/remote/file.txt /local/directory
> ```

## rsync

> ###### Flags
>
> ```bash
> -g, --group       preserve group
> -l, --links       copy symlinks as symlinks
> -n, --dry-run     show what would have been transferred
> -o, --owner       preserve owner (super-user only)
> -p, --perms       preserve permissions
> -r, --recursive   recurse into directories
> -t, --times       preserve times
> -v, --verbose     increase verbosity
> -z, --compress    compress file data during the transfer
> --delete          delete extraneous files from dest dirs
> --devices         preserve device files (super-user only)
> --partial         keep partially transferred files
> --progress        show progress during transfer
> --specials        preserve special files
> 
> -P same as --partial --progress
> -a same as -rlptgoD
> -D same as --devices --specials
> ```
>
> ###### Examples
>
> ```bash
> rsync Origional/* Backup/
> rsync -r Origional/ Backup/
> rsync -a --dry-run Origional/ Backup/
> rsync -av --dry-run Origional/ Backup/
> rsync -av --delete --dry-run Origional/ Backup/
> rsync -azP  ~/Desktop/Origional/ <uesr>@<host-ip-address>:Backup/   # sync from local to remote machine
> rsync -azP  <uesr>@<host-ip-address>:Backup/ ~/Desktop/Origional/   # sync from remote to local machine
> 
> # "https://code.visualstudio.com/docs/remote/troubleshooting#_using-rsync-to-maintain-a-local-copy-of-your-source-code"
> rsync -rlptzv --progress --delete --exclude=.git "user@hostname:/remote/source/code/path" .
> rsync -rlptzv --progress --delete --exclude=.git . "user@hostname:/remote/source/code/path"
> ```

## symlink & unlink

> A symlink (also called a symbolic link) is a type of file in Linux that points to another file or a folder on your computer. 
> Symlinks are <u>similar to shortcuts in Windows</u>.
>
> ###### Flags
>
> ```bash
> -b    create a backup of each existing destination file, he default style (simple) is used
> -h    If the link_name or link_dirname is a symbolic link, do not follow it
> -s, --symbolic    Create a symbolic link.
> -v, --verbose     Cause ln to be verbose, showing files as they are processed
> -f, --force       If the proposed link (link_name) exists, then unlink it so that the link may occur
> -r, --relative	  Create symbolic links relative to link location.
> ```
>
> ###### Add symlink
>
> ```bash
> ln -s <path to the file/folder to be linked> <the path of the link to be created>
> 
> # symlink for a file
> # Any modification to trans.txt will also be reflected in the original file
> ln -s /home/james/transactions.txt trans.txt
> 
> # symlink for a directory
> ln -s /home/james james
> ```
>
> ###### View symlink
>
> ```bash
> ls -l <path-to-assumed-symlink>
> ```
>
> ###### Remove symlink
>
> ```bash
> # remove symlink and keep file
> ln -f <path-to-file> <path-to-symlink>
> 
> # remove symlink and delete file
> unlink <path-to-symlink>
> 
> # remove symlink, origional file and directories are not affected
> rm <path-to-symlink>
> ```
>
> ### Example
>
> ##### Hard Links vs Symbolic(Soft) Links
>
> | Hard Link                                                    | Soft / Symbolic / Sym Link                                   |
> | ------------------------------------------------------------ | ------------------------------------------------------------ |
> | ![file1.txt and file2.txt both linked to the same data](https://www.computerhope.com/unix/images/link-diagram.jpg) | ![file2.txt symlinked to file1.txt](https://www.computerhope.com/unix/images/symlink-diagram.jpg) |
> | links to data of a file                                      | links to another link                                        |
> |                                                              | removing the file (or directory) that a symlink points to breaks the link |
> |                                                              | symbolic links (also called "symlinks" for short) can link to directories. <br />They can cross file system boundaries, <br />so a symbolic link to data on one drive or partition can exist on another drive or partition. |
>
> ###### Create a hard link
>
> ```bash
> echo "This is a file." > file1.txt
> cat file1.txt
>    'This is a file.'
> link file1.txt file2.txt
> cat file1.txt
>    'This is a file.'
> cat file2.txt
>    'This is a file.' 
> echo "It points to data on the disk." >> file1.txt
> cat file1.txt
>    'This is a file.'
>    'It points to data on the disk.'
> cat file2.txt
>    'This is a file.'
>    'It points to data on the disk.'
> # Both files show the change because they share the same data on the disk.
> 
> rm file1.txt
> cat file1.txt
>    'cat: file1.txt: No such file or directory'
> cat file2.txt
>    'This is a file.'
>    'It points to data on the disk.'
> # data stays on the disk even after the "file" (which is actually a link to the data) is removed
> ```
>
> ###### Create a symlink
>
> ```bash
> mkdir documents
> echo "This is a file." > documents/file1.txt
> ln -s documents/ dox
> tree
>    '.                     '
>    '├── documents         '
>    '│   └── file1.txt     '
>    '└── dox -> documents/ ' # can see that dox is linked to documents
> ```

## Kill a Process

> ```bash
> ps -a | grep tenant_functions.sh | grep -v grep | awk '{ print $1 }'
> # >>> '12345'
> 
> kill 12345
> 
> kill $(ps -a | grep tenant_functions.sh | grep -v grep | tail -1 | cut -d " " -f1)
> ps -a | grep tenant_functions.sh | grep -v grep | tail -1 | cut -d " " -f1 | xargs kill
> ```

## Xargs

> ```bash
> ls -1 Desktop/personal
> -> 'code_scratchpad'
> -> 'geneology'
> 
> ls -1 Desktop/personal | xargs                      
> -> 'code_scratchpad geneology'
> 
> ls -1 Desktop/personal | xargs -L 1
> -> 'code_scratchpad'
> -> 'geneology'
> 
> ls -1 Desktop/personal | xargs -n 1
> -> 'code_scratchpad'
> -> 'geneology'
> ```

## Cut

> cut out selected portions of each line of a file
>
> ###### Flags
>
> ```bash
> -b <list>    The list specifies byte positions.
> -c <list>    The list specifies character positions.
> -d <delim>   Use delim as the field delimiter character instead of the tab character.
> -f <list>    The list specifies fields, separated in the input by the field delimiter character. 
>           Output fields are separated by a single occurrence of the field delimiter character.
> ```
>
> ###### Examples
>
> ```bash
> echo Brian Lynch | cut -b 1,2,3                    # -> 'Bri'
> echo Brian Lynch | cut -b 1-3,6-8                  # -> 'Bri Ly'
> echo Brian Lynch | cut -c 4-                       # -> 'an Lynch'
> echo Brian Lynch | cut -c 1,2,3                    # -> 'Bri'
> echo Brian Lynch | cut -c 1-3,6-8                  # -> 'Bri Ly'
> echo Brian Lynch | cut -d " " -f 1                 # -> 'Brian'
> echo Brian Lynch | cut -d " " -f 2                 # -> 'Lynch'
> echo Brian Lynch Software Dev | cut -d " " -f 1-3  # -> 'Brian Lynch Software'
> 
> ```

---

## Links

- [Advanced Bash-Scripting Guide](https://tldp.org/LDP/abs/html/)
- [Baeldung Linux](https://www.baeldung.com/linux/)
