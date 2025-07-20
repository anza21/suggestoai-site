# SuggestoAI Blog System

## Overview
Το blog σύστημα του SuggestoAI επιτρέπει την αυτόματη δημιουργία και δημοσίευση blog posts με SEO optimization, RSS feeds, και social sharing.

## Δομή Αρχείων
```
blog/
├── index.html          # Blog homepage με λίστα posts
├── rss.xml            # RSS feed για το blog
├── README.md          # Αυτό το αρχείο
└── posts/
    ├── template.html  # Template για blog posts
    └── posts.json     # Metadata όλων των posts
```

## Χρήση του publish_post.py

### 1. JSON Input (Προτεινόμενο)
```bash
python3 publish_post.py --json '{
  "title": "Τίτλος Post",
  "description": "Σύντομη περιγραφή",
  "image": "URL εικόνας",
  "affiliate_link": "Affiliate link",
  "content": "<p>HTML περιεχόμενο</p>",
  "category": "Κατηγορία",
  "keywords": "keywords, για, SEO"
}'
```

### 2. Command Line Arguments
```bash
python3 publish_post.py \
  --title "Τίτλος Post" \
  --desc "Σύντομη περιγραφή" \
  --img "URL εικόνας" \
  --afflink "Affiliate link" \
  --review "<p>HTML περιεχόμενο</p>"
```

## Χαρακτηριστικά

### ✅ Αυτόματη Δημιουργία
- Blog post HTML με responsive design
- SEO meta tags (title, description, keywords)
- Open Graph tags για social media
- Structured data για search engines

### ✅ RSS Feed
- Αυτόματη ενημέρωση RSS feed
- Συμβατό με RSS readers
- Last build date tracking

### ✅ Sitemap Integration
- Αυτόματη προσθήκη στο sitemap.xml
- SEO-friendly URLs
- Priority και changefreq settings

### ✅ Git Integration
- Αυτόματο git add, commit, push
- Descriptive commit messages
- SSH remote support

### ✅ Social Sharing
- Twitter, Facebook, LinkedIn buttons
- Open Graph optimization
- Social media previews

### ✅ Related Posts
- Αυτόματη εμφάνιση related posts
- Dynamic loading από posts.json
- Responsive grid layout

## SEO Features

### Meta Tags
- Title optimization
- Description meta tag
- Keywords meta tag
- Author information

### Open Graph
- og:title, og:description, og:image
- og:type = article
- og:url με canonical URL

### Twitter Cards
- twitter:card = summary_large_image
- twitter:title, twitter:description
- twitter:image optimization

### Structured Data
- Article schema markup
- Author information
- Publication date
- Category classification

## Template Variables

Το template.html χρησιμοποιεί τα εξής placeholders:

- `{{TITLE}}` - Τίτλος του post
- `{{DESCRIPTION}}` - Meta description
- `{{KEYWORDS}}` - SEO keywords
- `{{IMAGE}}` - Featured image URL
- `{{FILENAME}}` - HTML filename
- `{{PUBLISH_DATE}}` - Ημερομηνία δημοσίευσης
- `{{CATEGORY}}` - Κατηγορία post
- `{{CONTENT}}` - HTML περιεχόμενο

## External Agent Integration

Για external agents, χρησιμοποιήστε το JSON format:

```json
{
  "title": "Product Review Title",
  "description": "Short product description for meta tags",
  "image": "https://example.com/product-image.jpg",
  "affiliate_link": "https://amazon.com/dp/PRODUCTID",
  "content": "<h2>Full HTML review content</h2><p>...</p>",
  "category": "Product Review",
  "keywords": "product, review, affiliate, recommendations"
}
```

## Dependencies

```bash
pip3 install beautifulsoup4 lxml
```

## URLs

- Blog Homepage: `https://suggestoai.com/blog/`
- RSS Feed: `https://suggestoai.com/blog/rss.xml`
- Individual Post: `https://suggestoai.com/blog/posts/YYYYMMDD-title.html`

## Troubleshooting

### Common Issues
1. **ModuleNotFoundError: No module named 'bs4'**
   - Εγκαταστήστε: `pip3 install beautifulsoup4`

2. **XML parser error**
   - Εγκαταστήστε: `pip3 install lxml`

3. **Git push fails**
   - Ελέγξτε SSH keys και remote configuration

### Validation
- Ελέγξτε το blog στο: `https://suggestoai.com/blog/`
- RSS feed: `https://suggestoai.com/blog/rss.xml`
- Sitemap: `https://suggestoai.com/sitemap.xml` 