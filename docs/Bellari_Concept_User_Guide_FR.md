![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue) ![Framework](https://img.shields.io/badge/Framework-Flask%203.0-green) ![Database](https://img.shields.io/badge/Database-PostgreSQL-orange) ![Status](https://img.shields.io/badge/Status-Proprietary-red) ![License](https://img.shields.io/badge/License-MOA%20Private-red) ![Owner](https://img.shields.io/badge/Owner-MOA%20Digital%20Agency-purple)

# Bellari Concept - Guide Utilisateur (Admin)

> **DOCUMENT STRICTEMENT CONFIDENTIEL**
>
> Ce guide est destiné aux administrateurs du site Bellari Concept.

Ce guide décrit l'utilisation de l'interface d'administration pour la gestion du contenu, des images et des paramètres du site.

## 1. Accès à l'Administration

### Connexion
1.  Accédez à l'URL : `https://votre-site.com/admin/login`
2.  Saisissez vos identifiants (Nom d'utilisateur et Mot de passe).
3.  Cliquez sur **"Se Connecter"**.

### Tableau de Bord
Une fois connecté, le Dashboard présente :
*   Un aperçu des **Pages** existantes.
*   Les dernières **Images** téléchargées.
*   Des liens rapides vers les outils de gestion (`Paramètres`, `Déconnexion`).

---

## 2. Gestion des Pages et du Contenu

Le site est structuré en **Pages** (Accueil, À Propos...), composées de **Sections** (blocs de contenu).

### Modifier une Page
1.  Allez dans le menu **Pages**.
2.  Cliquez sur le bouton **"Éditer"** (icône crayon) à côté de la page souhaitée.
3.  **Métadonnées (SEO) :**
    *   Modifiez le **Titre** et la **Méta Description** (crucial pour Google).
    *   Case **"Active"** : Décochez pour masquer la page (erreur 404).

### Gérer les Sections (Le Cœur du Site)
L'éditeur affiche les sections par paires bilingues.
*   **Gauche :** Version **FR**.
*   **Droite :** Version **EN**.
*   **Note :** Ces deux blocs fonctionnent ensemble et partagent la même position.

#### Ajouter une Nouvelle Section
1.  En bas de page, trouvez le formulaire **"Ajouter une nouvelle section (FR & EN)"**.
2.  Sélectionnez le **Type de Section** (Hero, Texte, Service, Features, Contact).
3.  Remplissez le contenu pour le **Français** et l'**Anglais**.
4.  Cliquez sur **"Créer les Sections"**.

#### Modifier une Section Existante
1.  Repérez le bloc à modifier.
2.  Changez les textes, liens ou images.
3.  Cliquez sur **"Mettre à jour"** pour sauvegarder *ce bloc spécifique*.

#### Supprimer une Section
1.  Cliquez sur **"Supprimer"** (rouge) en bas du bloc.
    *   *Attention :* Supprimez toujours la version EN si vous supprimez la FR pour garder la symétrie.

---

## 3. Gestion des Images (Médiathèque)

### Ajouter une Image
1.  Allez dans le menu **Images**.
2.  Utilisez la zone de **Drag & Drop** ou cliquez pour sélectionner un fichier (JPG, PNG, WEBP).
3.  L'image apparaît dans la liste avec son URL.

### Utiliser une Image
1.  Copiez l'**URL** affichée sous l'image (ex: `/static/uploads/image.jpg`).
2.  Dans l'éditeur de section, collez l'URL dans le champ **"Image URL"** ou **"Background Image"**.

---

## 4. Paramètres du Site & PWA

Le menu **Paramètres** (`/admin/settings`) permet de configurer l'identité du site.

### Identité Visuelle
*   **Logo / Favicon :** Changez l'image de marque.
*   **Nom du Site (FR/EN) :** Apparaît dans l'onglet du navigateur.

### Progressive Web App (PWA)
Transformez le site en application mobile :
*   **Activer PWA :** Cochez pour activer.
*   **Nom de l'App / Icône / Couleurs :** Personnalisez l'apparence sur le téléphone des clients.

---

## 5. Dépannage

### Problème de Synchronisation
Si le texte français ne correspond plus à l'anglais (décalage) :
1.  Allez sur le **Tableau de Bord**.
2.  Cliquez sur le bouton **"Normaliser les Sections"**.
3.  Ce script réaligne automatiquement tous les contenus.
