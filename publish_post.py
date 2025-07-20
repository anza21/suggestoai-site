#!/usr/bin/env python3
"""
SuggestoAI Autonomous Affiliate Agent - Auto Publisher

Usage:
1. Command line: python3 publish_post.py --title "Product Title" --desc "Short description" --img "img_url_or_path" --afflink "affiliate_url" [--review "review_html"]
2. JSON input: python3 publish_post.py --json '{"title": "...", "description": "...", "image": "...", "affiliate_link": "...", "content": "...", "category": "...", "keywords": "..."}'

Features:
- Προσθέτει νέα card στο ai-recommends.html (πάνω-πάνω)
- Δημιουργεί blog post με SEO optimization
- Αυτόματο git commit & push
- RSS feed update
- Sitemap update
"""
import argparse
import datetime
import os
import json
import subprocess
import re
from bs4 import BeautifulSoup
from urllib.parse import quote

parser = argparse.ArgumentParser(description='Auto-publish AI product recommendation.')
parser.add_argument('--title', help='Product title')
parser.add_argument('--desc', help='Short description')
parser.add_argument('--img', help='Image URL or path')
parser.add_argument('--afflink', help='Affiliate link')
parser.add_argument('--review', help='Full HTML review (optional)')
parser.add_argument('--json', help='JSON input with all post data')
args = parser.parse_args()

def create_safe_filename(title):
    """Create safe filename from title"""
    safe_title = re.sub(r'[^a-zA-Z0-9\s-]', '', title.lower())
    safe_title = re.sub(r'\s+', '-', safe_title)
    return safe_title[:50]

def update_posts_json(post_data):
    """Update posts.json with new post metadata"""
    posts_file = 'blog/posts/posts.json'
    
    # Load existing posts
    if os.path.exists(posts_file):
        with open(posts_file, 'r', encoding='utf-8') as f:
            posts = json.load(f)
    else:
        posts = []
    
    # Add new post at the beginning
    posts.insert(0, post_data)
    
    # Save updated posts
    with open(posts_file, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)

def update_rss_feed(post_data):
    """Update RSS feed with new post"""
    rss_file = 'blog/rss.xml'
    
    if not os.path.exists(rss_file):
        return
    
    with open(rss_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'xml')
    
    # Find channel
    channel = soup.find('channel')
    if not channel:
        return
    
    # Create new item
    item = soup.new_tag('item')
    
    title_tag = soup.new_tag('title')
    title_tag.string = post_data['title']
    item.append(title_tag)
    
    link_tag = soup.new_tag('link')
    link_tag.string = f"https://suggestoai.com/blog/posts/{post_data['filename']}"
    item.append(link_tag)
    
    desc_tag = soup.new_tag('description')
    desc_tag.string = post_data['excerpt']
    item.append(desc_tag)
    
    pubdate_tag = soup.new_tag('pubDate')
    pubdate_tag.string = datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0000')
    item.append(pubdate_tag)
    
    guid_tag = soup.new_tag('guid')
    guid_tag.string = f"https://suggestoai.com/blog/posts/{post_data['filename']}"
    item.append(guid_tag)
    
    # Insert at the beginning
    channel.insert(0, item)
    
    # Update lastBuildDate
    last_build = channel.find('lastBuildDate')
    if last_build:
        last_build.string = datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0000')
    
    with open(rss_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))

def update_sitemap(post_data):
    """Update sitemap.xml with new blog post"""
    sitemap_file = 'sitemap.xml'
    
    if not os.path.exists(sitemap_file):
        return
    
    with open(sitemap_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'xml')
    
    # Find urlset
    urlset = soup.find('urlset')
    if not urlset:
        return
    
    # Create new url entry
    url_tag = soup.new_tag('url')
    
    loc_tag = soup.new_tag('loc')
    loc_tag.string = f"https://suggestoai.com/blog/posts/{post_data['filename']}"
    url_tag.append(loc_tag)
    
    lastmod_tag = soup.new_tag('lastmod')
    lastmod_tag.string = datetime.datetime.now().strftime('%Y-%m-%d')
    url_tag.append(lastmod_tag)
    
    changefreq_tag = soup.new_tag('changefreq')
    changefreq_tag.string = 'monthly'
    url_tag.append(changefreq_tag)
    
    priority_tag = soup.new_tag('priority')
    priority_tag.string = '0.8'
    url_tag.append(priority_tag)
    
    # Insert at the beginning
    urlset.insert(0, url_tag)
    
    with open(sitemap_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))

def git_commit_push():
    """Perform git add, commit, and push"""
    try:
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', f'Add new blog post - {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}'], check=True)
        subprocess.run(['git', 'push'], check=True)
        print("✅ Git commit & push successful")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")

def create_blog_post(post_data):
    """Create blog post HTML file from template"""
    template_file = 'blog/posts/template.html'
    
    if not os.path.exists(template_file):
        print("❌ Template file not found")
        return None
    
    with open(template_file, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Replace placeholders
    replacements = {
        '{{TITLE}}': post_data['title'],
        '{{DESCRIPTION}}': post_data['excerpt'],
        '{{KEYWORDS}}': post_data.get('keywords', ''),
        '{{IMAGE}}': post_data['image'],
        '{{FILENAME}}': post_data['filename'],
        '{{PUBLISH_DATE}}': post_data['date'],
        '{{CATEGORY}}': post_data['category'],
        '{{CONTENT}}': post_data['content']
    }
    
    for placeholder, value in replacements.items():
        template = template.replace(placeholder, str(value))
    
    # Write blog post file
    post_file = f"blog/posts/{post_data['filename']}"
    with open(post_file, 'w', encoding='utf-8') as f:
        f.write(template)
    
    return post_file

def main():
    # Parse JSON input if provided
    if args.json:
        try:
            json_data = json.loads(args.json)
            title = json_data.get('title', '')
            description = json_data.get('description', '')
            image = json_data.get('image', '')
            affiliate_link = json_data.get('affiliate_link', '')
            content = json_data.get('content', '')
            category = json_data.get('category', 'Product Review')
            keywords = json_data.get('keywords', '')
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON: {e}")
            return
    else:
        # Use command line arguments
        title = args.title or ''
        description = args.desc or ''
        image = args.img or ''
        affiliate_link = args.afflink or ''
        content = args.review or ''
        category = 'Product Review'
        keywords = ''
    
    if not title or not description or not image:
        print("❌ Missing required fields: title, description, image")
        return
    
    # Create safe filename
    safe_title = create_safe_filename(title)
    date_str = datetime.datetime.now().strftime('%Y%m%d')
    filename = f'{date_str}-{safe_title}.html'
    
    # Create post data
    post_data = {
        'title': title,
        'excerpt': description,
        'image': image,
        'filename': filename,
        'date': datetime.datetime.now().strftime('%B %d, %Y'),
        'category': category,
        'keywords': keywords,
        'content': content
    }
    
    # Create blog post if content is provided
    if content:
        post_file = create_blog_post(post_data)
        if post_file:
            print(f"✅ Blog post created: {post_file}")
    
    # Update posts.json
    update_posts_json(post_data)
    print("✅ Posts metadata updated")
    
    # Update RSS feed
    update_rss_feed(post_data)
    print("✅ RSS feed updated")
    
    # Update sitemap
    update_sitemap(post_data)
    print("✅ Sitemap updated")
    
    # Create card for ai-recommends.html
    readmore_btn = ''
    if content:
        readmore_btn = f'<a href="blog/posts/{filename}" class="cta-btn readmore-btn" style="font-size:1rem;">Read More</a>'
    
    CARD_TEMPLATE = f'''
<div class="feature" style="max-width:320px;">
  <img src="{image}" alt="{title}">
  <h3>{title}</h3>
  <p>{description}</p>
  <a href="{affiliate_link}" class="cta-btn" style="font-size:1rem;" target="_blank">Buy Now</a>
  {readmore_btn}
</div>
'''
    
    # Insert card at the top of the EN section in ai-recommends.html
    with open('ai-recommends.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    # Find EN section
    en_section = soup.find(id='recs-en')
    if en_section:
        features_div = en_section.find('div', class_='features')
        if not features_div:
            # Create if not exists
            features_div = soup.new_tag('div', **{'class': 'features', 'style': 'flex-wrap:wrap;gap:2rem;'})
            en_section.append(features_div)
        
        # Insert new card at the top
        card_html = BeautifulSoup(CARD_TEMPLATE, 'html.parser')
        features_div.insert(0, card_html)
        
        with open('ai-recommends.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        print("✅ Product card added to ai-recommends.html")
    
    # Git commit & push
    git_commit_push()
    
    print(f"✅ Post published successfully: {title}")
    if content:
        print(f"📝 Full blog post: blog/posts/{filename}")
    print(f"🔗 Blog URL: https://suggestoai.com/blog/posts/{filename}")

if __name__ == "__main__":
    main() 