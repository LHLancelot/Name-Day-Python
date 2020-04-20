# nameday.py

from datetime import datetime, date 
from time import gmtime, strftime
import datetime

### Leap Year checker ###
dateused = input(" Date in mm dd yyyy format e.g. 19 11 2015 > ")
d = datetime.datetime.strptime(dateused, "%d %m %Y")

def leap_year(year):
    if d.year % 400 == 0:
        return True
    if d.year % 100 == 0:
        return False
    if d.year % 4 == 0:
        return True
    else:
        return False

### Change date to the day of the year ###
yearday = datetime.datetime.strptime(dateused,'%d %m %Y').timetuple().tm_yday

### List of names for non-leap years ###
names_non_leap = (" ", " No names today! ", " Aapeli ", " Elmer, Elmo ", " Ruut ", " Lea, Leea ", " Harri ",
" Aku, Aukusti ", " Hilppa, Titta ", " Veijo, Veikko, Veli ", " Nyyrikki ", " Kari, Karri ",
" Toini ", " Nuutti ", " Sakari, Saku ", " Solja ", " Ilmari, Ilmo ", " Anttoni, Toni ",
" Laura ", " Heikki, Henrik ", " Henna, Henni ", " Aune, Oona ", " Visa ", " Eine, Eini, Enni ",
" Senja ", " Paavo, Pauli ", " Joonatan ", " Viljo ", " Kaarlo, Kalle ", " Valtteri ", " Irja ",
" Alli ", " Riitta ", " Aamu ", " Valo ", " Armi ", " Asser ", " Teija, Terhi, Tiia ", " Rikhard, Riku ",
" Laina ", " Raija, Raisa ", " Elina ", " Talvikki ", " Elma ", " Sulo ", " Voitto ", " Sipi, Sippo ",
" Kai ", " Väinö ", " Kaino ", " Eija ", " Heli, Helinä ", " Keijo ", " Tuuli, Tuulikki ", " Aslak ",
" Matias, Matti ", " Tuija, Tuire ", " Nestori ", " Torsti ", " Onni ", " Alpo ", " Virva, Virve ", 
" Kauko ", " Ari ", " Laila, Leila ", " Tarmo ", " Tarja, Taru ", " Vilppu ", " Auvo ", 
" Aura, Auri, Aurora ", " Kalervo ", " Reijo, Reko ", " Erno, Tarvo ", " Matilda ", " Risto ", 
" Ilkka ", " Kerttu ", " Edvard, Eetu ", " Jooseppi, Juuso ", " Aki, Joakim, Kim ", " Pentti ", 
" Vihtori ", " Akseli ", " Gabriel, Kaapo ", " Aija ", " Immanuel, Manu ", " Sauli ", " Armas ",
" Joni, Joonas, Jouni ", " Usko ", " Irma, Irmeli ", " Pulmu, Raita ", " Pellervo ", " Sampo ",
" Ukko ", " Irene, Irina ", " Vilho, Ville ", " Ahvo, Allan ", " Suoma ", " Elias ", " Tero ",
" Verna ", " Julia, Julius ", " Tellervo ", " Taito ", " Linda, Tuomi ", " Jalo, Patrik ", " Otto ",
" Valdemar, Valto ", " Pälvi, Pilvi ", " Lauha ", " Anselmi, Anssi ", " Alina ", " Jyri, Jyrki, Yrjö ",
" Pertti ", " Markku, Marko, Markus ", " Teresa, Terttu ", " Merja ", " Ilpo, Ilppo ", " Teijo ",
" Miia, Mira, Mirja, Mirva ", " Vappu ", " Viivi, Vuokko ", " Outi ", " Roosa, Ruusu ", " Maini ",
" Ylermi ", " Helmi ", " Heino ", " Timo ", " Aina, Aini, Aino ", " Osmo ", " Lotta ", " Kukka ",
" Tuula ", " Sofia, Sonja ", " Essi, Esteri ", " Maila ", " Eero, Erkki ", " Emilia, Emma ", 
" Karoliina, Lilja ", " Konsta, Kosti ", " Hemminki, Hemmo ", " Lyydia, Lyyli ", " Touko, Tuukka ",
" Urpo ", " Minna, Vilhelmiina ", " Ritva ", " Alma ", " Oiva, Oivi ", " Pasi ", " Helga, Helka ",
" Teemu ", " Venla ", " Orvokki ", " Toivo ", " Sulevi ", " Kustaa, Kyösti ", " Suvi ", " Salomo ",
" Ensio ", " Seppo ", " Impi ", " Esko ", " Raila, Raili ", " Kielo ", " Viena, Vieno ", 
" Päivi, Päivikki ", " Urho ", " Tapio ", " Siiri ", " Into ", " Ahti, Ahto ", " Liina, Paula ",
" Aatto, Aatu ", " Johannes, Juhani ", " Uuno ", " Jarmo, Jorma ", " Elvi, Elviira ", " Leo ",
" Pekka, Petra, Petri, Pietari ", " Päiviö ", " Aaro ", " Maija, Mari, Maria, Meeri ", " Arvo ",
" Ulla, Ulpu ", " Unto ", " Esa ", " Klaus, Launo ", " Turkka, Turo ", " Ilta, Jasmin ", " Saima, Saimi ",
" Elli, Noora ", " Herkko, Hermanni ", " Ilari, Joel, Lari ", " Aliisa ", " Rauna, Rauni ",
" Reino ", " Ossi ", " Riikka ", " Saara, Salla, Salli, Sari ", " Maarit, Marketta, Reeta ",
" Hanna, Johanna ", " Leena ", " Oili ", " Kirsi, Kirsti, Tiina ", " Jaakko ", " Martta ",
" Heidi ", " Atso ", " Olavi, Olli ", " Asta ", " Elena, Helena ", " Maire ", " Kimmo ", 
" Linnea, Nea, Vanamo ", " Veera ", " Salme, Sanelma ", " Keimo, Toimi ", " Lahja ", " Sylvi ",
" Eira, Erja ", " Lauri ", " Sanna, Susanna ", " Klaara ", " Jesse ", " Kanerva, Onerva ", 
" Jaana, Marja, Marjatta ", " Aulis ", " Verneri ", " Leevi ", " Mauno, Maunu ", " Sami, Samuli ",
" Soini, Veini ", " Iivari, Iivo ", " Signe, Varma ", " Perttu ", " Loviisa ", " Ilma, Ilmi ",
" Rauli ", " Tauno ", " Iina, Iines ", " Eemeli, Eemil ", " Arvi ", " Pirkka ", " Sini, Sinikka ",
" Soile, Soili ", " Ansa ", " Mainio ", " Asko ", " Arho ", " Taimi ", " Eevert, Isto ", " Kalevi ",
" Aleksanteri ", " Valma, Vilja ", " Orvo ", " Iida ", " Sirpa ", " Hellevi ", " Aila, Aili ",
" Tytti, Tyyne ", " Reija ", " Varpu, Vaula ", " Mervi ", " Mauri ", " Mielikki ", " Alvar, Auno ",
" Kullervo ", " Kuisma ", " Vesa ", " Arja ", " Mika, Mikael, Mikko ", " Sirja, Sorja ", 
" Raine, Rainer, Rauno ", " Valio ", " Raimo ", " Saija, Saila ", " Inka, Inkeri ", " Minttu, Pinja ",
" Pirjo, Pirkko ", " Hilja ", " Ilona ", " Aleksi ", " Ohto, Otso ", " Aarre, Aarto ", 
" Taija, Taina, Tanja ", " Elsa, Else, Elsi ", " Helvi, Heta ", " Sirkka ", " Saana, Saini ",
" Säde, Satu ", " Uljas ", " Kasperi, Kauno ", " Ursula ", " Anita, Anja ", " Severi ", " Asmo ",
" Sointu ", " Amanda, Niina ", " Hellä, Helli ", " Simo ", " Alfred, Urmas ", " Eila ", " Arto, Artturi ",
" Lyly, Pyry ", " Topi, Topias ", " Terho ", " Hertta ", " Reima ", " Aadolf, Kustaa ", " Taisto ",
" Aatos ", " Teuvo ", " Martti ", " Panu ", " Virpi ", " Ano, Kristian ", " Iiris ", " Janika, Janita ",
" Aarne, Aarno ", " Einari, Eino ", " Tenho ", " Elisabet, Liisa ", " Jalmari, Jari ", " Hilma ",
" Selja, Silja ", " Ismo ", " Lempi ", " Kaija, Kaisa, Katri ", " Sisko ", " Hilkka ", " Heini ",
" Aimo ", " Antero, Antti ", " Oskari ", " Anelma, Unelma ", " Meri, Vellamo ", " Aira, Airi ", 
" Selma ", " Niilo, Niko ", " Sampsa ", " Kyllikki ", " Anna, Anne, Anni ", " Jutta ", " Taneli, Tatu ",
" Tuovi ", " Seija ", " Jouko ", " Heimo ", " Auli, Aulikki ", " Raakel ", " Aapo, Aappo, Rami ",
" Iikka, Iiro ", " Benjamin, Kerkko ", " Tuomas, Tuomo ", " Raafael ", " Senni ", " Aatami, Eeva ", "No names today!",
" No names today! ", " Tapani, Teppo ", " Hannes, Hannu ", " Piia ", " Rauha ", " Daavid, Taavetti "," Sylvester ",)

### List of names for leap years ###
names_leap = (" ", " No names today! ", " Aapeli ", " Elmer, Elmo ", " Ruut ", " Lea, Leea ", " Harri ",
" Aku, Aukusti ", " Hilppa, Titta ", " Veijo, Veikko, Veli ", " Nyyrikki ", " Kari, Karri ",
" Toini ", " Nuutti ", " Sakari, Saku ", " Solja ", " Ilmari, Ilmo ", " Anttoni, Toni ",
" Laura ", " Heikki, Henrik ", " Henna, Henni ", " Aune, Oona ", " Visa ", " Eine, Eini, Enni ",
" Senja ", " Paavo, Pauli ", " Joonatan ", " Viljo ", " Kaarlo, Kalle ", " Valtteri ", " Irja ",
" Alli ", " Riitta ", " Aamu ", " Valo ", " Armi ", " Asser ", " Teija, Terhi, Tiia ", " Rikhard, Riku ",
" Laina ", " Raija, Raisa ", " Elina ", " Talvikki ", " Elma ", " Sulo ", " Voitto ", " Sipi, Sippo ",
" Kai ", " Väinö ", " Kaino ", " Eija ", " Heli, Helinä ", " Keijo ", " Tuuli, Tuulikki ", " Aslak ",
" Matias, Matti ", " Tuija, Tuire ", " Nestori ", " Torsti ", " Onni ", " No names today!", " Alpo ", " Virva, Virve ", 
" Kauko ", " Ari ", " Laila, Leila ", " Tarmo ", " Tarja, Taru ", " Vilppu ", " Auvo ", 
" Aura, Auri, Aurora ", " Kalervo ", " Reijo, Reko ", " Erno, Tarvo ", " Matilda ", " Risto ", 
" Ilkka ", " Kerttu ", " Edvard, Eetu ", " Jooseppi, Juuso ", " Aki, Joakim, Kim ", " Pentti ", 
" Vihtori ", " Akseli ", " Gabriel, Kaapo ", " Aija ", " Immanuel, Manu ", " Sauli ", " Armas ",
" Joni, Joonas, Jouni ", " Usko ", " Irma, Irmeli ", " Pulmu, Raita ", " Pellervo ", " Sampo ",
" Ukko ", " Irene, Irina ", " Vilho, Ville ", " Ahvo, Allan ", " Suoma ", " Elias ", " Tero ",
" Verna ", " Julia, Julius ", " Tellervo ", " Taito ", " Linda, Tuomi ", " Jalo, Patrik ", " Otto ",
" Valdemar, Valto ", " Pälvi, Pilvi ", " Lauha ", " Anselmi, Anssi ", " Alina ", " Jyri, Jyrki, Yrjö ",
" Pertti ", " Markku, Marko, Markus ", " Teresa, Terttu ", " Merja ", " Ilpo, Ilppo ", " Teijo ",
" Miia, Mira, Mirja, Mirva ", " Vappu ", " Viivi, Vuokko ", " Outi ", " Roosa, Ruusu ", " Maini ",
" Ylermi ", " Helmi ", " Heino ", " Timo ", " Aina, Aini, Aino ", " Osmo ", " Lotta ", " Kukka ",
" Tuula ", " Sofia, Sonja ", " Essi, Esteri ", " Maila ", " Eero, Erkki ", " Emilia, Emma ", 
" Karoliina, Lilja ", " Konsta, Kosti ", " Hemminki, Hemmo ", " Lyydia, Lyyli ", " Touko, Tuukka ",
" Urpo ", " Minna, Vilhelmiina ", " Ritva ", " Alma ", " Oiva, Oivi ", " Pasi ", " Helga, Helka ",
" Teemu ", " Venla ", " Orvokki ", " Toivo ", " Sulevi ", " Kustaa, Kyösti ", " Suvi ", " Salomo ",
" Ensio ", " Seppo ", " Impi ", " Esko ", " Raila, Raili ", " Kielo ", " Viena, Vieno ", 
" Päivi, Päivikki ", " Urho ", " Tapio ", " Siiri ", " Into ", " Ahti, Ahto ", " Liina, Paula ",
" Aatto, Aatu ", " Johannes, Juhani ", " Uuno ", " Jarmo, Jorma ", " Elvi, Elviira ", " Leo ",
" Pekka, Petra, Petri, Pietari ", " Päiviö ", " Aaro ", " Maija, Mari, Maria, Meeri ", " Arvo ",
" Ulla, Ulpu ", " Unto ", " Esa ", " Klaus, Launo ", " Turkka, Turo ", " Ilta, Jasmin ", " Saima, Saimi ",
" Elli, Noora ", " Herkko, Hermanni ", " Ilari, Joel, Lari ", " Aliisa ", " Rauna, Rauni ",
" Reino ", " Ossi ", " Riikka ", " Saara, Salla, Salli, Sari ", " Maarit, Marketta, Reeta ",
" Hanna, Johanna ", " Leena ", " Oili ", " Kirsi, Kirsti, Tiina ", " Jaakko ", " Martta ",
" Heidi ", " Atso ", " Olavi, Olli ", " Asta ", " Elena, Helena ", " Maire ", " Kimmo ", 
" Linnea, Nea, Vanamo ", " Veera ", " Salme, Sanelma ", " Keimo, Toimi ", " Lahja ", " Sylvi ",
" Eira, Erja ", " Lauri ", " Sanna, Susanna ", " Klaara ", " Jesse ", " Kanerva, Onerva ", 
" Jaana, Marja, Marjatta ", " Aulis ", " Verneri ", " Leevi ", " Mauno, Maunu ", " Sami, Samuli ",
" Soini, Veini ", " Iivari, Iivo ", " Signe, Varma ", " Perttu ", " Loviisa ", " Ilma, Ilmi ",
" Rauli ", " Tauno ", " Iina, Iines ", " Eemeli, Eemil ", " Arvi ", " Pirkka ", " Sini, Sinikka ",
" Soile, Soili ", " Ansa ", " Mainio ", " Asko ", " Arho ", " Taimi ", " Eevert, Isto ", " Kalevi ",
" Aleksanteri ", " Valma, Vilja ", " Orvo ", " Iida ", " Sirpa ", " Hellevi ", " Aila, Aili ",
" Tytti, Tyyne ", " Reija ", " Varpu, Vaula ", " Mervi ", " Mauri ", " Mielikki ", " Alvar, Auno ",
" Kullervo ", " Kuisma ", " Vesa ", " Arja ", " Mika, Mikael, Mikko ", " Sirja, Sorja ", 
" Raine, Rainer, Rauno ", " Valio ", " Raimo ", " Saija, Saila ", " Inka, Inkeri ", " Minttu, Pinja ",
" Pirjo, Pirkko ", " Hilja ", " Ilona ", " Aleksi ", " Ohto, Otso ", " Aarre, Aarto ", 
" Taija, Taina, Tanja ", " Elsa, Else, Elsi ", " Helvi, Heta ", " Sirkka ", " Saana, Saini ",
" Säde, Satu ", " Uljas ", " Kasperi, Kauno ", " Ursula ", " Anita, Anja ", " Severi ", " Asmo ",
" Sointu ", " Amanda, Niina ", " Hellä, Helli ", " Simo ", " Alfred, Urmas ", " Eila ", " Arto, Artturi ",
" Lyly, Pyry ", " Topi, Topias ", " Terho ", " Hertta ", " Reima ", " Aadolf, Kustaa ", " Taisto ",
" Aatos ", " Teuvo ", " Martti ", " Panu ", " Virpi ", " Ano, Kristian ", " Iiris ", " Janika, Janita ",
" Aarne, Aarno ", " Einari, Eino ", " Tenho ", " Elisabet, Liisa ", " Jalmari, Jari ", " Hilma ",
" Selja, Silja ", " Ismo ", " Lempi ", " Kaija, Kaisa, Katri ", " Sisko ", " Hilkka ", " Heini ",
" Aimo ", " Antero, Antti ", " Oskari ", " Anelma, Unelma ", " Meri, Vellamo ", " Aira, Airi ", 
" Selma ", " Niilo, Niko ", " Sampsa ", " Kyllikki ", " Anna, Anne, Anni ", " Jutta ", " Taneli, Tatu ",
" Tuovi ", " Seija ", " Jouko ", " Heimo ", " Auli, Aulikki ", " Raakel ", " Aapo, Aappo, Rami ",
" Iikka, Iiro ", " Benjamin, Kerkko ", " Tuomas, Tuomo ", " Raafael ", " Senni ", " Aatami, Eeva ",
" No names today! ", " Tapani, Teppo ", " Hannes, Hannu ", " Piia ", " Rauha ", " Daavid, Taavetti ", " Sylvester ",)

def nameday():
    if leap_year:
        print("Day", yearday, ":", names_leap[yearday]) 
    else:
        print("Day", yearday, ":", names_non_leap[yearday])

nameday()
