U ovom projektu se nalaze video snimci, sljedeće sadržaje:

	Video "ima_oboljenje.mp4" prikazuje kako, na osnovu unosa od strane korisnika u odgovarajuća polja, algoritam Logističke Regresije obrađuje njegov unos i daje potom modal (Bootstrap) poruku gdje kaže da postoje indikacije za potencijalno srčano oboljenje. Potom se korisniku pruža mogućnost da pođe na stranicu gdje bi mogao zakazati pregled kod doktora, kupiti ljekove, kao i da spremi nešto zdravo za jelo, od naših zdravih recepata pogodnih za kardiovaskularno zdravlje, nakon klika na dugme "Reaguj preventivno"

	Video "nema_oboljenje.mp4" prikazuje kako, na osnovu unosa od strane korisnika u odgovarajuća polja, algoritam Logističke Regresije obrađuje njegov unos i daje potom modal (Bootstrap) poruku gdje kaže da ne postoje nikakve indikacije za potencijalno srčano oboljenje. Korisnik može da ode na stranicu, gdje se nalaze doktori, ljekovi i zdravi recepti, ali odlučuje da klikne na dugme "Zatvori" i da se vrati na početnu stranicu.

**NAPOMENA: Ukoliko budete imali problema sa pokretanjem ove aplikacije, uklonite iz originalnog direktorijuma kardiolog snimke "ima_oboljenje.mp4", "nema_oboljenje.mp4" i fajl README.md, pošto se ova aplikacija pokretala bez tih fajlova u originalnom direktorijuma (ovi fajlovi su informativne prirode i nikako ne utiču na krajnji ishod pokretanja aplikacije). U nastavku Vam je dato kako pokrenuti ovu aplikaciju...

--KAKO POKRENUTI OVU APLIKACIJU--

pozicionirati se u direktorijum kardiolog (uveriti se da u njemu ima manage.py) i kucati sljedecu komandu:

>> python manage.py runserver
