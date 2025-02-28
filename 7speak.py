from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# URL de connexion SSO
sso_url = "https://sso.ynov.com/login?service=https%3A%2F%2Fsso.ynov.com%2Fidp%2Fprofile%2FSAML2%2FCallback%3FentityId%3Dhttps%253A%252F%252Fwww.lms.7speaking.com%252Fynov%252Fsso%252Fmetadata.php%26SAMLRequest%3DPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48c2FtbHA6QXV0aG5SZXF1ZXN0IHhtbG5zOnNhbWxwPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6cHJvdG9jb2wiIHhtbG5zOnNhbWw9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDphc3NlcnRpb24iIEFzc2VydGlvbkNvbnN1bWVyU2VydmljZVVSTD0iaHR0cHM6Ly93d3cubG1zLjdzcGVha2luZy5jb20veW5vdi9zc28vaW5kZXgucGhwP2FjcyIgRGVzdGluYXRpb249Imh0dHBzOi8vc3NvLnlub3YuY29tL2lkcC9wcm9maWxlL1NBTUwyL1JlZGlyZWN0L1NTTyIgSUQ9Ik9ORUxPR0lOXzA2YzdiZWNmOGI5Zjc3ZTk3ODAxN2M0YTE2MDBlOTMyM2Y0YWFmOTkiIElzc3VlSW5zdGFudD0iMjAyNS0wMS0yN1QxNTo0ODoxM1oiIFByb3RvY29sQmluZGluZz0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmJpbmRpbmdzOkhUVFAtUE9TVCIgVmVyc2lvbj0iMi4wIj4KICAgIDxzYW1sOklzc3Vlcj5odHRwczovL3d3dy5sbXMuN3NwZWFraW5nLmNvbS95bm92L3Nzby9tZXRhZGF0YS5waHA8L3NhbWw6SXNzdWVyPgogICAgPHNhbWxwOk5hbWVJRFBvbGljeSBBbGxvd0NyZWF0ZT0idHJ1ZSIgRm9ybWF0PSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoxLjE6bmFtZWlkLWZvcm1hdDplbWFpbEFkZHJlc3MiLz4KCjwvc2FtbHA6QXV0aG5SZXF1ZXN0Pg%253D%253D%26RelayState%3Dhttps%253A%252F%252Flms.7speaking.com%252Fynov%252Fsso%252Findex.php"
home_url = "https://user.7speaking.com/home"
courses_url = "https://user.7speaking.com/workshop/news-based-lessons/news-lessons"

# Données de connexion SSO
email = "<Enter your mail>"
password = "<Enter your password>"

# Initialiser le navigateur
driver = webdriver.Chrome()  # Assurez-vous que chromedriver est dans votre PATH

try:
    # Ouvrir la page de connexion SSO
    print("Ouverture de la page de connexion SSO...")
    driver.get(sso_url)
    time.sleep(2)  # Attendre que la page se charge

    # Remplir les champs de connexion
    print("Remplissage des champs de connexion...")
    email_field = driver.find_element(By.NAME, "username")
    email_field.send_keys(email)
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(2)  # Attendre que la connexion se fasse

    # Vérifier si la connexion a réussi
    if "home" in driver.current_url:
        print("Connexion SSO réussie !")
    else:
        print("Échec de la connexion SSO.")
        exit()

    # Naviguer vers la page d'accueil
    print("Navigation vers la page d'accueil...")
    driver.get(home_url)
    time.sleep(2)  # Attendre que la page se charge

    # Naviguer vers la page des cours
    print("Navigation vers la page des cours...")
    driver.get(courses_url)
    time.sleep(1)

    # Décocher l'option "Vidéo"
    print("Décocher l'option 'Vidéo'...")
    try:
        # Localiser la case à cocher "Vidéo"
        video_checkbox = driver.find_element(By.CSS_SELECTOR, "input.jss108[type='checkbox']")

        # Vérifier si la case est déjà cochée
        if video_checkbox.is_selected():
            print("La case 'Vidéo' est cochée. On la décoche...")
            video_checkbox.click()  # Décocher la case
            time.sleep(1)  # Attendre que l'action soit prise en compte
            print("Case 'Vidéo' décochée.")
        else:
            print("La case 'Vidéo' est déjà décochée.")
    except Exception as e:
        print(f"Erreur lors de la décoche de la case 'Vidéo' : {e}")

    # Cliquer sur le bouton "Rechercher"
    try:
        search_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")  # Ajustez le sélecteur selon votre besoin
        search_button.click()
        print("Bouton 'Rechercher' cliqué.")
        time.sleep(5)  # Attendre que l'action soit prise en compte
    except Exception as e:
        print(f"Erreur lors du clic sur le bouton 'Rechercher' : {e}")

    # Trouver et cliquer sur tous les boutons "Study"
    # try:
    #     study_button = driver.find_element(By.CSS_SELECTOR, "button[type='study']")
    #     study_button.click()
    #     print("Bouton 'study' cliqué.")
    #     time.sleep(10)  # Attendre que l'action soit prise en compte
    # except Exception as e:
    #     print(f"Erreur lors du clic sur le bouton 'study' : {e}")
        
        
    driver.get(home_url)   
    # Simuler une activité en accédant à la page d'accueil toutes les 5 minutes
    print("Démarrage de la simulation d'activité...")
    while True:
        time.sleep(180)  # Attendre 5 minutes
        print("Accès à la page d'accueil...")
        driver.get(home_url)
        if "home" in driver.current_url:
            print("Activité simulée : Page d'accueil chargée.")
        else:
            print("Erreur lors du chargement de la page.")

        # Faire des exercices de temps en temps
        if time.localtime().tm_min % 10 == 0:  # Toutes les 10 minutes
            print("Début des exercices...")
            # Ajoutez ici le code pour interagir avec les exercices
            print("Exercices terminés.")

except KeyboardInterrupt:
    print("Script arrêté.")
finally:
    driver.quit()