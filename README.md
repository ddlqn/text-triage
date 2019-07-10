Triage API
==========

Dieses Projekt implementiert ein einfaches Flask API zur Triage von 
Textanfragen zu Digitec-Produkten basierend auf der Textlänge und der 
Anzahl Käufer des Produkts.

## Verwendung
Das API hat zwei Modi: einen simplen Modus, der eine Klassifizierung anhand 
einer einfachen Regel zu Textlänge und Anzahl Käufer vornimmt, und einen 
Modell-basierten Modus, der ein Machine Learning-Modell benutzt, das mit 
Beispieldaten trainiert wurde. Entsprechend erwartet das API drei Felder:

1. `text_len`: die Länge der Textanfrage
2. `buyers`: die Anzahl Kunden, die das Produkt bereits gekauft haben
3. `type`: der Triage-Modus, der verwendet werden soll (`simple` oder `ml`)

Das API benötigt die Dependencies in `requirements.txt`:

`pip install -r requirements.txt`

Der Server wird dann wie folgt gestartet:

`python api.py linear_regression_model.joblib`

## ML-Modell
Das ML-Modell wird dem API als Parameter übergeben. Die Datei 
`linear_regression_modl.joblib` wird im Jupyter notebook `ml_triage.ipynb` 
trainiert und erstellt. Ich habe mich hier aus Zeitgründen für ein einfaches 
Linear Regression-Modell entschieden, auch wenn es für die Daten wohl nicht 
optimal ist. Das API sollte aber auch ein anderes Modell laden können.

## Beispiel-Anfragen:
`Daniels-MBP:~ daniel$ curl '127.0.0
.1:5000/api/v1/text-triage?text_len=100&buyers=50&type=simple'`  
`1`  
`Daniels-MBP:~ daniel$ curl '127.0.0
.1:5000/api/v1/text-triage?text_len=50&buyers=10&type=simple'`  
`0`  
`Daniels-MBP:~ daniel$ curl '127.0.0
.1:5000/api/v1/text-triage?text_len=51&buyers=10&type=simple'`  
`1`  
`Daniels-MBP:~ daniel$ curl '127.0.0
.1:5000/api/v1/text-triage?text_len=51&buyers=9&type=simple'`  
`0`  

`Daniels-MBP:~ daniel$ curl '127.0.0
.1:5000/api/v1/text-triage?text_len=150&buyers=50&type=ml'`  
`0.577393`  
`Daniels-MBP:~ daniel$ curl '127.0.0
.1:5000/api/v1/text-triage?text_len=40&buyers=8&type=ml'`  
`0.480895`

## Dockerfile
Die Teilaufgabe mit dem Dockerfile habe ich als letztes in Angriff genommen. 
Soweit ich es testen konnte, startet der Flask-Server im Container, jedoch 
habe ich keine Verbindung von aussen herstellen können.