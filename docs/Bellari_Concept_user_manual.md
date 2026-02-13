# Bellari Concept - Manuel d'Utilisation

Bienvenue dans le guide d'utilisation du CMS Bellari Concept. Ce manuel vous aidera à gérer votre site web, mettre à jour le contenu et configurer les paramètres sans connaissances techniques avancées.

---

## 1. Accès au Panneau d'Administration

1.  Ouvrez votre navigateur et allez sur l'adresse de votre site suivie de `/admin/login` (ex: `https://www.bellari-concept.com/admin/login`).
2.  Entrez votre **Nom d'utilisateur** et votre **Mot de passe**.
3.  Cliquez sur **Se connecter**.

*Note : Pour des raisons de sécurité, votre session expire automatiquement après une période d'inactivité.*

---

## 2. Tableau de Bord (Dashboard)

Une fois connecté, vous arrivez sur le tableau de bord. Il vous offre une vue d'ensemble rapide :
*   **Pages :** Liste de toutes les pages actives de votre site.
*   **Dernières Images :** Aperçu des 10 dernières images uploadées.
*   **Actions Rapides :** Liens directs vers la gestion des pages, la médiathèque ou les paramètres.

---

## 3. Gestion du Contenu (CMS)

### Modifier une Page existante
1.  Dans le menu latéral ou le tableau de bord, cliquez sur **Pages & Contenu**.
2.  Repérez la page que vous souhaitez modifier (ex: `home`, `about`, `services`) et cliquez sur le bouton **Éditer** (icône crayon).

### L'Interface d'Édition Bilingue
L'éditeur est conçu pour travailler simultanément sur les versions Française (FR) et Anglaise (EN).
*   Chaque section est présentée par paire (FR à gauche, EN à droite).
*   Vous pouvez modifier les textes, les titres et les images indépendamment pour chaque langue.

### Ajouter une Nouvelle Section
En bas de la page d'édition :
1.  Repérez le formulaire **Ajouter une Section**.
2.  Choisissez le **Type de Section** (Hero, Texte, Service, etc.).
3.  Remplissez le contenu pour le **Français** et l'**Anglais**.
4.  Cliquez sur **Créer**. La section sera ajoutée à la fin de la page.

### Réorganiser les Sections
L'ordre d'affichage est déterminé par l'**Index d'Ordre** (0, 1, 2...).
*   Pour changer l'ordre, modifiez manuellement le champ "Index" de chaque section.
*   **Astuce :** Si l'ordre devient confus, utilisez l'outil **Normaliser les Sections** dans le menu principal pour réinitialiser proprement la numérotation (0, 1, 2, 3...) sans changer l'ordre visuel actuel.

---

## 4. Médiathèque (Images)

Avant d'ajouter une image dans une section, vous devez l'uploader dans la médiathèque.

### Uploader une Image
1.  Cliquez sur **Médiathèque** dans le menu latéral.
2.  Utilisez la zone de **Glisser-Déposer** ou cliquez pour sélectionner un fichier depuis votre ordinateur.
3.  Formats acceptés : JPG, PNG, WEBP.
4.  Une fois l'upload terminé, l'image apparaît dans la liste.

### Utiliser une Image dans une Section
1.  Dans la Médiathèque, repérez l'image souhaitée.
2.  Copiez l'**URL** affichée sous l'image (ex: `/static/uploads/a1b2c3d4_monimage.jpg`).
3.  Retournez dans l'éditeur de page.
4.  Collez l'URL dans le champ **URL de l'image** ou **Image de fond** de la section concernée.

---

## 5. Configuration du Site

Le menu **Paramètres** vous permet de contrôler l'identité et le comportement global du site.

### Identité Visuelle
*   **Logo du Site :** Changez le logo principal affiché dans la barre de navigation.
*   **Favicon :** Changez l'icône affichée dans l'onglet du navigateur.
*   **Nom du Site :** Mettez à jour le nom affiché dans les résultats de recherche (FR et EN).

### SEO & Réseaux Sociaux
*   **Mots-clés par défaut :** Définissez les meta-keywords pour les moteurs de recherche.
*   **Image OpenGraph :** L'image qui s'affiche lorsque votre site est partagé sur Facebook, LinkedIn ou WhatsApp.
*   **Liens Sociaux :** Remplissez les champs Facebook, Instagram, LinkedIn pour afficher les icônes dans le pied de page (footer).

### Progressive Web App (PWA)
Transformez votre site en application mobile installable.
1.  Activez l'option **Activer PWA**.
2.  Personnalisez le **Nom de l'App** (tel qu'il apparaîtra sur l'écran d'accueil du téléphone).
3.  Choisissez une **Couleur de Thème** (couleur de la barre de statut Android/iOS).
4.  Uploadez une **Icône d'App** (carrée, min. 512x512px).
5.  Sauvegardez. Les visiteurs mobiles verront désormais une invite pour "Installer l'application".
