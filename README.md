U prilogu se nalazi zip folder koji se zove "snimci rada nase aplikacije.zip", koji je upload-ovan zajedno sa originalnim projektom "kardiolog".

U njemu se nalaze video snimci, koji posjeduju sljedeće sadržaje:

	Video "aplikacija.mp4" predstavlja cjelokupni rad naše aplikacije, izgled njenog interfejsa, kako reaguju na pritiske određenih dugmadi, prikazuje autorska upozorenja ako se forma ne popuni kako treba (ako posjeduje prazna polja) itd.

	Video "ima_oboljenje.mp4" prikazuje kako, na osnovu unosa od strane korisnika u odgovarajuća polja, algoritam Logističke Regresije obrađuje njegov unos i daje potom modal (Bootstrap) poruku gdje kaže da postoje indikacije za potencijalno srčano oboljenje. Potom se korisniku pruža mogućnost da pođe na stranicu gdje bi mogao zakazati pregled kod doktora, kupiti ljekove, kao i da spremi nešto zdravo za jelo, od naših zdravih recepata pogodnih za kardiovaskularno zdravlje, nakon klika na dugme "Reaguj preventivno"

	Video "nema_oboljenje.mp4" prikazuje kako, na osnovu unosa od strane korisnika u odgovarajuća polja, algoritam Logističke Regresije obrađuje njegov unos i daje potom modal (Bootstrap) poruku gdje kaže da ne postoje nikakve indikacije za potencijalno srčano oboljenje. Korisnik može da ode na stranicu, gdje se nalaze doktori, ljekovi i zdravi recepti, ali odlučuje da klikne na dugme "Zatvori" i da se vrati na početnu stranicu.

--KAKO POKRENUTI OVU APLIKACIJU--

pozicionirati se u direktorijum kardiolog (uveriti se da u njemu ima manage.py) i kucati sljedecu komandu:

>> python manage.py runserver
