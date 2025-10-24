# Guide de Mise à Jour - Bellari Concept

## 📦 Ajout de la Section Expertise

Si vous avez déjà une installation existante et que vous souhaitez ajouter la nouvelle section "Expertise" entre le héro et les services, suivez ces étapes :

### Option 1: Script Automatique (Recommandé)

```bash
# Activer l'environnement virtuel
source .venv/bin/activate

# Exécuter le script d'ajout
python3 add_expertise_section.py
```

Le script va :
- ✅ Vérifier si la section existe déjà
- ✅ Mettre à jour les order_index des sections existantes
- ✅ Ajouter la section expertise en FR et EN
- ✅ La positionner entre le héro (0) et les autres sections

### Option 2: Ajout Manuel via SQL

Si vous préférez ajouter manuellement la section via SQL :

```sql
-- Récupérer l'ID de la page d'accueil
SELECT id FROM page WHERE slug = 'home';

-- Mettre à jour les order_index des sections existantes (augmenter de 1)
UPDATE section 
SET order_index = order_index + 1 
WHERE page_id = (SELECT id FROM page WHERE slug = 'home') 
AND order_index >= 1;

-- Ajouter la section expertise en français
INSERT INTO section (
    page_id, 
    section_type, 
    language_code, 
    heading, 
    subheading, 
    content, 
    image_url, 
    order_index, 
    is_active
) VALUES (
    (SELECT id FROM page WHERE slug = 'home'),
    'expertise',
    'fr',
    'Nous vous aidons à réaliser les projets de vos rêves',
    'Excellence et expertise au service de vos ambitions',
    'Avec Bellari Concept, chaque projet est un gage de qualité. Notre équipe spécialisée offre une maîtrise technique inégalée, allant de la construction à l''entretien de piscines. Nous mettons l''excellence au cœur de tout ce que nous faisons, transformant vos visions en réalités durables et esthétiquement plaisantes.',
    '/static/images/modern_construction__e4781d44.jpg',
    1,
    true
);

-- Ajouter la section expertise en anglais
INSERT INTO section (
    page_id, 
    section_type, 
    language_code, 
    heading, 
    subheading, 
    content, 
    image_url, 
    order_index, 
    is_active
) VALUES (
    (SELECT id FROM page WHERE slug = 'home'),
    'expertise',
    'en',
    'We help you realize your dream projects',
    'Excellence and expertise at the service of your ambitions',
    'With Bellari Concept, each project is a guarantee of quality. Our specialized team offers unparalleled technical mastery, from construction to pool maintenance. We put excellence at the heart of everything we do, transforming your visions into lasting and aesthetically pleasing realities.',
    '/static/images/modern_construction__e4781d44.jpg',
    1,
    true
);
```

### Option 3: Ajouter via l'Interface Admin

1. Connectez-vous à `/admin/login`
2. Allez dans "Pages" et sélectionnez la page "Home"
3. Cliquez sur "Créer une nouvelle section"
4. Configurez :
   - **Type de section**: expertise
   - **Langue**: Français (fr)
   - **Order Index**: 1
   - **Titre**: Nous vous aidons à réaliser les projets de vos rêves
   - **Sous-titre**: Excellence et expertise au service de vos ambitions
   - **Contenu**: [Votre texte]
   - **URL de l'image**: /static/images/modern_construction__e4781d44.jpg
   - **Active**: ✓
5. Répétez pour la version anglaise (language_code: en)

## 🔄 Vérification

Après l'ajout, vérifiez que la section s'affiche correctement :

```bash
# Vérifier les sections de la page d'accueil
psql -U bellari_user -d bellari_concept -c "
SELECT section_type, language_code, heading, order_index 
FROM section 
WHERE page_id = (SELECT id FROM page WHERE slug = 'home') 
ORDER BY order_index;
"
```

Vous devriez voir :
```
section_type | language_code | heading                                    | order_index
-------------+---------------+--------------------------------------------+-------------
hero         | fr            | BELLARI CONCEPT                            | 0
hero         | en            | BELLARI CONCEPT                            | 0
expertise    | fr            | Nous vous aidons à réaliser...             | 1
expertise    | en            | We help you realize your dream...          | 1
intro        | fr            | Créer des Espaces Intemporels              | 2
intro        | en            | Creating Timeless Spaces                   | 2
features     | fr            | Notre Expertise                            | 3
features     | en            | Our Expertise                              | 3
```

## 🎨 Personnalisation

Vous pouvez personnaliser la section expertise depuis le panneau admin :

1. Modifier le texte (heading, subheading, content)
2. Changer l'image (image_url)
3. Activer/désactiver la section (is_active)
4. Réorganiser sa position (order_index)

Les modifications seront visibles immédiatement sur le site.

## 🔧 Dépannage

### La section ne s'affiche pas

1. Vérifiez que is_active = true
2. Vérifiez que le template index.html contient le bloc pour section_type='expertise'
3. Effacez le cache du navigateur (Ctrl+Shift+R)
4. Redémarrez le serveur

### L'ordre des sections est incorrect

Utilisez le script de normalisation des sections :

```bash
# Via l'interface admin
Accédez à /admin/normalize-sections

# Ou via SQL
UPDATE section SET order_index = 0 WHERE section_type = 'hero' AND page_id = (SELECT id FROM page WHERE slug = 'home');
UPDATE section SET order_index = 1 WHERE section_type = 'expertise' AND page_id = (SELECT id FROM page WHERE slug = 'home');
UPDATE section SET order_index = 2 WHERE section_type = 'intro' AND page_id = (SELECT id FROM page WHERE slug = 'home');
UPDATE section SET order_index = 3 WHERE section_type = 'features' AND page_id = (SELECT id FROM page WHERE slug = 'home');
```

## 📝 Notes

- La section expertise utilise le même système de gestion que les autres sections
- Elle est totalement bilingue (FR/EN) et s'adapte automatiquement à la langue sélectionnée
- Le design est responsive et s'adapte à tous les écrans
- Vous pouvez créer plusieurs sections expertise si nécessaire en changeant l'order_index

Pour toute question, consultez la documentation complète dans `README_DEPLOYMENT.md`.
