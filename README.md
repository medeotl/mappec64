# mappec64

Il programma serve a creare mappe partendo da screenshot di giochi per c64 con flip-screen presi tramite emulatore.

Gli screenshot:
- vanno posti in `./screenshot`
- devo essere file bmp
- il nome del file deve essere del tipo `x.y.bmp`, dove x e y sono le coordinate (anche negative) dello screenshot preso, considerando che la prima schermata di gioco ha posizione (0,0)

Il programma si occupa di rimuovere la cornice del gioco, spostando i file in `./screenshot/cropped`. Qui vengono poi elaborati creando il file `mappa.bmp` posto nella directory principale del programma