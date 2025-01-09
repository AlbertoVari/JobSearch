from google.cloud import talent
import os

# Impostare il percorso del file di credenziali
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/../xxx.json"

def search_jobs(project_id):
    """Search jobs for 'IT Project Manager' in 'Bologna'"""
    
    # Crea un client per interagire con l'API Talent
    client = talent.JobServiceClient()

    # Crea la query di ricerca con il titolo
    job_query = talent.JobQuery(
        query="IT Project Manager",  # Ruolo da cercare
        location_filters=[talent.LocationFilter(address="Bologna")]
    )

    # Costruisci il parent path (progetto Google Cloud)
    parent = f"projects/{project_id}"

    try:
        # Esegui la ricerca dei lavori
        request = talent.SearchJobsRequest(
            parent=parent,  # Passa il parent nella richiesta
            job_query=job_query  # Passa la job query
        )
        
        response = client.search_jobs(request=request)
        print(response)
        # Stampa i risultati
        if response.matching_jobs:
            print("Lavori trovati:")
            for job in response.matching_jobs:
                print(f"Job title: {job.title}")
                print(f"Company name: {job.company}")
                print(f"Location: {job.locations}")
                print(f"Job Description: {job.description}")
                print("----------------------------")
        else:
            print("Nessun lavoro trovato per la ricerca.")

    except Exception as e:
        print(f"Errore durante la ricerca dei lavori: {e}")

# Esegui la funzione con il tuo project_id
project_id = "..."  # Sostituisci con il tuo project_id di Google Cloud
search_jobs(project_id)
