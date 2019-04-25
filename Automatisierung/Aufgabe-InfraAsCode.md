
# Aufgabe zu Infrastructure as Code

- Erstellen Sie eine Ubuntu VM in der Cloud und starten diese 
  Tragen Sie beim Erstellen Ihren Public Key ein, und testen das über einen ssh Login  
  Ist Ihnen klar wozu die Host-key Checking Abfrage dient? 
  Lassen Sie sich die Instanz anzeigen (console oder im Terminal mit "gcloud") und notieren Sie die IP Adresse  

- Vorbereitung zum Arbeiten mit Ansible 

  Im aktuellen Verzeichnis ist eine Vorlage für ein [hosts file](./hosts) und ein [Konfigurations-File](./ansible.cfg) 
  + Passen Sie das Konfigurationsfile an: 
    Einige wichtige Einstellungen sind mit "HILFREICH" markiert (suchen mit Ctrl+f)
    * Schalten Sie das hosts key checking ab 
    * Tragen Sie den Pfad zum Inventory ein 
    * Aktivieren Sie keep_remote_files

- Loslegen mit ansible! Ganz Unten finden Sie einige wichtige Kommandozeilen-Optionen zu ansible / ansible-playbook

- Ansible im AdHoc Modus nutzen

  Starten Sie ansible im AdHoc Modus und führen den Befehl "df -h /" aus, um sich den Plattenplatz der Cloud VM anzeigen zu lassen

  Sie brauchen dazu das Inventory File, indem die IP der Cloud-VM eingetragen wird  
  Sie müssen ansible.cfg anpassen  
  + Pfad zum inventory File eintragen
  + Das Host Key Checking für ssh abschalten

  Lesen Sie sich die [Beschreibung des Shell Moduls](https://docs.ansible.com/ansible/latest/modules/shell_module.html) durch  
  Rufen Sie ansible im AdHoc Modus mit dem Shell modul auf und übergeben den Befehl zum Anzeigen des Plattenplatzes

- Ansible mit Playbooks nutzen  
  Schreiben Sie ein Playbook, welches das Tool tree auf dem Cloud-VM installiert, anschliessend das Verzeichnis /home/ansible/projekt anlegt und dann lokale Datei ihrer Wahl in dieses Verzeichnis kopiert
  Tipp:  
  + Zur Installation benötigen Sie sudo Rechte, also müssen SIe mit Ansible die Direktive "become" nutzen
  + Machen Sie ein update vom Paket-Manager Cache vor der Installation 
  + Sie können für alle Aktionen Module von ansible nutzen. Fürs Verzeichnis anlegen und kopieren
    aus [dieser Liste](https://docs.ansible.com/ansible/latest/modules/list_of_files_modules.html) und fürs installieren aus [dieser](https://docs.ansible.com/ansible/latest/modules/list_of_packaging_modules.html)    

- **Bewertete Aufgabe: Schreiben Sie ein Playbook, dass Ihr Projekt auf der Cloud-VM installiert und startet, so dass die App von außen erreichbar ist**  
  Dazu gehören folgende Aufgaben 
  + Code auf die Maschine bringen 
  + Django installieren 
  + Abhängigkeiten installieren 
  + Starten Sie die App
  + Testen Sie die App

  + Bonus: Starten der VM mit ansible, Konfigurieren der Firewall, so dass der Port von außen zugelassen ist
    Hierzu brauchen Sie einen zweiten "Play" im Playbook, weil ansible hier das gcloud tool auf localhost nutzen soll 
  + Extra Bonus: Nutzung eines Apache-Webserver mit wsgi anstatt von "runserver"

  Einige Tipps: 
  + Sie sollten ansible **auf der Cloud VM** mit Python 3 nutzen. [Infos hier](https://docs.ansible.com/ansible/latest/reference_appendices/python_3_support.html)
    * Einstellung: ansible\_python\_interpreter=/usr/bin/python3 für die Cloud-VM
  + Sie können Ihre SW durch kopieren und auspacken eines Tar Files oder durch Git Clone installieren. Bei Git Clone werden aber auf der Cloud VM die keys für git benötigt. Das ist etwas komplizierter, aber professioneller
  + Zum Start der App können Sie mit den bei Python eingebauten Server nutzen

- Commandline Options zu ansible / ansible-playbook
    
  Die folgenden Optionen können miteinander kombiniert werden 

  ansible -i hosts  # Angabe des Inventory Files auf der Kommandozeile  
  ansible -v        # verbose mode: zeigt benutztes config-file an  
  ansible -vvv      # .. zeigt zusätzlich benutztes inventory an  