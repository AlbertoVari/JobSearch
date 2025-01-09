import urllib.parse
import webbrowser

def create_google_jobs_url(job_title, location):
    # Creiamo il termine di ricerca combinando il ruolo e la posizione
    search_query = f"offerte di lavoro {location} \"{job_title}\""
    
    # Usiamo urllib.parse per costruire correttamente l'URL
    base_url = "https://www.google.com/search?q="
    query = urllib.parse.quote(search_query)  # Codifica la query per l'URL
    
    # Creiamo l'URL finale
    google_jobs_url = base_url + query
    
    return google_jobs_url

# Richiediamo l'input dell'utente per il titolo del lavoro e la località
job_title = input("Inserisci il titolo del lavoro (es. IT Project Manager): ")
location = input("Inserisci la località (es. Emilia Romagna): ")

# Generiamo l'URL con i dati inseriti
url = create_google_jobs_url(job_title, location)

# Stampa il link per la ricerca su Google Jobs
print("Link per la ricerca di lavoro su Google Jobs:", url)

# Apri l'URL nel browser predefinito
webbrowser.open(url)
