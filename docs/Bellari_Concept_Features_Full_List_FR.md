![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue) ![Framework](https://img.shields.io/badge/Framework-Flask%203.0-green) ![Database](https://img.shields.io/badge/Database-PostgreSQL-orange) ![Status](https://img.shields.io/badge/Status-Proprietary-red) ![License](https://img.shields.io/badge/License-MOA%20Private-red) ![Owner](https://img.shields.io/badge/Owner-MOA%20Digital%20Agency-purple)

# Bellari Concept - Liste Complète des Fonctionnalités

> **DOCUMENT STRICTEMENT CONFIDENTIEL**
>
> Ce document est la propriété exclusive de **MOA Digital Agency**.

Ce document recense l'ensemble des fonctionnalités techniques et métier de la plateforme Bellari Concept.

## 1. Gestion de Contenu (CMS Bilingue)

Le cœur du système est un CMS sur-mesure permettant une gestion fine du contenu en Français et en Anglais.

*   **Pages Dynamiques :** Gestion des pages principales (`Home`, `About`, `Services`, `Portfolio`, `Contact`).
*   **Système de Sections :** Chaque page est composée de blocs modulaires.
    *   **Hero :** Bannière principale avec image de fond, titre, sous-titre et bouton d'action (CTA).
    *   **Intro :** Texte d'introduction riche.
    *   **Features :** Liste de points clés ou de services rapides.
    *   **Service :** Description détaillée d'une offre.
    *   **Contact :** Informations de contact structurées.
*   **Synchronisation FR/EN :**
    *   Création simultanée des versions FR et EN d'une section.
    *   Alignement automatique via `normalize_sections.py`.
    *   Indicateur visuel de parité dans l'admin.

## 2. Administration & Sécurité

Interface d'administration protégée (`/admin`) pour la gestion autonome du site.

*   **Authentification Forte :**
    *   Hachage des mots de passe via **Argon2** (standard de l'industrie).
    *   Protection contre les attaques par force brute (via délais de réponse).
    *   Session sécurisée (Cookies `HttpOnly`, `Secure`, `SameSite=Lax`).
*   **Médiathèque :**
    *   Upload d'images sécurisé (vérification des extensions).
    *   Renommage unique des fichiers (UUID) pour éviter les collisions.
    *   Visualisation et suppression des assets.
*   **Paramètres du Site (SiteSettings) :**
    *   Modification du Logo et Favicon à la volée.
    *   Configuration des liens sociaux (Facebook, Instagram, LinkedIn).
    *   Injection de l'ID Google Analytics.

## 3. Progressive Web App (PWA)

Le site est une PWA installable, offrant une expérience proche d'une application native.

*   **Manifest Dynamique (`/manifest.json`) :** Généré depuis la base de données (nom, couleurs, icônes configurables dans l'admin).
*   **Installation :** Invite d'installation sur mobile et desktop.
*   **Mode Standalone :** L'application se lance sans barre d'URL du navigateur.
*   **Service Worker :** Cache les assets statiques pour un chargement instantané.

## 4. SEO & Performance Technique

L'architecture est optimisée pour le référencement naturel et la vitesse.

*   **SEO Technique :**
    *   `sitemap.xml` généré dynamiquement pour toutes les pages actives.
    *   `robots.txt` configurable (bloque les bots indésirables, autorise Google/GPTBot).
    *   Balises Méta (Title, Description) éditables pour chaque page.
    *   Support OpenGraph pour le partage sur les réseaux sociaux.
*   **Performance :**
    *   Images servies via Nginx avec cache (headers `Expires`).
    *   CSS minifié (Tailwind via CDN).
    *   Base de données indexée sur les slugs et IDs.

## 5. Conformité & Sécurité Avancée

*   **Protection CSRF :** Tous les formulaires incluent un jeton unique anti-falsification (`Flask-WTF`).
*   **Content Security Policy (CSP) :** En-têtes stricts bloquant les scripts non autorisés (`Flask-Talisman`).
*   **Strict Transport Security (HSTS) :** Force le navigateur à n'utiliser que HTTPS.
*   **Sanitization :** Les entrées utilisateur sont nettoyées pour prévenir les injections SQL et XSS.
