# CloudComputingProject

## Get startet with ansible

1. Download the subfolder **Automatisierung** under [this link](https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/as14df/CloudComputingProject/tree/master/Automatisierung) and unzip it on your local machine

2. Open the file **hosts** and paste the ip adress of your compute engine after **[ServerGruppe]** then save the file

3. Open terminal in this folder and type in it: **ansible-playbook getcurl.yml** (ansible has to be installed)

4. Wait until ansible finished installation and startet the server then close the terminal

5. Youre done, just open your browser and type in: **<IP_ADRESS>:80/speaker**

// Make sure that in your compute engines settings "Zugriffsbereiche für Cloud API" 
is set to "Uneingeschränkten Zugriff auf alle Cloud-APIs zulassen"


## Get startet manually:

1. Install Virtualenv and initiate an environment on the compute engine, if you have not done this yet 

2. Start the environment by typing **source env/bin/activate** in terminal 

3. Install **Python3, pip3, Gcloud SDK, Google Translate API** and **Django** in it

4. Clone this Project into your environment104.197.226.168

6. Go to **~/CloudComputing/CloudComputingProject/Translator/translate** and type in terminal:
  * **python3 manage.py migrate** # migrate database
  * **python3 manage.py runserver 0.0.0.0:80** # start server

7. Youre done, just open your browser and type in: **<IP_ADRESS>:80/speaker**

   
   

