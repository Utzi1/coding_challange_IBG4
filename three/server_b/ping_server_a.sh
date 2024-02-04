
# wait a little to assure everything is running
sleep 1s

# ping a single time
ping -c 1 server_a

# check exit-status of ping command
if [ $? -eq 0 ]; then
  echo "Connection to server_A worked "
  echo "Load or reload localhost 3000 ;-)"
else
  echo "Connection to server_A failed"
fi

