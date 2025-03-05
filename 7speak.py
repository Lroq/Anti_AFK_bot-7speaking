from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL de connexion SSO
sso_url = "https://sso.ynov.com/login?service=https%3A%2F%2Fsso.ynov.com%2Fidp%2Fprofile%2FSAML2%2FCallback%3FentityId%3Dhttps%253A%252F%252Fwww.lms.7speaking.com%252Fynov%252Fsso%252Fmetadata.php%26SAMLRequest%3DPD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48c2FtbHA6QXV0aG5SZXF1ZXN0IHhtbG5zOnNhbWxwPSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6cHJvdG9jb2wiIHhtbG5zOnNhbWw9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDphc3NlcnRpb24iIEFzc2VydGlvbkNvbnN1bWVyU2VydmljZVVSTD0iaHR0cHM6Ly93d3cubG1zLjdzcGVha2luZy5jb20veW5vdi9zc28vaW5kZXgucGhwP2FjcyIgRGVzdGluYXRpb249Imh0dHBzOi8vc3NvLnlub3YuY29tL2lkcC9wcm9maWxlL1NBTUwyL1JlZGlyZWN0L1NTTyIgSUQ9Ik9ORUxPR0lOXzA2YzdiZWNmOGI5Zjc3ZTk3ODAxN2M0YTE2MDBlOTMyM2Y0YWFmOTkiIElzc3VlSW5zdGFudD0iMjAyNS0wMS0yN1QxNTo0ODoxM1oiIFByb3RvY29sQmluZGluZz0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmJpbmRpbmdzOkhUVFAtUE9TVCIgVmVyc2lvbj0iMi4wIj4KICAgIDxzYW1sOklzc3Vlcj5odHRwczovL3d3dy5sbXMuN3NwZWFraW5nLmNvbS95bm92L3Nzby9tZXRhZGF0YS5waHA8L3NhbWw6SXNzdWVyPgogICAgPHNhbWxwOk5hbWVJRFBvbGljeSBBbGxvd0NyZWF0ZT0idHJ1ZSIgRm9ybWF0PSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoxLjE6bmFtZWlkLWZvcm1hdDplbWFpbEFkZHJlc3MiLz4KCjwvc2FtbHA6QXV0aG5SZXF1ZXN0Pg%253D%253D%26RelayState%3Dhttps%253A%252F%252Flms.7speaking.com%252Fynov%252Fsso%252Findex.php"
home_url = "https://user.7speaking.com/home"
courses_url = "https://user.7speaking.com/workshop/news-based-lessons/news-lessons"

# Données de connexion SSO
email = "votre_email@exemple.com"
password = "votre_mot_de_passe"

driver = webdriver.Chrome()

try:
    print("Ouverture de la page de connexion SSO...")
    driver.get(sso_url)

    print("Attente des champs de connexion...")
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    print("Remplissage des champs de connexion...")
    email_field.send_keys(email)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.url_contains("home")
    )
    print("Connexion SSO réussie !")

    print("Navigation vers la page d'accueil...")
    driver.get(home_url)

    print("Navigation vers la page des cours...")
    driver.get(courses_url)

    print("Décocher l'option 'Vidéo'...")
    try:
        video_checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.jss108[type='checkbox']"))
        )
        if video_checkbox.is_selected():
            video_checkbox.click()
            print("Case 'Vidéo' décochée.")
        else:
            print("La case 'Vidéo' est déjà décochée.")
    except Exception as e:
        print(f"Erreur lors de la décoche de la case 'Vidéo' : {e}")

    print("Démarrage de la simulation d'activité...")
    while True:
        time.sleep(180)
        print("Accès à la page d'accueil...")
        driver.get(home_url)
        if "home" in driver.current_url:
            print("Activité simulée : Page d'accueil chargée.")
        else:
            print("Erreur lors du chargement de la page.")

        if time.localtime().tm_min % 10 == 0:
            print("Début des exercices...")
            print("Exercices terminés.")

except KeyboardInterrupt:
    print("Script arrêté par l'utilisateur.")
except Exception as e:
    print(f"Erreur inattendue : {e}")
finally:
    try:
        driver.quit()
        print("Fermeture du navigateur.")
    except Exception:
        print("Le navigateur était déjà fermé.")