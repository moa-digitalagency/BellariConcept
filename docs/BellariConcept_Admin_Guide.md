[ 🇫🇷 Français ] | [ 🇬🇧 English ](BellariConcept_Admin_Guide_en.md)

# 📖 Bellari Concept - Guide Administrateur
**Date :** 2025
**Auteur :** Aisance KALONJI (MOA Digital Agency)
**Usage :** Interne & Client Final

Ce guide explique comment utiliser le panneau d'administration pour gérer le contenu, les médias et la configuration du site.

---

## 1. Accès et Connexion

L'interface d'administration est sécurisée et accessible uniquement via authentification.

*   **URL :** `/admin` (ou `/admin/login`)
*   **Identifiants :** Définis lors de l'installation (ou via les variables d'environnement `ADMIN_USERNAME` / `ADMIN_PASSWORD`).

> **Note de Sécurité :** Après 3 tentatives infructueuses, l'accès peut être temporairement limité selon la configuration du serveur (Fail2Ban recommandé en production).

---

## 2. Tableau de Bord (Dashboard)

La page d'accueil de l'admin (`/admin`) offre une vue d'ensemble :
*   **Pages Actives :** Liste rapide des pages du site.
*   **Dernières Images :** Aperçu des fichiers récemment téléversés.
*   **Actions Rapides :** Liens vers les paramètres et la médiathèque.
*   **Outils :** Lien "Normaliser les Sections" pour corriger les désynchronisations FR/EN.

---

## 3. Gestion du Contenu (Pages & Sections)

### 3.1 Éditer une Page
Cliquez sur une page (ex: "Home") pour entrer dans l'éditeur.
*   **Paramètres SEO :** Modifiez le `Titre` (Balise Title) et la `Méta Description` (Apparaît dans Google).
*   **Statut :** Cochez/Décochez "Active" pour publier ou masquer la page.

### 3.2 Gérer les Sections (Le "Builder")
Le contenu est divisé en blocs appelés "Sections". Chaque section existe en paire (Français / Anglais).

*   **Ajouter une Section :**
    1.  Allez en bas de page "Ajouter une nouvelle section".
    2.  Choisissez le **Type** (Hero, Features, Text, Contact...).
    3.  Remplissez le contenu pour le FR et l'EN simultanément (recommandé via "Create Both").
*   **Modifier une Section :**
    *   Modifiez le texte, les liens des boutons, ou l'image de fond.
    *   **Image de fond :** Copiez l'URL d'une image depuis la Médiathèque et collez-la dans le champ `Background Image`.
*   **Réordonner :** Modifiez le numéro `Ordre` et sauvegardez. (Astuce : Utilisez l'outil "Normaliser" après de gros changements).

---

## 4. Médiathèque (Images)

Accessible via le menu "Images".

*   **Upload :** Glissez-déposez ou sélectionnez des fichiers (.jpg, .png, .webp).
*   **Optimisation :** Le système renomme automatiquement les fichiers pour la sécurité.
*   **Utilisation :**
    1.  Copiez l'URL de l'image (bouton "Copier le lien").
    2.  Collez cette URL dans les champs `Image URL` ou `Background Image` de vos sections.

---

## 5. Paramètres du Site & PWA

Accessible via le menu "Paramètres".

### 5.1 Identité Visuelle
*   **Logo du Site :** Changez le logo principal (Format PNG/SVG recommandé).
*   **Favicon :** L'icône dans l'onglet du navigateur.

### 5.2 Progressive Web App (PWA)
Configurez l'apparence de l'application lorsqu'elle est installée sur mobile.
*   **Activer PWA :** Active/Désactive le manifest.
*   **Nom de l'App :** Le nom sous l'icône sur l'écran d'accueil du téléphone.
*   **Thème :** Couleur de la barre d'état (Hexadécimal).
*   **Icône PWA :** Doit être une image carrée (512x512 recommandé).

### 5.3 Réseaux Sociaux
Remplissez les liens vers vos profils (Facebook, Instagram, LinkedIn). Ils apparaîtront automatiquement dans le pied de page (Footer).

---
© MOA Digital Agency (myoneart.com) - Auteur : Aisance KALONJI
