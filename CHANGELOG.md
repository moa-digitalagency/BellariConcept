# Changelog / Journal des Modifications

All notable changes to Bellari Concept website will be documented in this file.

Tous les changements notables du site Bellari Concept seront documentés dans ce fichier.

---

## [1.2.0] - 2025-10-24

### Added / Ajouté
- ✅ **Complete English content** - Added all missing English translations for every page section / Ajout de toutes les traductions anglaises manquantes pour chaque section
- ✅ **Settings & SEO page** - New admin page for site configuration / Nouvelle page admin pour la configuration du site
  - Logo upload and management / Téléchargement et gestion du logo
  - SEO meta tags (keywords, Open Graph image) / Balises meta SEO (mots-clés, image Open Graph)
  - Google Analytics ID / ID Google Analytics
  - Social media links (Facebook, Instagram, LinkedIn) / Liens réseaux sociaux (Facebook, Instagram, LinkedIn)
- ✅ **Bilingual README** - Complete documentation in French and English / Documentation complète en français et anglais
- ✅ **Bilingual CHANGELOG** - Version history in both languages / Historique des versions dans les deux langues

### Changed / Modifié
- 🔄 Navigation menu updated to include Settings link / Menu de navigation mis à jour avec lien Paramètres
- 🔄 Mobile responsive improvements across all pages / Améliorations du responsive mobile sur toutes les pages

### Fixed / Corrigé
- 🐛 Missing English content - all sections now available in both languages / Contenu anglais manquant - toutes les sections maintenant disponibles dans les deux langues
- 🐛 Language switching now shows consistent content / Le changement de langue affiche maintenant un contenu cohérent

---

## [1.1.0] - 2025-10-24

### Added / Ajouté
- ✅ **Fully Rounded Buttons** - Changed all buttons from rounded-lg to rounded-full for maximum roundness / Changement de tous les boutons de rounded-lg à rounded-full pour un maximum d'arrondi
- ✅ **Bilingual Admin Interface** - Complete French/English admin panel with language persistence / Panneau admin complet français/anglais avec persistance de langue
- ✅ **Image Preview with Resolution** - Admin can now see image preview with width x height display / L'admin peut maintenant voir l'aperçu des images avec affichage largeur x hauteur
- ✅ **SEO Meta Descriptions** - Added meta_description field to Page model with character limit and recommendations / Ajout du champ meta_description au modèle Page avec limite de caractères et recommandations
- ✅ **Language Persistence Fix** - Language selection now persists across all admin operations (create, update, delete) / La sélection de langue persiste maintenant à travers toutes les opérations admin (créer, mettre à jour, supprimer)

### Changed / Modifié
- 🔄 Admin button styling updated to fully rounded / Style des boutons admin mis à jour en entièrement arrondi
- 🔄 Admin panel language toggle added / Bouton de changement de langue ajouté au panneau admin

---

## [1.0.0] - 2025-10-24

### Added / Ajouté
- ✅ **Multilingual Support** - Added French (default) and English language switching / Support multilingue français (par défaut) et anglais
- ✅ **Real Content** - Integrated actual Bellari Concept content from bellariconcept.com / Intégration du contenu réel de Bellari Concept depuis bellariconcept.com
- ✅ **Company Logo** - Added official Bellari Concept logo throughout the site / Ajout du logo officiel Bellari Concept sur tout le site
- ✅ **Professional Images** - Added stock images for all 6 services / Ajout d'images stock pour les 6 services
- ✅ **Floating Language Toggle** - Added FR/EN switcher in bottom left corner / Ajout du sélecteur FR/EN dans le coin inférieur gauche
- ✅ **Updated Contact Info** - Real contact details (bellari.groupe@gmail.com, +212 6 35 50 24 61, Marrakech) / Coordonnées réelles (bellari.groupe@gmail.com, +212 6 35 50 24 61, Marrakech)
- ✅ **Services** - Construction, Électricité, Plomberie, Peinture, Climatisation, Entretien de Piscine

### Features / Fonctionnalités
- ✅ Flask backend with PostgreSQL database / Backend Flask avec base de données PostgreSQL
- ✅ CMS system for content and image management / Système CMS pour la gestion de contenu et d'images
- ✅ Modern frontend with Tailwind CSS / Frontend moderne avec Tailwind CSS
- ✅ Admin authentication system / Système d'authentification admin
- ✅ 5 main pages: Home, About, Services, Portfolio, Contact / 5 pages principales: Accueil, À Propos, Services, Portfolio, Contact
- ✅ Security improvements: Protected database initialization, persistent SESSION_SECRET, admin-only access controls / Améliorations de sécurité: initialisation de base de données protégée, SESSION_SECRET persistant, contrôles d'accès admin uniquement

---

## Project Information / Informations sur le Projet

### Tech Stack / Stack Technologique
- **Frontend**: HTML, Tailwind CSS (CDN), Vanilla JavaScript
- **Backend**: Python 3.11, Flask, Flask-SQLAlchemy, Flask-Login
- **Database / Base de données**: PostgreSQL (Neon)
- **Image Processing / Traitement d'images**: Pillow

### Color Scheme / Palette de Couleurs
- Primary / Primaire: #1A1A1A (charcoal black / noir charbon)
- Secondary / Secondaire: #F8F8F8 (warm white / blanc chaud)
- Accent: #D4AF37 (elegant gold / or élégant)
- Text / Texte: #333333 (dark grey / gris foncé)
- Background / Fond: #FFFFFF (pure white / blanc pur)
- Subtle / Subtil: #E5E5E5 (light grey / gris clair)

### Typography / Typographie
- Display Font / Police d'affichage: Playfair Display (headings, logo / titres, logo)
- Body Font / Police de texte: Inter (content, UI / contenu, interface)

---

## Changelog Format / Format du Journal

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/), et ce projet adhère au [Versionnage Sémantique](https://semver.org/lang/fr/spec/v2.0.0.html).

### Categories / Catégories
- `Added` / `Ajouté` for new features / pour les nouvelles fonctionnalités
- `Changed` / `Modifié` for changes in existing functionality / pour les changements dans les fonctionnalités existantes
- `Deprecated` / `Déprécié` for soon-to-be removed features / pour les fonctionnalités bientôt supprimées
- `Removed` / `Supprimé` for now removed features / pour les fonctionnalités maintenant supprimées
- `Fixed` / `Corrigé` for any bug fixes / pour toute correction de bugs
- `Security` / `Sécurité` in case of vulnerabilities / en cas de vulnérabilités
