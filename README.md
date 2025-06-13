# Όνομα Project

O Pinakas είναι ένα Django project για την εμφάνιση του προγράμματος και των εφημεριών του σχολικού προγράμματος σε οθόνη(ες)

## Λειτουργίες

- Εμφάνιση ημερήσιου προγράμματος
- Πίνακας καθημερινών εφημεριών
- Πίνακας τροποποιήσεων του ημερησίου προγράμματος
- Διαχειρίσιμο μέσω Django admin

## Εγκατάσταση

```bash
git clone https://github.com/koumatzidis/pinakas.git
cd pinakas
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate

pinakas/static/Pinakas_page1.png
pinakas/static/Pinakas_page_2.png

