#!/bin/bash



expect -c "
set timeout 20
spawn sqlite3 db.sqlite
expect \"sqlite>\"
send \".separator ,\n\"
expect \"sqlite>\"
send \".import table.csv positions\n\"
expect \"sqlite>\"
exit 0
"
