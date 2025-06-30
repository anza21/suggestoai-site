# SuggestoAI Autonomous Affiliate Agent Site

## Πώς να δημοσιεύσεις νέο AI post

1. Εγκατέστησε τα requirements:
   ```
pip install -r requirements.txt
   ```
2. Τρέξε το script:
   ```
python3 publish_post.py --title "Product Title" --desc "Short description" --img "img_url_or_path" --afflink "affiliate_url" [--review "review_html"]
   ```
   - Θα προσθέσει νέα κάρτα στο ai-recommends.html (πάνω-πάνω)
   - Αν δώσεις --review, θα δημιουργήσει και νέο HTML post

## Πώς να κάνεις commit & push στο GitHub

```bash
git add .
git commit -m "Add new AI product post"
git push
```

## SEO & Extra
- Sitemap: sitemap.xml
- RSS feed: rss.xml
- Google Analytics: (δες index.html για integration)

## Contact
contact@suggestoai.com