# mappec64

Il programma serve a creare mappe partendo da screenshot di giochi per c64 con flip-screen presi tramite emulatore.

Gli screenshot:

- vanno posti in `./screenshots`
- la directory `./screenshots` deve contenere una sottodirectory `./cropped`
- devono essere file bmp
- il nome del file deve essere del tipo `x.y.bmp`, dove x e y sono le coordinate (anche negative) dello screenshot preso, considerando che la prima schermata di gioco ha posizione (0,0), quindi il relativo screenshot si chiamerà 0.0.bmp

Il programma si occupa di rimuovere la cornice del gioco, spostando i file in `./screenshot/cropped`. Qui vengono poi elaborati creando il file `mappa.bmp` posto nella directory principale del programma

N.B. Aggiustare l'area da rimuovere in base al gioco che state mappando
