
sleep 1s

ping -c 1 db

if [ $? -eq 0 ]; then
  echo "Connection to the database is successful"
else
  echo "Connection to the database failed"
fi

