# etyping-py
The RPA tool for e-typing with Python


# Environment 
- ubuntu:20.04
- docker
- docker-compose


# configuration 
- it's needed to create `auth.json` under root directory to login.
```json
{
  "email": "<your email>",
  "passwd": "<password>"
}
```
- optionally, you can edit config.yml for the program.


# Run 
```sh
$ xhsot + \
  && cd env/docker/ \
  && docker-compose up
```


# Stop
```sh
$ docker-compose down
```