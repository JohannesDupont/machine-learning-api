### Code Refactoring model.ipynb

`solutions.ipynb`: enthält refactored code für model training & development
`data`: enthält die CSV files für training und validatiton
`model`: enthält die trainierten models, ist gleichzeitig auch docker volume für den Deployment Container
`test_api.ipynb`: enthält ein beispiel notebook für das abfragen der Model Deployment API

der erste schritt war es, den Code in model.ipynb zu refactoren. Der code war nicht darauf ausgerichtet, in einem professionellen umfeld zu agieren. Dazu ist vor allem logging für erleichterte Fehleranalyse sowie ein OOP ansatz wichtig, damit man den Code besser unit/integration testen kann und mehr übersicht beim weiteren Entwickeln und bugfixen hat. In `solutions.ipynb` findet sich der refactrored code.

Jeder Abschnitt wird nun in eine klasse ausgelagert: 
zunächst werden alle pfade und weitere abhängigkeiten in einer Config Class gepflegt und alle umgebungsvariablen in einer .env datei im dir-root gespeichert. Alle weiteren schritte werden in seperaten klassen verpackt: DataLoader für das datenhändling, Visualiase für alle Datenvisualisierungen etc. 

Dann in einem nächsten Schritt wird die Projekt architektur in Docker aufgesetzt, das heißt das das alle MLOps Schritte in einzelne container ausgelagert werden. Dadurch erhält man mehr kontrolle über den gesamt prozess da nun alle microservices getrennt voneinander laufen. Hier habe ich vor allem zwischen Model Training und Model Development unterschieden. 

Die Dateien `start_jupyterlab.sh` und `start_model_container.sh` starten jeweils einmal einen container zum trainieren und einen container für das model deployment. Die models werden in einem docker volume gespeichert das in der `start_jupyterlab.sh` datei generiert wird, dass sich beide container teilen. Das heißt, dass wenn ein model fertig trainiert und gespeichert wurde es direkt dem deployment container zur verfügung steht und es per api angesprochen werden kann. 

**MLOPS**
Grundsätzlich ist es wichtig, dass das training und das deployment voneinander getrennt sind, aber als microservices miteinander kommunizieren können und sich relevante Volumes, wie beispielsweise das model volume, teilen. Darüberhinaus würde man in einem nächsten Schritt noch eine model training tracking technologie wie beispielsweise MLFlow an den Model Training Container integrieren bzw verknüpfen.
