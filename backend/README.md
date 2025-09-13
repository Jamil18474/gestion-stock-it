# Backend Django

## 🚀 Installation

1. **Se placer dans le dossier backend**
    ```bash
    cd backend
    ```

7. **Lancer le serveur**
    ```bash
    python manage.py runserver
    ```
    Accès admin : [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 🧪 Lancer les tests

```bash
python manage.py test stock
```

---

## Déploiement

L'URL du Backend est accessible sur https://gestion-stock-it-production.up.railway.app/api/

## 📝 Notes

- Pensez à bien configurer les CORS si vous utilisez le frontend séparément.
- Les identifiants de test sont à créer via `createsuperuser`.
