# ba-website

This is everything that was used for my bachelors thesis. 
Here you will find all the source code, config files and scripts used to create it.
If you don't have my thesis in front of you and just want to check how or why I did things the way I did, you should not look into this repository.
All code was made for one purpose only, nothing is tested and nothing was build with security in mind.
It all for use in a controlled environment, protected by a firewall. 
If you don't know what you are doing, you should not copy any code or config from this repo because it would be unsafe to use in production.
And if you know what you are doing, then why would you need my code, you already know how to do it better!

If you have my thesis in front of you and want to check how or why I did the things I did, you will find everything needed in this repository.
I tried to document everything needed to set it the project up, although it was not relevant for my thesis. 
If you have any questions, feel free to get in touch with me, I will try my best to help you.


### To install env

poetry shell
poetry install

### For local start of backend-server

docker-compose up -d ba-postgres adminer
cd ba_website
export DBDATABASE=ba-db
export DBHOST=127.0.0.1
export DBPASSWORD=1234
export DBPORT=5432
export DBUSER=ba-user
export DEBUG_DEPLOYMENT=True
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 127.0.0.1:1337

In one command:

docker-compose up -d ba-postgres adminer && cd ba_website && export DBDATABASE=ba-db && export DBHOST=127.0.0.1 && export DBPASSWORD=1234 && export DBPORT=5432 && export DBUSER=ba-user && python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0:1337

### For local start of frontend-server
cd ba_frontend
yarn install
export VUE_APP_BACKEND=127.0.0.1:1337/api
yarn serve

### Start virtual machines

To start virtual machines you need vagrant.
You also need some plugins

```
vagrant plugin install vagrant_reboot_linux
```

Edit the vagrantfile and set static IPs for the interfaces which work on yout network and have access to the internet. 
You can also use DHCP for it, see vagrant documentation for that.

To start one VM for every service (frontend, backend, db), use:
vagrant up '/multi.*/'

To start one VM with everything in it, use:
vagrant up '/single_vm.*/'

Right now, online the single VMs are supported and ready to use!

To stop VMs use:
vagrant halt

To remove all VMs use:
vagrant destroy --force

### Classic deployment
Start vm:
```
vagrant up single_vm_classic
```

Open ssh session in vm
```
vagrant ssh single_vm_classic
```

Go into project folder

```
cd /vagrant
```


run postgres init
```
./postgres/init.sh
```

Go into backend folder
```
cd ba_website
```

Run prepare script
```
./prepare_classic.sh
```

A new terminal will be spawned. In that terminal, run the start script.
```
./run_classic.sh
```

Your backend is now running.

Now go into the frontend folder ba_frontend.
Run
```
./run_classic.sh
```

Now the server is available under ip:1337

## Docker deployment

Start VM

```
vagrant up single_vm_docker
```

Go to vagrant folder
```
cd /vagrant
```

Then do:

```
docker-compose -f docker-compose_registry.yml up
```


## k3s deployment

Start VM

```
vagrant up single_vm_orchestration
```

Go to k3s folder
```
cd /vagrant/k3s
```

Then do:

```
sudo kubectl apply -f .
```

## Tests

To run the performance tests go to the performance_test edit the run_tests.py file.
The hosts array has to meet your environment.

Then run:
```
python run_tests.py
```

Then you have to wait a long time. Your test files will be sorted in the test_results folder.

## Create graphs

You will find some files inside the pyplot_files folder inside the performance_tests folder. 
Depending on your results you have to manually edit the files to get nice looking results.
You can start all tests with:
```
python analyze_data.py timestamp filetype
```
So e.g.:
```
python analyze_data.py 2020-08-13T00:58:04 png
```
This command will anayze the data and create graphs and json files with some results.