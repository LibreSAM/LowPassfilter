# Tiefpassflter

Dieses Programm entfernt aus einer gegebenen WAV-Datei Frequenzen über einer gegebenen Frequenz und gibt eine WAV-Datei mit dem
modifizierten Signal aus

### Erwartete Eingaben
- Pfad zum Ursprungssignal in einer WAV-Datei
- Cutoff-Frequency
- Pfad zur Ausgabe der modifizierten WAV-Datei

### Ausgabe
- WAV-Datei, die das modifizierte Signal enthält

### Abhängigkeiten

- numpy
- scipy
- math

### Verwendung
1. Pfad zur WAV-Datei angeben
2. Cuttoff-Frequenz angeben
3. Pfad zur Ausgabe des WAV-Files setzen

### Details zur Implementierung

Implementiert wurde ein FIR Window Filter. Hierbei handelt es sich um eine der einfachsten Methoden, 
einen Tiefpassfilter zu implementieren (vgl. https://ccrma.stanford.edu/~jos/sasp/Example_1_Low_Pass_Filtering.html).
