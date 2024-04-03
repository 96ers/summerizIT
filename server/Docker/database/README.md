  

## Run Docker to connect to database Mysql

Build images and run

~~~bash  
  sudo docker-compose up -d 
~~~

Check if the image is active  

~~~bash  
  sudo docker ps
~~~

Turn off images  

~~~bash  
  sudo docker-compose down
~~~

Go to the phpmyadmin page  

~~~bash  
sensible-browser 'http://localhost:<your-phpmyadmin-port>/'
~~~

To run this docker-compose, you will need to add the following environment variables to your .env file  
`MYSQL_DATABASE`

`MYSQL_USER`

`MYSQL_PASSWORD`

`MYSQL_ROOT_PASSWORD`

`MYSQL_INTERNAL_PORT`

`MYSQL_PUBLIC_PORT`

`PMA_HOST`

`PMA_PORT` = `MYSQL_INTERNAL_PORT`

`PMA_INTERNAL_PORT`

`PMA_PUBLIC_PORT`  

`ANOTHER_API_KEY` 


## License  

[MIT](https://choosealicense.com/licenses/mit/)
