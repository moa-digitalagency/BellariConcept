# Bellari Concept - Guide Utilisateur (Admin)

Ce guide décrit l'utilisation de l'interface d'administration pour la gestion du contenu, des images et des paramètres du site Bellari Concept.

---

## 1. Accès à l'Administration

### Connexion
1.  Accédez à l'URL : `/admin/login`
2.  Saisissez vos identifiants (Email/Nom d'utilisateur et Mot de passe).
    *   *Note :* Le premier compte administrateur est créé lors de l'installation via les variables d'environnement.
3.  Cliquez sur **"Se Connecter"**.

### Tableau de Bord
Une fois connecté, vous arrivez sur le Dashboard qui présente :
*   Un aperçu des **Pages** existantes.
*   Les dernières **Images** téléchargées.
*   Des liens rapides vers les outils de gestion (`Paramètres`, `Déconnexion`).

---

## 2. Gestion des Pages et du Contenu

Le site est structuré en **Pages** (Accueil, À Propos, Services...), elles-mêmes composées de **Sections** (blocs de contenu).

### Modifier une Page
1.  Allez dans le menu **Pages**.
2.  Cliquez sur le bouton **"Éditer"** (icône crayon) à côté de la page souhaitée.
3.  **Métadonnées (SEO) :**
    *   En haut de page, vous pouvez modifier le **Titre** (balise `<title>`) et la **Méta Description**.
    *   Ces champs sont cruciaux pour le référencement Google.
    *   Case à cocher **"Active"** : Décochez pour masquer temporairement la page aux visiteurs (erreur 404).

### Gérer les Sections (Le Cœur du Site)
L'éditeur de page affiche les sections sous forme de liste.
*   **Concept de "Paires" :** Le site étant bilingue (Français/Anglais), chaque bloc de contenu est présenté par paire.
    *   À gauche : La version **FR**.
    *   À droite : La version **EN**.
    *   **Important :** Ces deux blocs fonctionnent ensemble. Ils partagent la même position dans la page.

#### Ajouter une Nouvelle Section
1.  En bas de page, localisez le formulaire **"Ajouter une nouvelle section (FR & EN)"**.
2.  Sélectionnez le **Type de Section** (Hero, Texte, Service, Features, Contact, etc.).
3.  Remplissez le contenu pour le **Français** (Titre, Sous-titre, Contenu).
4.  Remplissez le contenu pour l'**Anglais**.
5.  Cliquez sur **"Créer les Sections"**.
    *   *Le système créera automatiquement les deux versions et les placera à la fin de la page.*

#### Modifier une Section Existante
1.  Repérez le bloc à modifier dans la liste.
2.  Changez les textes, les liens des boutons ou les images.
    *   **Image URL :** Collez le lien d'une image (depuis la bibliothèque d'images).
    *   **Background Image :** (Optionnel) Pour les sections Hero avec image de fond.
3.  Cliquez sur **"Mettre à jour"** pour sauvegarder les changements de *ce bloc spécifique*.

#### Supprimer une Section
1.  Cliquez sur le bouton **"Supprimer"** (rouge) en bas du bloc concerné.
    *   *Attention :* Si vous supprimez la version FR, pensez à supprimer aussi la version EN pour garder la symétrie, ou utilisez l'outil de normalisation (voir section 5).

---

## 3. Gestion des Images (Médiathèque)

### Ajouter une Image
1.  Allez dans le menu **Images**.
2.  Utilisez la zone de **Drag & Drop** ou cliquez pour sélectionner un fichier.
3.  **Formats acceptés :** PNG, JPG, JPEG, WEBP, GIF.
4.  Une fois l'upload terminé, l'image apparaît dans la liste avec son URL.

### Utiliser une Image
1.  Copiez l'**URL** affichée sous l'image (ex: `/static/uploads/a1b2c3d4_photo.jpg`).
2.  Retournez dans l'édition d'une Section.
3.  Collez l'URL dans le champ **"Image URL"** ou **"Background Image"**.

---

## 4. Paramètres du Site & PWA

Le menu **Paramètres** (`/admin/settings`) permet de configurer l'identité du site sans toucher au code.

### Identité Visuelle
*   **Logo du Site :** Changez le logo principal (barre de navigation).
*   **Favicon :** L'icône affichée dans l'onglet du navigateur.
*   **Nom du Site (FR/EN) :** Le nom affiché dans le titre et les métadonnées.

### Réseaux Sociaux
*   Remplissez les champs **Facebook**, **Instagram**, **LinkedIn**.
*   Les icônes apparaîtront automatiquement dans le pied de page (Footer) si l'URL est renseignée.

### Progressive Web App (PWA)
C'est ici que vous transformez le site en "Application Installable" sur mobile.
*   **Activer PWA :** Cochez pour activer la fonctionnalité.
*   **Nom de l'App :** Le nom qui apparaîtra sous l'icône sur l'écran d'accueil du téléphone.
*   **Icône PWA :** L'icône de l'application (format carré recommandé, min 192x192px).
*   **Couleur de Thème :** La couleur de la barre de statut Android/iOS.
*   **Couleur de Fond :** La couleur de l'écran de lancement (Splash Screen).

---

## 5. Dépannage & Maintenance

### Problème de Synchronisation (Sections désordonnées)
Si vous constatez que le texte français ne correspond plus au texte anglais en face (décalage), ou si l'ordre des sections semble cassé :
1.  Allez sur le **Tableau de Bord**.
2.  Cherchez le bouton **"Normaliser les Sections"** (souvent en bas ou dans un menu maintenance).
    *   *Action technique :* Ce bouton lance un script qui réaligne tous les index et force la correspondance entre les versions FR et EN.
3.  Retournez sur la page : l'affichage devrait être corrigé.
